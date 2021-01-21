import requests
from bs4 import BeautifulSoup
import openpyxl

# 페이지 번호만큼 수동으로 넣어줬음.
maximum = 7
page = 1

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for v in range(maximum):
    data = requests.get('https://cba.snu.ac.kr/ko/faculty?major=' + str(page), headers=headers)
    html = data.content.decode('euc-kr', 'replace')
    soup = BeautifulSoup(html, 'html.parser')

    ul = soup.select('#tabm6_1 > div > ul')
    for li in ul:

        # p3_11 > div.faulty_tab > ul > li.m1 > a
        # p3_11 > div.faulty_tab > ul > li.m2 > a
        name_link = li.select_one('li > a ')['href']
        if name_link.startswith('http') == True:
            name_link = 0
        base = 'https://cba.snu.ac.kr'
        if name_link != 0:
            url = base + name_link
        # print(url)

        data2 = requests.get(url, headers=headers)
        html2 = data2.content.decode('euc-kr', 'replace')
        soup2 = BeautifulSoup(html2, 'html.parser')
        ul2 = soup2.select('#facultyinfo > div > ul')
        for li2 in ul2:
            name = li2.select_one('li:nth-child(1) > p > span.kname').text
            email = li2.select_one('li:nth-child(5) > span > a').text
            tel = li2.select_one('li:nth-child(4)').text
            tit = "경영대학"
            # print(name, email, tel)
            sheet.append([name, tit, email, tel])

    page += 1

wb.save("professor.xlsx")