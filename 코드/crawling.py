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
weather_text=[]
job_text=[]
result={}


def clean_text(text):
	cleaned_text = re.sub('[a-zA-Z]', '', text)
	cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', cleaned_text)
	return cleaned_text
for page_number in range(1, 11000):
	URL = 'https://www.csi.go.kr/acd/acdCaseView.do?case_no='+str(page_number)
	response = requests.get(URL)
	soup = BeautifulSoup(response.text, 'html.parser')

	find_date = soup.select("#main > div:nth-child(12) > table > tbody > tr:nth-child(2) > td:nth-child(2)")
	find_weather = soup.select("#main > div:nth-child(12) > table > tbody > tr:nth-child(3) > td:nth-child(4) > div > span:nth-child(1) > label")
	find_job = soup.select("#main > div:nth-child(12) > table > tbody > tr:nth-child(9) > td.t-left")
	find_worker = soup.select("#main > div:nth-child(14) > table > tbody > tr:nth-child(6) > td.t-left > div > div")

	for date in find_date:
		date1= str(date.text)
		date_text.append(date1)

	for weather in find_weather:
		weather1= str(weather.text)
		weather1 = weather1.replace("\r","").replace("\n","").replace("\t","")
		weather_text.append(weather1)

	for job in find_job:
		job1= str(job.text)
		job1 = job1.replace("\r","").replace("\n","").replace("\t","")
		job_text.append(job1)

	for worker in find_worker:
		worker1= str(worker.text)
		worker1 = worker1.replace("\r","").replace("\n","").replace("\t","")
		worker_text.append(worker1)

result={'date':date_text ,'worker':worker_text}
df = pd.DataFrame(result)
#print(df)
df.to_excel("result.xlsx")

