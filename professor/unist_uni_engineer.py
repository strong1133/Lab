import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

url = 'https://unist-kor.unist.ac.kr/academics/undergraduate-programs/academics-at-a-glance/'
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

lis = soup.select('#post-622 > div > div > div > div > ul > li:nth-child(2) > div.cont > ul > li')
for li in lis:
    tit = li.select_one('a').text
    base_url = li.select_one('a')['href']
    base_url = base_url.split('kor')[0]
    url = 'kor/people/faculty_school/'
    tit_url = base_url + url
    print(tit, tit_url)

# post-622 > div > div > div > div > ul > li:nth-child(2) > div.cont > ul > li:nth-child(1) > a
# post-622 > div > div > div > div > ul > li:nth-child(2) > div.cont > ul > li:nth-child(2) > a


# https://me.unist.ac.kr/kor/people/faculty_school/
# https://nuclear.unist.ac.kr/kor/people/faculty_school/

# sheet.append([name, tit, email, tel])
# wb.save("professor.xlsx")
