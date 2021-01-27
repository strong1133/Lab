import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

v = [36, 37, 38, 39]
va = ['소프트웨어학부', '차세대기술공학부', '미래사회공학부', '휴먼기계바이오공학부']
for i in range(len(v)):
    url = 'http://www.ewha.ac.kr/ewha/academics/eltec-engineering-prof.do?deptUniNo=' + str(v[i])
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    divs = soup.select('#jwxe_main_content > div > div.bn-list-person01.type01 > div > div> div')
    for div in divs:
        if div.select_one('div > div.b-prof-box01 > p > span > a') is not None:
            name = div.select_one('div > div.b-prof-box01 > p > span > a').text.strip()
        if div.select_one('div > div.b-prof-box01 > p > a.b-email') is not None:
            email = div.select_one('div > div.b-prof-box01 > p > a.b-email').text
        if div.select_one('div > div.b-prof-box01 > div > ul.b-prof-list.type01 > li.b-tel > a') is not None:
            tel = div.select_one('div > div.b-prof-box01 > div > ul.b-prof-list.type01 > li.b-tel > a').text
        tit = va[i]
        print(name,tit, email, tel)
        sheet.append([name, tit, email, tel])
wb.save("professor.xlsx")

# sheet.append([name, tit, email, tel])
# wb.save("professor.xlsx")
