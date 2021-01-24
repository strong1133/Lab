import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

page = 1
maximum = 33

sheet.append(["이름", "소속", "이메일", "전화번호"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for page in range(maximum):
    url = 'http://www.postech.ac.kr/research/research-activities/faculty-directory/page/' + str(page) + '/'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    ul = soup.select('#post-152 > div > div > div.plist_contbox > div > div.unit_cont_ro.unit2 > div > div > ul > li')
    for li in ul:
        name = li.select_one('div > div.hc_wrap > div.h_slat > a > div').text
        tit = li.select_one('div > div.hc_wrap > div.h_slat > div').text
        email = li.select_one('div > div.hc_wrap > div.c_slat > div.c_info2 > span > a').text
        tel = li.select_one('div > div.hc_wrap > div.c_slat > div.c_info1 > span').text
        print(name, tit, email, tel)
        sheet.append([name, tit, email, tel])
    page += 1
wb.save("professor.xlsx")

# sheet.append([name, tit, email, tel])
# wb.save("professor.xlsx")

#post-152 > div > div > div.plist_contbox > div > div.unit_cont_ro.unit2 > div > div > ul > li:nth-child(6) > div > div.hc_wrap > div.c_slat > div.c_info1 > span
#post-152 > div > div > div.plist_contbox > div > div.unit_cont_ro.unit2 > div > div > ul > li:nth-child(5) > div > div.hc_wrap > div.h_slat > div
# post-152 > div > div > div.plist_contbox > div > div.unit_cont_ro.unit2 > div > div > ul > li:nth-child(1) > div > div.hc_wrap > div.h_slat > a > div
# post-152 > div > div > div.plist_contbox > div > div.unit_cont_ro.unit2 > div > div > ul > li:nth-child(2) > div > div.hc_wrap > div.h_slat > a > div
#post-152 > div > div > div.plist_contbox > div > div.unit_cont_ro.unit2 > div > div > ul > li:nth-child(8) > div > div.hc_wrap > div.c_slat > div.c_info2 > span > a