import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["이름", "소속", "이메일", "전화번호"])

chrome_driver_dir = './chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

driver = webdriver.Chrome(chrome_driver_dir,
                          chrome_options=chrome_options)
page = 1
maximum = 2

for v in range(maximum):
    driver.get('https://me.kaist.ac.kr/team/team_010100.html?page=' + str(
        page) + '&plist=&find_field=&find_word=&find_state=&find_ordby=&conf=&mode=1')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.select('body > div.home.sub > div.sub_section_wrap > div > div > div.team_list > ul > li')
    for li in lis:
        name = li.select_one('div > div.txt_bx > a > p').text
        name_url = li.select_one('div > div.txt_bx > a')['href']
        base_url = 'https://me.kaist.ac.kr/'
        url = base_url + name_url

        driver.get(url)
        html = driver.page_source
        soup2 = BeautifulSoup(html, 'html.parser')
        divs = soup2.select('body > div > div > div > div > div.txt_bx > div')
        for div in divs:
            if div.select_one('dl:nth-child(5) > dd > a') is not None:
                email = div.select_one('dl:nth-child(5) > dd > a').text
            if div.select_one('dl:nth-child(7) > dd') is not None:
                tel = div.select_one('dl:nth-child(7) > dd').text
                tit='기계공학과'
                doc = {
                    'name': name,
                    'tit': tit,
                    'email': email,
                    'tel': tel
                }
                print(doc)
                sheet.append([name, tit, email, tel])
    page += 1

wb.save("professor.xlsx")
driver.quit()

# sheet.append([name, tit, email, tel])
# wb.save("professor.xlsx")

# body > div > div > div > div > div.txt_bx > div > dl:nth-child(5) > dd > a
# body > div > div > div > div > div.txt_bx > div > dl:nth-child(7) > dd

# https://me.kaist.ac.kr/pop/team.html?uid=1&LANGUAGE_TYPE=kor
