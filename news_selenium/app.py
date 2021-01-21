import requests
from flask import Flask
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver_dir = './static/bin/chromedriver'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/wfootball/index.nhn', headers=headers)


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')

# driver = webdriver.Chrome(chrome_driver_dir)  # Optional argument, if not specified will search path.
# driver.get('https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N');

# html = driver.page_source
soup = BeautifulSoup(data.text, 'html.parser')

articles = soup.select('#content > div > div.home_feature > div.feature_side > div > ol >li ')
for article in articles:
    title = article.select_one('a').text
    print(title)



# content > div > div.home_feature > div.feature_side > div > ol > li:nth-child(1) > a
# content > div > div.home_feature > div.feature_side > div > ol > li:nth-child(2) > a
