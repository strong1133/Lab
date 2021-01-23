import requests
from bs4 import BeautifulSoup
import openpyxl

# 페이지 번호만큼 수동으로 넣어줬음.
maximum = 65
page = 0

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

page = 1
maximum = 100


for page in range(maximum):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://eng.sogang.ac.kr/eng/eng01_4_' + str(page) + '.html', headers=headers)
    html = data.content.decode('utf-8', 'replace')
    soup = BeautifulSoup(html, 'html.parser')

    if soup.select_one('#body > div.main > div.section > div.titl0 > b') is not None:
        tit = soup.select_one('#body > div.main > div.section > div.titl0 > b').text


    trs = soup.select('#body > div.main > div.section > div.table0 > table > tbody > tr')
    for tr in trs:
        name = tr.select_one('tr > td').text
        email = tr.select_one('tr > td:nth-child(5)').text
        email = email + '@sogang.ac.kr'
        tel = tr.select_one('tr > td:nth-child(4)').text
        tel = '02-705-' + tel

        print(name, tit, email, tel)
        sheet.append([name, tit, email, tel])
    page += 1


wb.save("professor.xlsx")




#  sheet.append([name, tit, email, tel])
# wb.save("professor.xlsx")
