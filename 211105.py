from urllib.request import urlopen
from bs4 import BeautifulSoup
from openpyxl import workbook
from openpyxl.workbook import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('복지뉴스')


html = urlopen("https://search.naver.com/search.naver?query=%EB%B3%B5%EC%A7%80&where=news&ie=utf8&sm=nws_hty/")
bsOdject = BeautifulSoup(html, "html.parser")

for link in bsOdject.find_all('a.news_wrap'):
    print(link.text.strip(), link.get('href'))