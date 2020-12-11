import requests
from bs4 import BeautifulSoup
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
django.setup()

from api.models import Item

__headers__ = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
COUNT = "1"

def parse_items():
    res = requests.get(
        'https://search.musinsa.com/category/001005?d_cat_cd=001005&page_kind=search&list_kind=small&sort=pop&page=1&display_cnt='+COUNT,
        headers=__headers__).text
    bs = BeautifulSoup(res, "html.parser")

    # print(bs.prettify())

    all_item = bs.find('div', class_="list-box box")
    item_list = all_item.find_all('li', class_="li_box")
    return item_list


def parse_item_info(item):
    brand = item.find('p', class_="item_title").get_text()
    a = item.find('a', {"name": "goods_link"})  # link 와 title 이 있는 a 태그
    link = a.get('href')
    title = a.get('title')
    img_link = item.find('img', class_="lazyload lazy").get('data-original')
    price = item.find('p', class_="price").get_text().strip()

    detail_res = requests.get(link, headers=__headers__).text
    detail_info = BeautifulSoup(detail_res, "html.parser")

    size_info = detail_info.find('table', class_="table_th_grey").find('tbody').find_all('tr')[2:]
    size_list = []
    for s in size_info:
        size = s.find('th').get_text()
        size_list.append(size)

    item_info = {
        'img_link': img_link,
        'brand': brand,
        'link': link,
        'title': title,
        'price': price,
        'size_list': size_list
    }
    return item_info


if __name__ == '__main__':
    item_list = parse_items()
    for item in item_list:
        data = parse_item_info(item)
        queryset = Item.objects.create(img_link=data['img_link'], brand=data['brand'], link=data['link'], title=data['title'], price=data['price'], size_list=data['size_list'])
        queryset.save()
