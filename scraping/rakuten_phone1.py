from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def price1(price):
    price_final=""
    for i in price:
        if(i.isdigit()):
            price_final+=i
    price_final1=int(price_final)
    return price_final1

def scraping(writer,s):
    print("Page number=",s)
    url = "https://search.rakuten.co.jp/search/mall/-/560202/?nitem=apple%20iphone&p="+str(s)+"&used=0"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    mobiles = soup.findAll("div", {"class": "dui-card searchresultitem"})
    for i in mobiles:
        maker = i.find("div", {"class": "content title"}).get_text().strip()
        if ("中古" in maker or "新品未使用" in maker or "新品未開封品" in maker):
            continue
        else:
            price = i.find("div", {"class": "content description price"}).span.get_text().strip()
            price_final1 = price1(price)
            url = i.a.attrs['href']
            image = i.img.attrs["src"]
            name = maker
            writer.writerow((image, name, price_final1, url))
    s += 1
    if s<=50:
        scraping(writer,s)
    else:
        csvfile.close()
        exit()

csvfile = open("rakuten_phone.csv", "w")
writer = csv.writer(csvfile)
scraping(writer,1)