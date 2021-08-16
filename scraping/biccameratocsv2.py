
# DELETE FROM DATABASE WHERE NAME = "MacBookPro 15インチ MR942JA/A"

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def scraper(pageurl, writer):
    url = "https://www.biccamera.com/bc/category/001/100/009/025/?rowPerPage=100" + pageurl
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    laptops = soup.find("div",{"class":"bcs_listItem"}).findAll("li",{"data-item":"data-item"})
    #laptops = laptopsbox.findAll("li",{"data-item":"data-item"}) #extracting each product box
    try:
        for i in laptops:
            image = i.find("p",{"class":"bcs_image"}).img.attrs['src']
            maker = i.find("p",{"class":"bcs_maker"}).get_text().strip()
            pname = i.find("p",{"class":"bcs_title"}).get_text().strip()
            price = i.find("span",{"class":"val"}).get_text().strip()
            price = price.replace("¥","")
            price = price.replace("円","")
            price = price.replace(",","")
            url = i.find("p",{"class":"bcs_title"}).a['href']
            name = maker + " " + pname
            writer.writerow((image,name,int(price),url))  
        try:
            newurl = soup.findAll("li",{"class":"bcs_l"})[1].a.attrs['href']
            print("---" + newurl)          
            scraper(newurl[44:], writer)
        except:
            return None
    finally:
        csvfile.close()

csvfile = open("biccamera_laptops2.csv", "w")
writer = csv.writer(csvfile)
#writer.writerow(("Image","Name","Price","URL"))
scraper(" ",writer)