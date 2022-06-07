import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv


file = open('products.csv', 'w',encoding='utf-8', newline='\n')
pro_file = csv.writer(file)
pro_file.writerow(['image','category', 'price'])

page = 1
while page < 6:
    res = requests.get(f'https://www.ecrater.com/c/66/computers-networking?&srn={page}')
    beautifulsoup = BeautifulSoup(res.text,"html.parser")
    items = beautifulsoup.find('ul',id="product-list-grid")
    all = items.find_all('li', class_= 'product-item')
    for i in all:
        price = i.div.span.text
        product_image = i.a.img.get('src')
        describtion = i.a.img.get('title')
        product_category = i.find('a', class_= 'product-category').text
        pro_file.writerow([product_image,product_category,price,describtion])

    sleep(randint(15,20))
    page+=1

file.close()