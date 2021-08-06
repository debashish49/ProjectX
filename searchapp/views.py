from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
from searchapp.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import mysql.connector 

# Create your views here.
username = None
record_laptop = None
record_phone = None
products = None

def home(request):
    return render(request, "searchapp/home.html", {
    })

history1 = []
hist= []

def aboutus(request):
    return render(request, "searchapp/aboutus.html", {})

def history(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
    cursor = con.cursor()
    if request.user.is_authenticated:
        if request.GET:
            cursor.execute("delete from {}".format(request.user.username+"_hist"))
            con.commit()
        query1="select * from {}".format(request.user.username+"_hist")
        cursor.execute(query1)
        history1=cursor.fetchall()
        return render(request, "searchapp/history.html", {
        "history1" : history1
        })
    else:
        if request.GET:
            cursor.execute("delete from history")
            con.commit()
        cursor.execute("CREATE TABLE IF NOT EXISTS history (no int primary key auto_increment, history varchar(1000),date1 varchar(1000))")
        con.commit()
        query1="select * from history"
        cursor.execute(query1)
        history2=cursor.fetchall()
        return render(request, "searchapp/history.html", {
        "history2" : history2
        })

def mycart(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
    cursor = con.cursor()
    if request.GET:
        if "remove" in request.GET:
            no = request.GET["remove"]
            query = "DELETE FROM {} WHERE no = {}".format(request.user.username,no)
            con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
            cursor = con.cursor()
            cursor.execute(query)
            con.commit() 
        elif "removeall" in request.GET:
            query = "DELETE FROM {}".format(request.user.username)
            con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
    query = "SELECT * FROM {}".format(request.user.username)
    cursor.execute(query)
    records = list(cursor.fetchall())
    return render(request, "searchapp/mycart.html", {
        "records" : records,
        "username" : request.user.username
    })


def signup(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
    cursor = con.cursor()
    if request.method == "POST":
        cursor.execute("CREATE TABLE IF NOT EXISTS userlist (no int PRIMARY KEY AUTO_INCREMENT, username varchar(1000) NOT NULL, firstname varchar(1000) NOT NULL, lastname varchar(1000) NOT NULL, password varchar(12) NOT NULL)")
        con.commit()
        query = "SELECT username FROM userlist"
        cursor.execute(query)
        records = cursor.fetchall()

        sign_form = signupform(request.POST)

        for i in records:
            if request.POST.get("username") == i[0]:
                return render(request, "searchapp/signup.html", {
                    "message":"Username already exists",
                    "form": signupform()
                })
                break
        else:
            if sign_form.is_valid():
                
                user_name = sign_form.cleaned_data['username']
                firstname = sign_form.cleaned_data['firstname']
                lastname = sign_form.cleaned_data['lastname']
                password = sign_form.cleaned_data['password']
                repassword = sign_form.cleaned_data['repassword']

                if password != repassword:
                    return render(request, "searchapp/signup.html", {
                    "form": signupform(),
                    "password_message": "Passwords do not match"
                })

                global username
                query="insert into userlist (username,firstname,lastname,password) values ('{}','{}','{}','{}')".format(user_name, firstname, lastname, password)
                cursor.execute(query)

                user = User.objects.create_user(username=user_name, password=password)
                
                user.first_name = firstname
                user.last_name = lastname
                user.save()

                query1 = "CREATE TABLE {} (no int PRIMARY KEY, image varchar(1000) NOT NULL, name varchar(1000) NOT NULL, price int(20) NOT NULL, url varchar(1000) NOT NULL )".format(user_name)
                cursor.execute(query1)
                
                query2="CREATE TABLE {} (no int PRIMARY KEY AUTO_INCREMENT,history varchar(1000),date1 varchar(1000))".format(user_name+"_hist")
                cursor.execute(query2)
                
                con.commit()
                
                return render(request, "searchapp/signup.html", {
                    "complete":"New User Registration Complete!",
                    "form": signupform()
                })
            else:
                return render(request, "searchapp/signup.html", {
                    "message":"Enter all the details",
                    "form": signupform()
                })
    return render(request, "searchapp/signup.html", {
        "form": signupform()
    })

def login_view(request):
    if request.method == "POST":

        login_form = loginform(request.POST)

        global username
        
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username= user_name, password= password)

        if user is not None:
            login(request, user)
            return render(request,"searchapp/home.html")
        else:
            return render(request,"searchapp/login.html", {
                "message": "Invalid Credentials",
                "form":loginform()
            })
    return render(request, "searchapp/login.html", {
        "form":loginform()
    })

def logout_view(request):
    logout(request)
    return render(request, "searchapp/login.html", {
        "form":loginform()
    })

def searchlaptops(request): 
    con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
    cursor=con.cursor()
    if request.method == "POST":
        global search
        search = request.POST['search']
        choices = request.POST['choices']
        retailer = request.POST['retailer']

        form = searchform(request.POST)
        form2 = pricefilter(request.POST)
        form3 = retailerfilter_laptop(request.POST)
        
        cursor.execute("CREATE TABLE IF NOT EXISTS history (no int primary key auto_increment, history varchar(1000),date1 varchar(1000))")
        con.commit()

        if form.is_valid() and form2.is_valid() and form3.is_valid():
            search = form.cleaned_data["search"]
            choices = form2.cleaned_data["choices"]
            retailer = form3.cleaned_data["retailer"]
            if request.user.is_authenticated:
                query1 = "insert into {} (history,date1) values ('{}','{}')".format(request.user.username+"_hist",search,datetime.now().strftime("%d/%m %H:%M"))
                cursor.execute(query1)
                con.commit()
            else:
                query1 = "insert into history (history,date1) values ('{}','{}')".format(search,datetime.now().strftime("%d/%m %H:%M"))
                cursor.execute(query1)
                con.commit()
        else:
            return render(request,"searchapp/searchlaptops.html", {
                "form":searchform(),
                "form2":pricefilter(),
                "form3":retailerfilter_laptop()
            })
        # if search:
        #     global products
        #     if choices != '' and retailer != '':
        #         query = "SELECT * FROM laptops WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "+choices
        #         cursor.execute(query)
        #         products = list(cursor.fetchall())
        #     elif choices !='' and retailer == '':
        #         query = "SELECT * FROM laptops WHERE MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "+choices
        #         cursor.execute(query)
        #         products = list(cursor.fetchall())
        #     elif choices =='' and retailer != '':
        #         query = "SELECT * FROM laptops WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE)"
        #         cursor.execute(query)
        #         products = list(cursor.fetchall())
        #     else:
        #         query = "SELECT * FROM laptops WHERE MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE)"
        #         cursor.execute(query)
        #         products = list(cursor.fetchall())
        if search:
            global products
            if choices != '' and retailer != '':
                query = "SELECT * FROM laptops WHERE url like '%%{}%%' and MATCH(name) AGAINST ('{}' IN NATURAL LANGUAGE MODE) order by price {} ".format(retailer,search,choices)
                cursor.execute(query)
                products = list(cursor.fetchall())
            elif choices !='' and retailer == '':
                query = "SELECT * FROM laptops WHERE MATCH(name) AGAINST ('{}' IN NATURAL LANGUAGE MODE) order by price {}".format(search,choices)
                cursor.execute(query)
                products = list(cursor.fetchall())
            elif choices =='' and retailer != '':
                query = "SELECT * FROM laptops WHERE url like '%%{}%%' and MATCH(name) AGAINST ('{}' IN NATURAL LANGUAGE MODE)".format(retailer,search)
                cursor.execute(query)
                products = list(cursor.fetchall())
            else:
                query = "SELECT * FROM laptops WHERE MATCH(name) AGAINST ('{}' IN NATURAL LANGUAGE MODE)".format(search)
                cursor.execute(query)
                products = list(cursor.fetchall())

            if products:
                return render(request, "searchapp/searchlaptops.html", {
                    "form":searchform(),
                    "form2":pricefilter(),
                    "form3":retailerfilter_laptop(),
                    "products": products,
                    "search":search
                    })
            else:
                messages.error(request,"No Results Found")    
        else:
            return HttpResponseRedirect("searchlaptops")
        con.commit()
        
    if request.GET:
        con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
        cursor = con.cursor()
        query1 = "SELECT no FROM {}".format(request.user.username)
        cursor.execute(query1)
        records = cursor.fetchall()
        for i in records:
            if int(request.GET["cart"]) == int(i[0]):
                return render(request, "searchapp/searchlaptops.html", {
                    "form":searchform(),
                    "form2":pricefilter(),
                    "form3":retailerfilter_laptop(),
                    "products":products,
                    "search":search,
                    "message":"This item already exists in cart"
                })
        else:
            no = request.GET['cart']
            query = "SELECT * FROM laptops WHERE no = {}".format(no)
            con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
            cursor = con.cursor()
            cursor.execute(query)
            record_laptop = cursor.fetchone()
            img_url = record_laptop[1]
            name = record_laptop[2]
            price = record_laptop[3]
            url = record_laptop[4]
            query = 'INSERT INTO {} VALUES({}, "{}", "{}", {}, "{}")'.format(request.user.username, no, img_url, name, price, url)
            cursor.execute(query)
            con.commit() 
            return render(request, "searchapp/searchlaptops.html",{
                "form":searchform(),
                "form2":pricefilter(),
                "form3":retailerfilter_laptop(),
                "search":search,
                "products":products
            })

    return render(request, "searchapp/searchlaptops.html",{
        "form":searchform(),
        "form2":pricefilter(),
        "form3":retailerfilter_laptop()
    })

def searchphones(request): 
    con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
    cursor = con.cursor()
    if request.method == "POST":
        global search
        search = request.POST['search']
        choices = request.POST['choices']
        retailer = request.POST['retailer']

        form = searchform(request.POST)
        form2 = pricefilter(request.POST)
        form3 = retailerfilter_phones(request.POST)

        cursor.execute("CREATE TABLE IF NOT EXISTS history (no int primary key auto_increment, history varchar(1000),date1 varchar(1000))")
        con.commit()

        if form.is_valid() and form2.is_valid() and form3.is_valid():
            search=form.cleaned_data["search"]
            choices=form2.cleaned_data["choices"]
            retailer=form3.cleaned_data["retailer"]
            if request.user.is_authenticated:
                query1 = "insert into {} (history,date1) values ('{}','{}')".format(request.user.username+"_hist",search,datetime.now().strftime("%d/%m %H:%M"))
                cursor.execute(query1)
                con.commit()
            else:
                query1 = "insert into history (history,date1) values ('{}','{}')".format(search,datetime.now().strftime("%d/%m %H:%M"))
                cursor.execute(query1)
                con.commit()
        else:
            return render(request,"searchapp/searchphones.html", {
            "form":searchform(),
            "form2":pricefilter(),
            "form3":retailerfilter_phones()
            })
        # if search:
        #     global products
        #     if choices != '' and retailer != '':
        #         query = "SELECT * FROM phones WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "+choices
        #         cursor.execute(query)
        #         products=list(cursor.fetchall())
        #     elif choices !='' and retailer == '':
        #         query = "SELECT * FROM phones WHERE MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "+choices
        #         cursor.execute(query)
        #         products=list(cursor.fetchall())
        #     elif choices =='' and retailer != '':
        #         query = "SELECT * FROM phones WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE)"
        #         cursor.execute(query)
        #         products=list(cursor.fetchall())
        #     elif choices == '' and retailer == '':
        #         query = "SELECT * FROM phones WHERE MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE)"
        #         cursor.execute(query)
        #         products=list(cursor.fetchall())
        if search:
            global products
            if choices != '' and retailer != '':
                query = "SELECT * FROM phones WHERE url like '%%{}%%' and MATCH(name) AGAINST ('{}' IN NATURAL LANGUAGE MODE) order by price {} ".format(retailer,search,choices)
                cursor.execute(query)
                products = list(cursor.fetchall())
            elif choices !='' and retailer == '':
                query = "SELECT * FROM phones WHERE MATCH(name) AGAINST ('{}' IN NATURAL LANGUAGE MODE) order by price {}".format(search,choices)
                cursor.execute(query)
                products = list(cursor.fetchall())
            elif choices =='' and retailer != '':
                query = "SELECT * FROM phones WHERE url like '%%{}%%' and MATCH(name) AGAINST ('{}' IN NATURAL LANGUAGE MODE)".format(retailer,search)
                cursor.execute(query)
                products = list(cursor.fetchall())
            else:
                query = "SELECT * FROM phones WHERE MATCH(name) AGAINST ('{}' IN NATURAL LANGUAGE MODE)".format(search)
                cursor.execute(query)
                products = list(cursor.fetchall())

            if products:
                return render(request, "searchapp/searchphones.html", {
                    "form":searchform(),
                    "form2":pricefilter(),
                    "form3":retailerfilter_phones(),
                    "products": products,
                    "search":search
                    })
            else:
                messages.error(request,"No Results Found")    

        else:
            return HttpResponseRedirect("searchphones")
        con.commit()
    
    if request.GET:
        con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
        cursor = con.cursor()
        query1 = "SELECT no FROM {}".format(request.user.username)
        cursor.execute(query1)
        records = cursor.fetchall()
        for i in records:
            if int(request.GET["cart"]) == int(i[0]):
                return render(request, "searchapp/searchphones.html", {
                    "form":searchform(),
                    "form2":pricefilter(),
                    "form3":retailerfilter_laptop(),
                    "products":products,
                    "search":search,
                    "message":"This item already exists in cart"
                })
        else:
            no = request.GET['cart']
            query = "SELECT * FROM phones WHERE no = {}".format(no)
            con = mysql.connector.connect(host="localhost",user="root",passwd="@grade12",database="products")
            cursor = con.cursor()
            cursor.execute(query)
            global record_phone
            record_phone = cursor.fetchone()
            img_url = record_phone[1]
            name = record_phone[2]
            price = record_phone[3]
            url = record_phone[4]
            query = 'INSERT INTO {} VALUES({}, "{}", "{}", {}, "{}")'.format(request.user.username, no, img_url, name, price, url)
            cursor.execute(query)
            con.commit() 
            return render(request, "searchapp/searchphones.html",{
                "form":searchform(),
                "form2":pricefilter(),
                "form3":retailerfilter_laptop(),
                "products":products,
                "search":search
            })


    return render(request, "searchapp/searchphones.html",{
        "form":searchform(),
        "form2":pricefilter(),
        "form3":retailerfilter_phones()
    })



