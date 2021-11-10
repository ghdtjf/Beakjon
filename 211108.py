import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?query=%EB%B3%B5%EC%A7%80&where=news&ie=utf8&sm=nws_hty/"
# 위에 url로 페이지 요청
res = requests.get(url)

# HTML 분석기
bsOdject = BeautifulSoup(res.content, "lxml")
bsOdject = bsOdject.find("ul", { "class": "list_news" })

result_list = list()

for link in bsOdject.find_all('li',{ "class": "bx" }):
    _link = link.find("a", {"class":"news_tit"})
    result_list.append([_link.get('title'), _link.get("href")])


print(result_list)

# from openpyxl import Workbook

# wb = Workbook()
# sheet = wb.active

# row_idx = 1

# for item in result_list:
#     title_cell = sheet.cell(row=row_idx, column=1)
#     link_cell = sheet.cell(row=row_idx, column=2)
#     title_cell.value = item[0]
#     link_cell.value = item[1]
#     row_idx += 1

wb.save("복지뉴스.xlsx")