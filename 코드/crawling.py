import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
#엑셀로 저장하기 위한 변수
RESULT_PATH ='C: '  #결과 저장할 경로
now = datetime.now() #파일이름 현 시간으로 저장하기

whole_source = ""
for page_number in range(1, maximum+1):
	URL = 'http://land.naver.com/news/field.nhn?page=' + str(page_number)
	response = requests.get(URL)
	whole_source = whole_source + response.text
soup = BeautifulSoup(whole_source, 'html.parser')
find_title = soup.select("#content > div.section_headline > ul > li > dl > dt > a")

for title in find_title:
	print(title.text)

