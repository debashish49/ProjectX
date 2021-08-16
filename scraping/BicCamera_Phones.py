import bs4
import urllib.request
from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as soup
import csv
import mysql.connector

def scrape(suffix, writer):
    page_url = "https://www.biccamera.com/bc/category/001/240/020/?sold_out_tp2=1&rowPerPage=100&p=" + str(suffix)
    page = page_url

    global i

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

    i+=1

    if i > 2:
        csvfile.close()
        
    else:
        suffix_pro = str(i)
        print(str(i) + "------" + str(suffix_pro))
        scrape(suffix_pro, writer)
    
csvfile = open("BicCamera_Phones.csv", "w", encoding = "utf-8", newline='')
writer = csv.writer(csvfile)
#writer.writerow(("Name","Price","URL", "ImgURL"))
i=1
scrape(i, writer)

#connecting to database
mycon=mysql.connector.connect(host="localhost", user='root', passwd='@grade12', database='products')
cursor = mycon.cursor()

cursor.execute("ALTER DATABASE products CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
mycon.commit()

with open("BicCamera_Phones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO biccameraphones(image,name,price,url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        mycon.commit()


