import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["이름", "소속", "이메일", "전화번호"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

arr = [5,6,7,8,9,10]
for i in arr:
    url = 'https://www.gachon.ac.kr/major/professor.jsp?h3=arts&h4=0'+str(i)

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    ul = soup.select('#content > div')
    for li in ul:
        if li.select_one('div > ul > li:nth-child(1)') is not None:
            name = li.select_one('div > ul > li:nth-child(1)').text.split('(')[0].split(":")[-1].strip()
            tit = li.select_one('div > ul > li:nth-child(1)').text.split('(')[-1].split(")")[0].strip()
            if li.select_one('div > ul > li:nth-child(3) > a') is not None:
                email = li.select_one('div > ul > li:nth-child(3) > a').text
                if li.select_one('div > ul > li:nth-child(5)') is not None:
                    tel = li.select_one('div > ul > li:nth-child(5)').text.split('/')[-1].strip()
                    print(name, tit, email, tel)
                    sheet.append([name, tit, email, tel])

wb.save("professor.xlsx")

