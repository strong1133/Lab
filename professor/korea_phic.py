import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for i in range(1, 2):
    url = 'https://www.knsu.ac.kr/web/kor/u_01_03_02'

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    ul = soup.select('#p_p_id_EXT_GYOSU_ > div > div > div > div > dl')
    for li in ul:
        name = li.select_one('div > dl > dd:nth-child(4)').text
        tit = li.select_one('div > dl > dd:nth-child(2)').text + " " + li.select_one('div > dl > dd:nth-child(6)').text
        email = li.select_one('div > dl > dd:nth-child(10) > a').text
        tel = li.select_one('div > dl > dd:nth-child(8)').text
        print(name, tit, email, tel)
        sheet.append([name, tit, email, tel])
        wb.save("professor.xlsx")




# https://www.knsu.ac.kr/web/kor/u_01_02_01_tab01
# https://www.knsu.ac.kr/web/kor/u_01_02_02_tab01
