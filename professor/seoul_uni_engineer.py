import requests
from bs4 import BeautifulSoup
import openpyxl

# 페이지 번호만큼 수동으로 넣어줬음.
maximum = 65
page = 0

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "전화번호","이메일"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://eng.snu.ac.kr/professor?&title=&page=0', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# url에 page번호를 달아주기 위해 페이지 번호량 만큼 반복문
for page in range(maximum):
    data = requests.get('https://eng.snu.ac.kr/professor?&title=&page=' + str(page), headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    ul = soup.select('#block-system-main > div > div > div.view-content > ul > li')
    for li in ul:
        name = li.select_one(' dl > dt > a').text
        name_url =li.select_one(' dl > dt > a')['href']

        data = requests.get('https://eng.snu.ac.kr' + name_url, headers=headers)
        soup2 = BeautifulSoup(data.text, 'html.parser')

        tel = soup2.select_one('#block-system-main > div > table > tbody > tr:nth-child(2) > td')
        tel = '02-'+ tel.text


        belong = li.select_one(' dl > dd ').text
        a = belong.split('|')[0]
        b = a.split('\n')[1]
        if li.select_one(' dl > dd > a:nth-child(13)') is not None:
            email = li.select_one(' dl > dd > a:nth-child(13)').text
        elif li.select_one(' dl > dd > a:nth-child(14)') is None:
            email = "이메일이 없습니다."
        else:
            email = li.select_one(' dl > dd > a:nth-child(14)').text

        doc = {
            'name': name,
            'belong': b,
            'email': email,
            'tel' : tel
        }

        print(doc)
        sheet.append([name, b, email, tel])

    page += 1

wb.save("professor.xlsx")

#https://eng.snu.ac.kr/node/16970