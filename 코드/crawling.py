import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime
#엑셀로 저장하기 위한 변수
RESULT_PATH ='C:/Users/yangj/OneDrive/바탕 화면/캡스톤2/capstone2/capstone2/코드'  #결과 저장할 경로
now = datetime.now() #파일이름 현 시간으로 저장하기
date_text =[]
worker_text=[]
result={}


def clean_text(text):
	cleaned_text = re.sub('[a-zA-Z]', '', text)
	cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', cleaned_text)
	return cleaned_text
for page_number in range(70, 120):
	URL = 'https://www.csi.go.kr/acd/acdCaseView.do?case_no='+str(page_number)
	response = requests.get(URL)
	soup = BeautifulSoup(response.content, 'html.parser')
	find_date = soup.select("#main > div:nth-child(12) > table > tbody > tr:nth-child(2) > td:nth-child(2)")
	find_worker = soup.select("#main > div:nth-child(14) > table > tbody > tr:nth-child(6) > td.t-left > div > div")
	for date in find_date:
		date1= str(date.text)
		date_text.append(date1)
	for worker in find_worker:
		worker1= str(worker.text)
		worker_text.append(worker1)

result={'date':date_text ,'worker':worker_text}
df = pd.DataFrame(result)
df.to_excel(RESULT_PATH,sheet_name='sheet1')

