import requests
from bs4 import BeautifulSoup
import openpyxl

# 페이지 번호만큼 수동으로 넣어줬음.
maximum = 65
page = 0

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sbs.sogang.ac.kr/sbs/sbs02_1.html', headers=headers)
html = data.content.decode('utf-8', 'replace')
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select('#body > div.main > div.section > div > table > tbody > tr')
for tr in trs:
    if tr.select_one('tr > td:nth-child(2) > p > b') is not None:
        name = tr.select_one('tr > td:nth-child(2) > p > b').text
        name = name.split(' ')[0]
        a = tr.select_one('tr > td:nth-child(2) > p').text
        a1 = a.split('·')[2]
        tit = a1.split(':')[1]

        b = a.split('·')[5]
        email = b.split(':')[1]

        c = a.split('·')[4]
        tel = c.split(':')[1]

        print(name, tit, email, tel)
        sheet.append([name, tit, email, tel])

wb.save("professor.xlsx")
