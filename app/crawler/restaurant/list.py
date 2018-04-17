import os

import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://www.foodfly.co.kr/restaurants?sortby=fee&category_korean=on'

if not os.path.exists('list.html'):
    client = webdriver.Chrome('/usr/local/bin/chromedriver')
    client.get(url)
    height = 0
    while True:
        client.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
        body = client.find_element_by_css_selector('body')
        cur_height = body.size['height']
        if cur_height > height:
            height = cur_height
        else:
            break

    source = client.page_source
    open('list.html', 'wt').write(source)
    client.quit()

soup = BeautifulSoup(open('list.html').read(), 'lxml')
a_list = soup.select('.restaurant-list > a')
for a in a_list:
    pk = re.match(r'^.*/(?P<pk>\d+)', a.get('href', '')).group('pk').strip()
    bg = a.select_one('.restaurant_box span.restaurant_box_bg').get_text(strip=True)
    bg_hover = a.select_one('.restaurant_box span.restaurant_box_bg_hover').get_text(strip=True)
    p = re.compile(r'^url\((?P<url>.*?)\)')
    bg_url = p.match(bg).group('url')
    bg_hover_url = p.match(bg_hover).group('url')

    name = a.select_one('.restaurant_info .restaurant_name').get_text(strip=True)
    print(pk)
    print(name)
    print(bg_url)
    print(bg_hover_url)
    print('')


# if not os.path.exists('detail.html'):
#     response = requests.get(url)
#     open('detail.html', 'wt').write(response.text)
#
# soup = BeautifulSoup(open('detail.html').read(), 'lxml')