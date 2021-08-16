
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

def scraper(suffix, writer):
    global s
    url = "https://online.nojima.co.jp/category/20000006/?searchCategoryCode=20000006&mode=image&pageSize=60&currentPage=" + str(suffix)
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
    if s <= 3:
        newsuffix = s
        print("---" + str(newsuffix))          
        scraper(newsuffix, writer)
    else:
        csvfile.close()

csvfile = open("nojima_laptops2.csv", "w")
writer = csv.writer(csvfile)
#writer.writerow(("Image","Name","Price","URL"))
s = 1
scraper(s,writer)