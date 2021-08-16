import bs4
import urllib.request
from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as soup
import csv
import mysql.connector

def scrape(writer):
    page_url = "https://www.biccamera.com/bc/category/001/240/240/?entr_nm=%83%41%83%62%83%76%83%8B%81%40Apple&q=iPhone&type=03&rowPerPage=100"
    page = page_url

    req = Request(page, headers={'User-Agent': 'XYZ/3.0'})
    webpage = urlopen(req, timeout=20).read()

    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("li", {"data-item": "data-item"})


    for container in containers:

        brand = container.findAll("p", {"class":"bcs_maker"})[0]
        brand_pro = brand.text

        info = container.findAll("p", {"class":"bcs_title"})[0]
        title_pro=info.a.text

        name_pro = brand_pro + title_pro

        #because some items are second-hand

        try:
            price = container.findAll("p", {"class":"bcs_price"})[0]
            price_pro = price.span.text
            price_pro = price_pro.replace(",", "")
            price_pro = price_pro.replace("円", "")
            price_pro = int(price_pro)

            link=container.findAll("p", {"class":"bcs_title"})[0]
            link_pro = link.a["href"]

            img_link = container.findAll("p", {"class": "bcs_image"})[0].a.img
            img_pro = img_link["src"]
            writer.writerow((img_pro, name_pro,price_pro,link_pro))  

        except:
            pass
    
csvfile = open("BiciPhones.csv", "w", encoding = "utf-8", newline='')
writer = csv.writer(csvfile)
#writer.writerow(("Name","Price","URL", "ImgURL"))
scrape(writer)

csvfile.close()

mycon=mysql.connector.connect(host="localhost", user='root', passwd='@grade12', database='products')
cursor = mycon.cursor()

cursor.execute("DROP TABLE IF EXISTS biccameraphones")
mycon.commit()

cursor.execute("CREATE TABLE biccameraphones(image varchar(1000), name varchar(1000), price int(20), url varchar(1000))")
mycon.commit()

cursor.execute("ALTER DATABASE products CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
mycon.commit()

with open("BiciPhones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO biccameraphones(image, name, price, url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        mycon.commit()




