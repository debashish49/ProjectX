import bs4
import urllib.request
from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as soup
import csv
import mysql.connector

def scrape(writer):

    print("Data: iPhone SE 2nd Gen")

    page_url = "https://www.yodobashi.com/category/174101/174102/174103/?disptyp=02&searchtarget=prodname&sorttyp=COINCIDENCE_RANKING&word=iphonese2ndsimfree"
    page = page_url

    req = Request(page, headers={'User-Agent': 'XYZ/3.0'})
    webpage = urlopen(req, timeout=20).read()

    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("div", {"class": "srcResultItem_block pListBlock hznBox js_productBox js_smpClickable productListTile"})

    for container in containers:

        info = container.findAll("div", {"class":"pName fs14"})[0]
        name_pro=info.text

        #because some items are second-hand

        price = container.findAll("span", {"class":"productPrice"})[0]
        price_pro = price.text
        price_pro = price_pro.replace(",", "")
        price_pro = price_pro.replace("円", "")
        price_pro = price_pro.replace("￥", "")
        price_pro = int(price_pro)

        link=container.findAll("a", {"class":"js_productListPostTag js-clicklog js-taglog-schRlt js_smpClickableFor cImg js-clicklog-check"})[0]
        link_pro = "https://www.yodobashi.com" + link["href"]

        img_link = container.findAll("div", {"class": "pImg mb15"})[0].img
        img_pro = img_link["src"]

        writer.writerow((img_pro, name_pro,price_pro,link_pro))  


    print("Data: iPhone 11 Pro and Pro Max")

    page_url = "https://www.yodobashi.com/category/174101/174102/174103/?word=iphone11simfreemodel"
    page = page_url

    req = Request(page, headers={'User-Agent': 'XYZ/3.0'})
    webpage = urlopen(req, timeout=20).read()

    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("div", {"class": "srcResultItem_block pListBlock hznBox js_productBox js_smpClickable productListTile"})


    for container in containers:

        info = container.findAll("div", {"class":"pName fs14"})[0]
        name_pro=info.text

        #because some items are second-hand

        price = container.findAll("span", {"class":"productPrice"})[0]
        price_pro = price.text
        price_pro = price_pro.replace(",", "")
        price_pro = price_pro.replace("円", "")
        price_pro = price_pro.replace("￥", "")
        price_pro = int(price_pro)

        link=container.findAll("a", {"class":"js_productListPostTag js-clicklog js-taglog-schRlt js_smpClickableFor"})[0]
        link_pro = "https://www.yodobashi.com" + link["href"]

        img_link = container.findAll("div", {"class": "pImg mb15"})[0].img
        img_pro = img_link["src"]

        writer.writerow((img_pro, name_pro,price_pro,link_pro))  

    print("Data: iPhone 11")

    page_url = "https://www.yodobashi.com/category/174101/174102/174103/?word=iphone11simfree"
    page = page_url

    req = Request(page, headers={'User-Agent': 'XYZ/3.0'})
    webpage = urlopen(req, timeout=20).read()

    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("div", {"class": "srcResultItem_block pListBlock hznBox js_productBox js_smpClickable productListTile"})


    for container in containers:

        info = container.findAll("div", {"class":"pName fs14"})[0]
        name_pro=info.text

        #because some items are second-hand

        price = container.findAll("span", {"class":"productPrice"})[0]
        price_pro = price.text
        price_pro = price_pro.replace(",", "")
        price_pro = price_pro.replace("円", "")
        price_pro = price_pro.replace("￥", "")
        price_pro = int(price_pro)

        link=container.findAll("a", {"class":"js_productListPostTag js-clicklog js-taglog-schRlt js_smpClickableFor"})[0]
        link_pro = "https://www.yodobashi.com" + link["href"]

        img_link = container.findAll("div", {"class": "pImg mb15"})[0].img
        img_pro = img_link["src"]

        writer.writerow((img_pro, name_pro,price_pro,link_pro))  

    print("Data: iPhone XS ans XS Max")

    page_url = "https://www.yodobashi.com/category/174101/174102/174103/?word=iphonexssimfree"
    page = page_url

    req = Request(page, headers={'User-Agent': 'XYZ/3.0'})
    webpage = urlopen(req, timeout=20).read()

    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("div", {"class": "srcResultItem_block pListBlock hznBox js_productBox js_smpClickable productListTile"})


    for container in containers:

        info = container.findAll("div", {"class":"pName fs14"})[0]
        name_pro=info.text

        #because some items are second-hand

        price = container.findAll("span", {"class":"productPrice"})[0]
        price_pro = price.text
        price_pro = price_pro.replace(",", "")
        price_pro = price_pro.replace("円", "")
        price_pro = price_pro.replace("￥", "")
        price_pro = int(price_pro)

        link=container.findAll("a", {"class":"js_productListPostTag js-clicklog js-taglog-schRlt js_smpClickableFor"})[0]
        link_pro = "https://www.yodobashi.com" + link["href"]

        img_link = container.findAll("div", {"class": "pImg mb15"})[0].img
        img_pro = img_link["src"]

        writer.writerow((img_pro, name_pro,price_pro,link_pro))  
    
csvfile = open("yodobashiiPhones.csv", "w", encoding = "utf-8", newline='')
writer = csv.writer(csvfile)
#writer.writerow(("Name","Price","URL", "ImgURL"))
scrape(writer)

csvfile.close()

mycon=mysql.connector.connect(host="localhost", user='root', passwd='@grade12', database='deletedb')
cursor = mycon.cursor()

cursor.execute("DROP TABLE IF EXISTS yodobashiphones")
mycon.commit()

cursor.execute("CREATE TABLE yodobashiphones(image varchar(1000), name varchar(1000), price int(10), url varchar(1000))")
mycon.commit()

cursor.execute("ALTER DATABASE deletedb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
mycon.commit()

with open("yodobashiiPhones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO yodobashiphones(image, name, price, url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        mycon.commit()