from bs4 import BeautifulSoup
from selenium import webdriver
# bs가 막힐경우 webdriver를 사용

class NaverMovie:
    def __init__(self, url):
        driver = webdriver.Chrome(executable_path='C:/Users/ezen/PycharmProjects/tensorflow190803/webcrawl/data/chromedriver')
        driver.get(url)
        self.soup = BeautifulSoup(driver.page_source, 'html.paraser')

    def scrap(self):
        html = self.soup.prettify()
        print(html)

