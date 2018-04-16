import os
import requests
from bs4 import BeautifulSoup

url = 'http://www.foodfly.co.kr/restaurants/show/20870'
if not os.path.exists('detail.html'):
    response = requests.get(url)
    open('detail.html', 'wt').write(response.text)

soup = BeautifulSoup(open('detail.html').read(), 'lxml')
top_box = soup.select_one('#restaurant-show > .top-box')
left_section = top_box.select_one('.left-section')
right_section = top_box.select_one('.right-section')

restaurant_name = left_section.select_one('.main-info > h1').get_text(strip=True)
restaurant_thumbnail = left_section.select_one('.main-info img.restaurant-thumbnail').get('src')
sub_info = left_section.select_one('.main-info .main-info-sub')
sub_info_dict = {
    p.select('span')[0].get_text(strip=True): p.select('span')[1].get_text(strip=True)[2:]
    for p in sub_info.select('p')
}

restaurant_info = soup.select_one('#restaurant-show > .restaurant-info')
# print(restaurant_info.get_text())
info_p_list = [p.get_text(strip=True) for p in restaurant_info.select('p') if p.get_text(strip=True)]

for p in info_p_list:
    print(p)

restaurant_origin = soup.select('#restaurant-show > .bordered')[1]
origin = restaurant_origin.select_one('p').get_text()
print(origin)

menu_container = soup.select_one('#restaurant-show > .show-menu > .left-section')
category_list = []
category_list_soup = menu_container.select('.menu-category')
for category in category_list_soup:
    category_name = category.select_one('.row-category').get_text(strip=True)
    category_dict = {
        'name': category_name,
        'menus': []
    }
    menu_list_soup = category.select('.row-menu')
    for menu in menu_list_soup:
        menu_name = menu.select_one('.col-menu > strong').get_text(strip=True)
        menu_desc = menu.select_one('.col-menu > span').get_text(strip=True)
        menu_photo_soup = menu.select_one('.col-photo > img')
        menu_photo = menu_photo_soup.get('src') if menu_photo_soup else ''
        menu_price = menu.select_one('.col-price > .price').get_text(strip=True)
        menu_dict = {
            'name': menu_name,
            'desc': menu_desc,
            'photo': menu_photo,
            'price': menu_price,
        }
        category_dict['menus'].append(menu_dict)
    category_list.append(category_dict)

print(category_list)