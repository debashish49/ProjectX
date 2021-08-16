import bs4
import urllib.request
from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as soup
import csv
import mysql.connector

def scrape(suffix, writer):
    page_url = "https://www.yodobashi.com/category/174101/174102/174114/p" + str(suffix) + "/?disptyp=02&searchtarget=prodname&sorttyp=COINCIDENCE_RANKING&word="
    page = page_url

    global i

    req = Request(page, headers={'User-Agent': 'XYZ/3.0'})
    webpage = urlopen(req, timeout=20).read()

    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("div", {"class": "srcResultItem_block pListBlock hznBox js_productBox js_smpClickable productListTile"})


    for container in containers:
        info = container.findAll("div", {"class":"pName fs14"})[0]
        title_pro=info.text


        price = container.findAll("span", {"class":"productPrice"})[0]
        price_pro = price.text
        price_pro = price_pro.replace(",", "")
        price_pro = price_pro.replace("￥", "")
        price_pro = int(price_pro)
        link=container.a
        link_pro = "https://www.yodobashi.com" + link["href"]

        img_link = container.findAll("div", {"class": "pImg mb15 js_addLatestSalesOrder"})[0].img
        img_pro = img_link["src"]

        writer.writerow((img_pro, title_pro,price_pro,link_pro))  

    i+=1

    if i > 3:
        csvfile.close()
        
    else:
        suffix_pro = str(i)
        print(str(i) + "------" + str(suffix_pro))
        scrape(suffix_pro, writer)
    
csvfile = open("Yodobashi_Phones.csv", "w", encoding = "utf-8", newline='')
writer = csv.writer(csvfile)
#writer.writerow(("Name","Price","URL", "ImgURL"))
i=1
scrape(i, writer)

#connecting to database
mycon=mysql.connector.connect(host="localhost", user='root', passwd='@grade12', database='products')
cursor = mycon.cursor()

cursor.execute("DROP TABLE IF EXISTS yodobashiphones")
mycon.commit()

cursor.execute("CREATE TABLE yodobashiphones(image varchar(1000), name varchar(1000), price int(10), url varchar(1000))")
mycon.commit()

cursor.execute("ALTER DATABASE products CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
mycon.commit()

with open("Yodobashi_Phones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO yodobashiphones(image,name,price,url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        mycon.commit()


