import csv
import mysql.connector

#connecting to database
con = mysql.connector.connect(host="localhost",user="root",passwd="",database="products")     # update your user, password, and host
cursor = con.cursor()

cursor.execute("DROP TABLE IF EXISTS laptops")

query1= "CREATE TABLE laptops( no int AUTO_INCREMENT PRIMARY KEY, image varchar(255), name varchar(255), price int(20), url varchar(1000) )"
cursor.execute(query1)

with open("biccamera_laptops.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()


with open("biccamera_laptops2.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("kakaku_laptops.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("kakaku_laptops2.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("nojima_laptops.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("nojima_laptops2.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("yamadadenki_laptops.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("yamadadenki_laptops2.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("yodobashi_laptops.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO laptops(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()


cursor.execute("ALTER DATABASE products CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
con.commit()

cursor.execute("DROP TABLE IF EXISTS phones")

query2= "CREATE TABLE phones( no int AUTO_INCREMENT PRIMARY KEY, image varchar(255), name varchar(255), price int(20), url varchar(1000) )"
cursor.execute(query2)

with open("rakuten_phone.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO phones(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("rakuten_iphone.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        image = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO phones(image,name,price,url) VALUES (%s,%s,%s,%s)",(image,name,price,url))
        con.commit()

with open("BiciPhones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO phones(image, name, price, url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        con.commit()

with open("BicCamera_Phones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO phones(image,name,price,url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        con.commit()

with open("AppleiPhones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO phones(image, name, price, url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        con.commit()

with open("Yodobashi_Phones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO phones(image,name,price,url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        con.commit()

with open("Yamada_Phones.csv", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        print(i)
        img = i[0]
        name = i[1]
        price = i[2]
        url = i[3]
        cursor.execute("INSERT INTO phones(image,name,price,url) VALUES (%s,%s,%s,%s)",(img, name, price, url))
        con.commit()























































