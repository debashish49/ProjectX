
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

def scraper(suffix, writer):
    global s
    url = "https://www.yamada-denkiweb.com/category/207/001/005/?path=0007-%E3%83%91%E3%82%BD%E3%82%B3%E3%83%B3%E3%83%BB%E5%91%A8%E8%BE%BA%E6%A9%9F%E5%99%A8%E3%83%BBPC%E3%82%BD%E3%83%95%E3%83%88%3A0001-%E3%83%91%E3%82%BD%E3%82%B3%E3%83%B3%E3%83%BB%E3%82%BF%E3%83%96%E3%83%AC%E3%83%83%E3%83%88PC%3A0005-207001005_Apple%E3%83%8E%E3%83%BC%E3%83%88&o=" + str(suffix)
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    html = urlopen(req, timeout=120).read()
    soup = BeautifulSoup(html,"html.parser")
    laptops = soup.findAll("div",{"class":"item-wrapper"}) #extracting each product box

    for i in laptops:
        image = i.img.attrs['data-src']
        name = i.find("p",{"class":"item-name"}).a.get_text().strip()
        price = i.find("span",{"class":"highlight large"}).get_text().strip()
        price = price.replace("¥","")
        price = price.replace("円","")
        price = price.replace(",","")
        url = "https://www.yamada-denkiweb.com" + i.find("p",{"class":"item-name"}).a.attrs['href']
        writer.writerow((image,name,int(price),url))  
    s += 20
    if s <= 40:
        newsuffix = s
        print("---" + str(newsuffix))          
        scraper(newsuffix, writer)
    else:
        csvfile.close()

csvfile = open("yamadadenki_laptops2.csv", "w")
writer = csv.writer(csvfile)
#writer.writerow(("Image","Name","Price","URL"))
s = 0
scraper(s,writer)