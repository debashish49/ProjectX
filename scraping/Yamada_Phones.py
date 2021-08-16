import bs4
import urllib.request
from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as soup
import csv
import mysql.connector

def scrape(suffix, writer):
    page_url = "https://www.yamada-denkiweb.com/category/209/001/001/" + str(suffix)
    page = page_url

    global i

    req = Request(page, headers={'User-Agent': 'XYZ/3.0'})
    webpage = urlopen(req, timeout=20).read()

    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("div", {"class": "item-wrapper"})


    for container in containers:
        info = container.findAll("p", {"class":"item-name"})[0]
        title_pro=info.a.text

        try:
            price = container.findAll("span", {"class":"highlight large"})[0]
            price_pro = price.text
            price_pro = price_pro.replace(",", "")
            price_pro = price_pro.replace("¥", "")
            price_pro = int(price_pro)

        except:
            price_pro = "N/A"

        link=container.findAll("p", {"class":"item-name"})[0]
        link_pro = "https://www.yamada-denkiweb.com/" + link.a["href"]

        img_link = container.findAll("div", {"class": "item-thumbnail"})[0].a.img
        img_pro = img_link["data-src"]

        writer.writerow((img_pro, title_pro,price_pro,link_pro))  
        
    i+=20

    if i > 120:
        csvfile.close()
        
    else:
        suffix_pro = "?path=0009-%E6%90%BA%E5%B8%AF%E9%9B%BB%E8%A9%B1%E3%83%BB%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%95%E3%82%A9%E3%83%B3%3A0001-%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%95%E3%82%A9%E3%83%B3%3A0001-209001001_SIM%E3%83%95%E3%83%AA%E3%83%BC%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%95%E3%82%A9%E3%83%B3&amp;o=" + str(i)
        print(str(i) + "------" + str(suffix_pro))
        scrape(suffix_pro, writer)
    
csvfile = open("Yamada_Phones.csv", "w", encoding = "utf-8", newline='')
writer = csv.writer(csvfile)
#writer.writerow(("Name","Price","URL", "ImgURL"))
i=0
scrape(" ", writer)

#connecting to database
mycon=mysql.connector.connect(host="localhost", user='root', passwd='@grade12', database='products')
cursor = mycon.cursor()

cursor.execute("DROP TABLE IF EXISTS yamadadenkiphones")
mycon.commit()

cursor.execute("CREATE TABLE yamadadenkiphones(image varchar(1000), name varchar(1000), price int(10), url varchar(1000))")
mycon.commit()

cursor.execute("ALTER DATABASE products CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
mycon.commit()

with open("Yamada_Phones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO yamadadenkiphones(image,name,price,url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        mycon.commit()


