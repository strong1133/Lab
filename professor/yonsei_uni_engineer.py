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
data = requests.get('https://fis.yonsei.ac.kr/faculty/dep_search.do', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

ul = soup.select('#jwxe_main_content > div.belong-wrap > div > div:nth-child(5) > dl > dd > ul > li')

for li in ul:
    a = li.select_one('a')['href']
    tit = li.select_one('a').text
    tit = tit.split('/')[0]
    # print(tit)
    base = 'https://fis.yonsei.ac.kr/'
    url = base + a
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    divs = soup.select('#jwxe_main_content > div.belong-wrap > div > div.pro-list > div')
    for dls in divs:
        if dls.select_one('dl > dt > a') is None:
            name = dls.select_one('dl > dt').text.strip()
            name = name.split(' ')[0]
        else:
            name = dls.select_one('dl > dt > a').text.strip()
            name = name.split(' ')[0]

        email = dls.select_one('dl > dd.pro-info-etc > ul > li:nth-child(1) > a').text
        tel = dls.select_one('dl > dd.pro-info-etc > ul > li:nth-child(2)').text.strip()
        doc = {
            'name': name,
            'tit': tit,
            'email': email,
            'tel': tel
        }
        print(doc)
        sheet.append([name, tit, email, tel])


wb.save("professor.xlsx")


