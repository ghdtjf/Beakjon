import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from openpyxl import Workbook

keyword = "자원봉사센터"

result_list = list()
wb = Workbook()
sheet = wb.active
sheet.title = keyword

sheet.append(['기관명', '주소',  '전화번호', '팩스번호', '홈페이지주소'])
for page in tqdm(range(1, 13 + 1)):
    url = 'http://www.kfvc.or.kr/contents/sub04/sub04_02.html?a_gb=app&a_cd=4&a_item=0&tm=1&view_cd=d&page={}&code=&po_area='.format(page)
    res = requests.get(url)

    bsOdject = BeautifulSoup(res.content, 'lxml')
    bsOdject = bsOdject.find("div", {"class" : "wrap_brdList"}).find("tbody")

    for item in bsOdject.find_all("tr"):
        상세보기 = "http://www.kfvc.or.kr" + item.find("a", {"class" : "detail_btn"}).get("href")
        res = requests.get(상세보기)
        bsOdject = BeautifulSoup(res.content, 'lxml')
        bsOdject = bsOdject.find("div", {"class" : "wrap_brdList"}).find("tbody")
        sub_item = bsOdject.find_all("tr")
        기관명 = sub_item[0].find("td").text.strip() + " 자원봉사센터"
        주소 = sub_item[1].find("td").text.strip()
        전화번호 = sub_item[3].find_all("td")[0].text.strip().replace(")", "-")
        팩스번호 = sub_item[3].find_all("td")[1].text.strip().replace(")", "-")
        홈페이지주소 = sub_item[4].find("a", {"target" : "_blank"}).get("href")
        result_list.append([기관명, 주소,  전화번호, 팩스번호, 홈페이지주소])

for item in result_list:
    sheet.append(item)

wb.save("{}.xlsx".format(keyword))