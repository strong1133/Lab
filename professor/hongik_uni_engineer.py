import requests
from bs4 import BeautifulSoup
import openpyxl
from selenium import webdriver

chrome_driver_dir = './chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

driver = webdriver.Chrome(chrome_driver_dir,
                          chrome_options=chrome_options)
driver.get('http://www.hongik.ac.kr/front/hakkwainfoview.do?campusGubun=1&dept_code=AAB100&depth=1')

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select('#hakkwaGyosu > div > div > table > tbody')

for tr in trs:
    name = tr.select_one('tr.t1 > td:nth-child(2)').text
    tit = tr.select_one('tr.t1 > td:nth-child(3)').text
    email = tr.select_one('tr.t2 > td > div > div > div > div:nth-child(1) > div:nth-child(2) > p > a').text
    tel = tr.select_one('tr.t2 > td > div > div > div > div:nth-child(2) > div:nth-child(4) > p').text
    doc = {
        'name': name,
        'tit': tit,
        'email': email,
        'tel': tel,
    }
    print(doc)
    sheet.append([name, tit, email, tel])
driver.quit()
wb.save("professor.xlsx")
