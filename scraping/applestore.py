
#image, name, price, url
#applestore

import csv
import mysql.connector


phones = open("AppleiPhones.csv", "w", encoding = "utf-8", newline='')
writer = csv.writer(phones)

#header
#writer.writerow(("image","name","price", "url"))

#records

#iPhone 11 Pro 64 GB

name = "iPhone 11 Pro 64 GB Midnight Green"
price = 106800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-midnight-green-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954990073"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 64 GB Space Gray"
price = 106800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-space-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954989577"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 64 GB Silver"
price = 106800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-silver-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954989256"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 64 GB Gold"
price = 106800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-gold-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954990120"

writer.writerow((img, name, price, url))

#iPhone 11 Pro 256 GB

name = "iPhone 11 Pro 256 GB Midnight Green"
price = 122800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-midnight-green-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954990073"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 256 GB Space Gray"
price = 122800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-space-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954989577"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 256 GB Silver"
price = 122800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-silver-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954989256"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 256 GB Gold"
price = 122800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-gold-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954990120"

writer.writerow((img, name, price, url))

#iPhone 11 Pro 512 GB

name = "iPhone 11 Pro 512 GB Midnight Green"
price = 144800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-midnight-green-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954990073"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 512 GB Space Gray"
price = 144800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-space-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954989577"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 512 GB Silver"
price = 144800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-silver-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954989512"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro 512 GB Gold"
price = 144800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-gold-select-2019?wid=470&amp;hei=556&amp;fmt=png-alpha&amp;.v=1566954990120"

writer.writerow((img, name, price, url))

#iPhone 11 Pro Max 64 GB

name = "iPhone 11 Pro Max 64 GB Midnight Green"
price = 119800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-midnight-green-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953859350"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 64 GB Space Gray"
price = 119800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-space-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953858806"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 64 GB Silver"
price = 119800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-silver-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953858420"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 64 GB Gold"
price = 119800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-gold-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953859132"

writer.writerow((img, name, price, url))

#iPhone 11 Pro Max 256 GB

name = "iPhone 11 Pro Max 256 GB Midnight Green"
price = 135800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-midnight-green-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953859350"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 256 GB Space Gray"
price = 135800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-space-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953858806"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 256 GB Silver"
price = 135800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-silver-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953858420"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 256 GB Gold"
price = 135800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-gold-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953859132"

writer.writerow((img, name, price, url))

#iPhone 11 Pro Max 512 GB

name = "iPhone 11 Pro Max 512 GB Midnight Green"
price = 157800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-midnight-green-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953859350"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 512 GB Space Gray"
price = 157800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-space-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953858806"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 512 GB Silver"
price = 157800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-silver-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953858420"

writer.writerow((img, name, price, url))

name = "iPhone 11 Pro Max 512 GB Gold"
price = 157800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11-pro"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-11-pro-max-gold-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566953859132"

writer.writerow((img, name, price, url))

#iPhone 11 64 GB

name = "iPhone 11 64 GB White"
price = 74800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-white-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956148115"

writer.writerow((img, name, price, url))

name = "iPhone 11 64 GB Black"
price = 74800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-black-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144418"

writer.writerow((img, name, price, url))

name = "iPhone 11 64 GB Green"
price = 74800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-green-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144838"

writer.writerow((img, name, price, url))

name = "iPhone 11 64 GB Yellow"
price = 74800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-yellow-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1568141245782"

writer.writerow((img, name, price, url))

name = "iPhone 11 64 GB Purple"
price = 74800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-purple-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566960958082"

writer.writerow((img, name, price, url))

name = "iPhone 11 64 GB PRODUCT(Red)"
price = 74800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-red-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144763"

writer.writerow((img, name, price, url))

#iPhone 11 128 GB

name = "iPhone 11 128 GB White"
price = 79800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-white-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956148115"

writer.writerow((img, name, price, url))

name = "iPhone 11 128 GB Black"
price = 79800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-black-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144418"

writer.writerow((img, name, price, url))

name = "iPhone 11 128 GB Green"
price = 79800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-green-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144838"

writer.writerow((img, name, price, url))

name = "iPhone 11 128 GB Yellow"
price = 79800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-yellow-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1568141245782"

writer.writerow((img, name, price, url))

name = "iPhone 11 128 GB Purple"
price = 79800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-purple-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566960958082"

writer.writerow((img, name, price, url))

name = "iPhone 11 128 GB PRODUCT(Red)"
price = 79800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-red-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144763"

writer.writerow((img, name, price, url))

#iPhone 11 256 GB

name = "iPhone 11 256 GB White"
price = 90800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-white-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956148115"

writer.writerow((img, name, price, url))

name = "iPhone 11 256 GB Black"
price = 90800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-black-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144418"

writer.writerow((img, name, price, url))

name = "iPhone 11 256 GB Green"
price = 90800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-green-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144838"

writer.writerow((img, name, price, url))

name = "iPhone 11 256 GB Yellow"
price = 90800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-yellow-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1568141245782"

writer.writerow((img, name, price, url))

name = "iPhone 11 256 GB Purple"
price = 90800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-purple-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566960958082"

writer.writerow((img, name, price, url))

name = "iPhone 11 256 GB PRODUCT(Red)"
price = 90800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-11"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone11-red-select-2019?wid=470&hei=556&fmt=png-alpha&.v=1566956144763"

writer.writerow((img, name, price, url))

#iPhone SE (2nd Generation) 64 GB

name = "iPhone SE (2nd Generation) 64 GB White"
price = 44800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-white-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574259457"

writer.writerow((img, name, price, url))

name = "iPhone SE (2nd Generation) 64 GB Black"
price = 44800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-black-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574260051"

writer.writerow((img, name, price, url))

name = "iPhone SE (2nd Generation) 64 GB PRODUCT(Red)"
price = 44800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-red-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574260319"

writer.writerow((img, name, price, url))

#iPhone SE (2nd Generation) 128 GB

name = "iPhone SE (2nd Generation) 128 GB White"
price = 49800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-white-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574259457"

writer.writerow((img, name, price, url))

name = "iPhone SE (2nd Generation) 128 GB Black"
price = 49800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-black-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574260051"

writer.writerow((img, name, price, url))

name = "iPhone SE (2nd Generation) 128 GB PRODUCT(Red)"
price = 49800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-red-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574260319"

writer.writerow((img, name, price, url))

#iPhone SE (2nd Generation) 256 GB

name = "iPhone SE (2nd Generation) 256 GB White"
price = 60800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-white-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574259457"

writer.writerow((img, name, price, url))

name = "iPhone SE (2nd Generation) 256 GB Black"
price = 60800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-black-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574260051"

writer.writerow((img, name, price, url))

name = "iPhone SE (2nd Generation) 256 GB PRODUCT(Red)"
price = 60800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-se"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-se-red-select-2020?wid=470&hei=556&fmt=png-alpha&.v=1586574260319"

writer.writerow((img, name, price, url))

#iPhone XR 64 GB

name = "iPhone XR 64 GB"
price = 64800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-xr"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-xr-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1550795424612"

writer.writerow((img, name, price, url))

#iPhone XR 128 GB

name = "iPhone XR 128 GB"
price = 69800
url = "https://www.apple.com/jp/shop/buy-iphone/iphone-xr"
img = "https://store.storeimages.cdn-apple.com/8567/as-images.apple.com/is/iphone-xr-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1550795424612"

writer.writerow((img, name, price, url))

phones.close()


mycon=mysql.connector.connect(host="localhost", user='root', passwd='@grade12', database='products')
cursor = mycon.cursor()

cursor.execute("DROP TABLE IF EXISTS applephones")
mycon.commit()

cursor.execute("CREATE TABLE applephones(image varchar(1000), name varchar(1000), price int(15), url varchar(1000))")
mycon.commit()

cursor.execute("ALTER DATABASE products CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
mycon.commit()

with open("AppleiPhones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO applephones(image, name, price, url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        mycon.commit()