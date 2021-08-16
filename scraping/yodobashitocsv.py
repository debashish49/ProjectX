#scraper to csv file:

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

def scraper(pageurl, writer):
    url = "https://www.yodobashi.com/category/19531/11970/34643/" + pageurl
    #req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    #html = urlopen(url)
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    html = urlopen(req, timeout=20).read()
    soup = BeautifulSoup(html,"html.parser")
    laptops = soup.findAll("div",{"data-arealimitsalesdisable":"false"}) #extracting each product box
    try:
        for i in laptops:
            image = i.img.attrs['src']
            maker = i.find("div",{"class":"pName fs14"}).p.get_text().strip()
            pname = i.img.attrs['alt']
            price = i.find("span",{"class":"productPrice"}).get_text().strip()
            price = price.replace(price[0],"")
            price = price.replace(",","")
            url = "https://www.yodobashi.com" + i.a.attrs['href']
            name = maker + " " + pname
            writer.writerow((image,name,int(price),url))  
        try:
            newurl = soup.find("a",{"class":"next"}).attrs['href']
            print("---" + newurl)          
            scraper(newurl[28:], writer)
        except:
            return None
    finally:
        csvfile.close()

csvfile = open("yodobashi_laptops.csv", "w")
writer = csv.writer(csvfile)
#writer.writerow(("Image","Name","Price","URL"))
scraper(" ",writer)