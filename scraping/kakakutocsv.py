#scraper to csv file:

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def scraper(pageurl, writer):
    url = "https://kakaku.com/pc/note-pc/itemlist.aspx?pdf_vi=c" + pageurl
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    laptops = soup.findAll("div",{"class":"itemCatWrap"}) #extracting each product box
    try:
        for i in laptops:
            image = i.find("span",{"class":"itemCatImg"}).img.attrs['src']
            maker = i.find("span",{"class":"maker"}).get_text().strip()
            pname = i.find("span",{"class":"name2line"}).get_text().strip()
            price = i.find("span",{"class":"price"}).a.get_text().strip()
            price = price.replace("¥","")
            price = price.replace(",","")
            url = i.a.attrs['href']
            name = maker + " " + pname
            writer.writerow((image,name,int(price),url))  
        try:
            newurl = soup.findAll("li",{"class":"pageicon"})[1].a.attrs['href']
            print("---" + newurl)          
            scraper(newurl[34:], writer)
        except:
            return None
    finally:
        csvfile.close()

csvfile = open("kakaku_laptops.csv", "w")
writer = csv.writer(csvfile)
#writer.writerow(("Image","Name","Price","URL"))
scraper(" ",writer) 























