import requests
from bs4 import BeautifulSoup
import pandas
import math


# Parameters
taipei_city=0
new_taipei_city=2

target_city = new_taipei_city

shilin_district=111
luchou_distrcit=247

target_district = luchou_distrcit

sort_descend_by_update_time = '21'
sort_ascend_by_update_time = '20'
sort_by_default = '11'

price_range_1000_1500 = '1000%7E1500'
price_range_1500_2000 = '1500%7E2000'
target_price_range = price_range_1000_1500

item_per_page = 19

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
# Parameters

rakuya_request_url = f'https://www.rakuya.com.tw/sell/result?city={target_city}&zipcode={target_district}&usecode=1&sort={sort_by_default}&price={target_price_range}&page='

print(f'Looing for city: {target_city} district: {target_district}, price_range: {target_price_range} ...')

request = requests.get(url=rakuya_request_url, headers=headers)
soup = BeautifulSoup(markup=request.content,features="html.parser")

total_items = soup.find(name='span', attrs={"class": "numb setSearchTotal"}).text
print("Total found item: %s" % total_items)

page_limit = math.ceil(int(total_items)/item_per_page)+1
print("Page limit: %s" % page_limit)
print('\n')

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

list = []

for page in range(1, page_limit):
    target_url = f'{rakuya_request_url}{page}'
    print("Working on %s" % target_url)

    request = requests.get(url=target_url, headers=headers)
    soup = BeautifulSoup(markup=request.content,features="html.parser")

    all_listing = soup.find_all(name="section",attrs={"class":"grid-item search-obj"})

    for idx, item in enumerate(all_listing):
        dict = {}
        right_side = item.find(name='div',attrs={"class":"grid-column rightside"})
        dict['title'] = right_side.find(name="div", attrs={"class":"h2 title-2"}).text
        dict['address'] = right_side.find(name="h2", attrs={"class":"address"}).text.replace('\n','').replace(' ','')
        dict['price(w)'] = right_side.find(name='span',attrs={"class":"text__price"}).text.replace('萬','')
        dict['unit_price'] = right_side.find(name='span',attrs={"class":"unit__price"}).text
        
        info = right_side.find(name='ul',attrs={"class":"list__info"}).text.split()
        dict['purpose'] = info[0]
        dict['area(ping))'] = info[1].replace('坪','')
        dict['age'] = info[2]
        dict['floor'] = info[3]
        
        # dict['info'] = right_side.find(name='ul',attrs={"class":"list__info"}).text.replace('\n','').replace(' ','')
        dict['url'] = item.find('a').get('href')
        list.append(dict)
        # print("%s: %s \n%s/%s, \n%s, %s" % (idx, title, price, unit_price, address, info))
        # print("\n")

    
print("Total items %s", len(list))



df = pandas.DataFrame(list)
df.to_csv(f'{target_city}_{target_district}_{target_price_range}.csv')