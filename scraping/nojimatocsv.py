
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

def scraper(suffix, writer):
    global s
    url = "https://online.nojima.co.jp/category/10001920/?searchCategoryCode=10001920&mode=image&pageSize=60&currentPage=" + str(suffix)
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    html = urlopen(req, timeout=120).read()
    soup = BeautifulSoup(html,"html.parser")
    laptops = soup.findAll("div",{"class":"shouhinlist"}) #extracting each product box

    for i in laptops:
        image = "https://online.nojima.co.jp" + i.img.attrs['src']
        maker = i.findAll("span")[0].get_text().strip()
        pname = i.findAll("span")[1].get_text().strip()
        price = i.find("span",{"class":"price"}).get_text().strip()
        price = price.replace("¥","")
        price = price.replace("円","")
        price = price.replace(",","")
        url = "https://online.nojima.co.jp" + i.a.attrs['href']
        name = maker + " " + pname
        writer.writerow((image,name,int(price),url))  
    s += 1
    if s <= 27:
        newsuffix = s
        print("---" + str(newsuffix))          
        scraper(newsuffix, writer)
    else:
        csvfile.close()

csvfile = open("nojima_laptops.csv", "w")
writer = csv.writer(csvfile)
#writer.writerow(("Image","Name","Price","URL"))
s = 1
scraper(s,writer)





"""
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

def scraper(pageurl, writer):
    url = "https://www.yamada-denkiweb.com/category/207/001/001/" + pageurl
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
    html = urlopen(req, timeout=20).read()
    soup = BeautifulSoup(html,"html.parser")
    laptops = soup.findAll("div",{"class":"item-wrapper "}) #extracting each product box
    try:
        for i in laptops:
            image = i.img.attrs['data-src']
            name = i.find("p",{"class":"item-name"}).a.get_text().strip()
            price = i.find("span",{"class":"highlight large"}).get_text().strip()
            url = i.find("p",{"class":"item-name"}).a.attrs['href']
            writer.writerow((image,name,price,url))  
        try:
            newurl = soup.findAll("div",{"class":"pagination pagination-right"})[1].findAll("li")[-1].a.attrs['href']
            if newurl == "javascript: void(0);":
                csvfile.close()
            else:
                print("---" + newurl)          
                scraper(newurl, writer)
        except:
            return None
    finally:
        csvfile.close()

csvfile = open("yamadadenki_laptops.csv", "w")
writer = csv.writer(csvfile)
writer.writerow(("Image","Name","Price","URL"))
scraper(" ",writer)

"""