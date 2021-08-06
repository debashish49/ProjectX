# ProjectX
ProjectX is a Django application that displays laptops and mobile phones from popular Japanese e-commerce websites on a single app - for users to search, compare and select the best product according to their preference.

# Group Members									  
Debashish Sahoo

Aditya Sundar

Darshan Shivakumar


# Project Functionalities
- **Login and Registration System:** 
Register a new user, Login with a user, Logout of a user.
- **Product Search:** 
Search for a laptop or phone from multiple retailers.
- **Search filtering:** 
Filter search by Price & Retailer.
- **Search History:** 
View history of all searches made on the website
- **Shopping Cart**: 
Add product to cart, View cart, Remove specific product from cart, Remove all products from cart, Print PDF of cart. Feature available only when a user is logged in

# Project Walkthrough 
 
## Web Scraping: 
Web scraping refers to the extraction of data from a website. To perform this task, we made use of the Python-based Beautiful Soup library. It allows us to parse through the HTML code of a website and extract the required information. 

To perform web scraping, a comprehensive knowledge of the various HTML tags is necessary, as the data you intend to scrape is embedded within these various tags. The web browser’s ‘Inspect Element’ feature comes into hand here, which allows you to view the HTML code of any section of the web page that you’re currently viewing. This helps us decipher the location of the information we intend to extract.

![My image](http://url/to/image.jpg)
Our project borrows data from renowned Japanese retailers, namely Yodobashi Camera, Bic Camera, Nojima, Yamada Denki, Kakaku and Rakuten, and Apple. For each e-commerce website, we programmed a code that recursively parsed through hundreds of pages of product results and extracted the product’s name, price, URL and image. 
Here’s part of a sample scraping program using Beautiful Soup:
    url = "https://kakaku.com/pc/note-pc/itemlist.aspx?pdf_vi=c" + pageurl
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    
    laptops = soup.findAll("div",{"class":"itemCatWrap"}) #extracting each product box
    try:
        for i in laptops:
            image = i.find("span",{"class":"itemCatImg"}).img.attrs['src']
            pname = i.find("span",{"class":"name2line"}).get_text().strip()
            price = i.find("span",{"class":"price"}).a.get_text().strip() #extracting image, name and price from each product box
We first added these details to a CSV file for keeping simple track of the items scraped. Then, we added these records to a MySQL Database, namely ‘products’, separated into two tables: ‘phones’ and ‘laptops’. 
Search Algorithm:
By incorporating Python-MySQL connectivity, we first developed a search algorithm that takes the user’s search input and displays details of relevant products from our database. We made use of MySQL’s full-text search feature, which displays all closely-matched records from the database, and ranks them by relevance. Before performing a full-text search with a particular field of a table, we need to create a full-text index of that field as shown below:
ALTER TABLE table_name ADD FULLTEXT(column_name) ;
Next, we can proceed to the actual search full-text search query. The following example searches through the name field of the laptop table for the user’s search input lenovo thinkpad:
SELECT * FROM laptops WHERE MATCH(name) AGAINST(‘lenovo thinkpad’ IN NATURAL LANGUAGE MODE) ; 

Say Hi to Django:

Our website is basically a product of a Django-based project. Django is a free-to-use high-level Python Web framework that encourages clean rapid project developments, by using the model-template-views architectural pattern.

Once we obtained all the product details and developed the search algorithm, we incorporated it into a new Django project and continued to develop our project further.

We created a Django project called projectx, created an app within project named searchapp, and then successfully ran the project:
debashish@MacBook-Pro % django-admin startproject projectx 
debashish@MacBook-Pro % cd projectx

debashish@MacBook-Pro projectx % python3 manage.py startapp searchapp

debashish@MacBook-Pro projectx % python3 manage.py runserver

Connecting Django to MySQL:

The obvious prerequisite to using Python-MySQL connectivity is importing mysql.connector and connecting the python file to the database, given as follows:

import mysql.connector 
con = mysql.connector.connect(host="localhost",user="root",password="grade12",database="products") 

Next, in settings.py of our Django app searchapp, we changed the standard SQLite backend that Django uses, to our very own MySQL as follows:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products',
        'USER': 'root',
        'PASSWORD': 'grade12',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
 
We also need to allow Django to migrate a few Django-authorized tables into our database to ensure all authentication throughout the server run remains smooth:
 
debashish@MacBook-Pro projectx % python3 manage.py migrate
debashish@MacBook-Pro projectx % python3 manage.py inspectdb > models.py
 
The above line of code allows Django to add these tables to our database:

Product Search:
Our website provides you with a beautiful search bar, that lets you search for your desired product. The results are displayed in a very attractive manner- clearly showing the products’ images, names, prices & the name of the retailer that sells the product. Clicking on the product name instantly takes you to the product’s original link from the retailer. 


And the list keeps going...

To program our search queries, we used Django’s raw function, that lets us execute raw SQL queries on Django models. For example:
 
query = "SELECT * FROM laptops WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "
 
products = Laptops.objects.raw(query)
 
Here, the products variable stores all the search results. This products variable is then used in our HTML page to appropriately display all the results. Here is a look at the relevant section from searchlaptops.html :
 
{% for i in products %}
<tr>
<td> <img src={{i.image}} width="200"> </td>
<td> <h3> <a href={{i.url}}> {{ i.name }} </a> </h3> </td>
<td> <h3>¥{{ i.price }}</h3></td>
. . . . . . . . . . . . . . . . . .
 
Here is the part of our code in views.py that is responsible for the search algorithm for laptops:
 
 
def searchlaptops(request):
 
    if request.method == "POST":
        search = request.POST['search']
        choices=request.POST['choices']
        retailer=request.POST['retailer']
 
        form=searchform(request.POST)
        form2=pricefilter(request.POST)
        form3=retailerfilter_laptop(request.POST)
        
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            search=form.cleaned_data["search"]
            choices=form2.cleaned_data["choices"]
            retailer=form3.cleaned_data["retailer"]
            history1.append([search, datetime.now().strftime("%d/%m %H:%M")])
        else:
            return render(request,"searchapp/searchlaptops.html", {
                "form":searchform(),
                "form2":pricefilter(),
                "form3":retailerfilter_laptop()
            })
 
        if search:
            global products
            if choices != '' and retailer != '':
                query = "SELECT * FROM laptops WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "+choices
                products = Laptops.objects.raw(query)
            elif choices !='' and retailer == '':
                query = "SELECT * FROM laptops WHERE MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "+choices
                products = Laptops.objects.raw(query)
            elif choices =='' and retailer != '':
                query = "SELECT * FROM laptops WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE)"
                products = Laptops.objects.raw(query)
            else:
                query = "SELECT * FROM laptops WHERE MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE)"
                products = Laptops.objects.raw(query)
            if products:
                return render(request, "searchapp/searchlaptops.html", {
                    "form":searchform(),
                    "form2":pricefilter(),
                    "form3":retailerfilter_laptop(),
                    "products": products
                    })
            else:
                messages.error(request,"No Results Found")    
        else:
            return HttpResponseRedirect("searchlaptops")
 
    return render(request, "searchapp/searchlaptops.html",{
        "form":searchform(),
        "form2":pricefilter(),
        "form3":retailerfilter_laptop()
    })
 
Filtering Search Results:
The product results can be further narrowed down using our smart filtering system, which allows the user to filter their searches: (1) By Retailer & (2) By Price:


 if search:
            global products
            if choices != '' and retailer != '':
                query = "SELECT * FROM phones WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "+choices
                cursor.execute(query)
                products=list(cursor.fetchall())
            elif choices !='' and retailer == '':
                query = "SELECT * FROM phones WHERE MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE) order by price "+choices
                cursor.execute(query)
                products=list(cursor.fetchall())
            elif choices =='' and retailer != '':
                query = "SELECT * FROM phones WHERE url like '%%"+retailer+"%%' and MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE)"
                cursor.execute(query)
                products=list(cursor.fetchall())
            elif choices == '' and retailer == '':
                query = "SELECT * FROM phones WHERE MATCH(name) AGAINST ('"+search+"' IN NATURAL LANGUAGE MODE)"
                cursor.execute(query)
                products=list(cursor.fetchall())

Search History:
This functionality allows us to see the history of all searches made (as well as the date and time of the search) when no user is logged in, and also the search history of each specific user when he/she is logged in! 




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



Login and Registration System:
New user registrations can be made by visiting the ‘Sign Up’ page. It is as simple as entering the relevant fields such as username, name, email and password, and proceeding to click the Register button. 


Failure to correctly re-enter your password, leaving fields empty, or signing up with a username that already exists, will give you an appropriate error message. To avoid accounts with duplicate usernames, we add every new user’s details to a new MySQL table userlist to our database. And by using simple Python-MySQL connectivity, we make the program check through the list of users to avoid duplicate registrations. 
 
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

Once a new account is registered, the user can log into the website by visiting the ‘Login’ page:






By entering their username and password, the user can successfully login. Entering invalid credentials will give you an appropriate error message. 


Once logged in, the user is redirected to the home page where he/she is welcomed with their first name! Logged in users can enjoy the benefit of the shopping cart feature, which will be explained at detail in a later section.



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

And of course, just as a user logs in, he/she can easily log out by simply clicking the ‘Logout’ button on the top right-hand corner of the page. 
def logout_view(request):
    logout(request)
    return render(request, "searchapp/login.html", {
        "form":loginform()
    })

Shopping Cart:
This feature allows a registered user to add a product to their shopping cart, by simply clicking the Add to Cart button next to a product:

Users can view their cart by visiting the ‘My Cart’ page. Here, they also have the ability to (1) remove any product from their cart, (2) remove all products from the cart, and (3) to print a PDF of their cart. The shopping cart is an exclusive feature only  available to registered users when they’re logged in. 


 {% if request.user.is_authenticated %}
                    <td> 
                        <form method="GET" action="{% url 'searchapp:searchlaptops' %}">
                            <button type="submit" name="cart" value={{i.0}} class="btn-boot btn-dark btn-elegant btn-rounded btn-sm my-0 waves-effect waves-light">                                
                                <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-cart-plus-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1H.5zM4 14a1 1 0 1 1 2 0 1 1 0 0 1-2 0zm7 0a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM9 5.5a.5.5 0 0 0-1 0V7H6.5a.5.5 0 0 0 0 1H8v1.5a.5.5 0 0 0 1 0V8h1.5a.5.5 0 0 0 0-1H9V5.5z"/>
                            </svg></button> 
                        </form>
                    </td>
                    {% endif %}

To store the cart details of a particular user, we designed the program to create a new MySQL table for every registered user under their username. Every time a user adds an item to their cart, the corresponding product details are added to the user’s own table on our database. And every time someone deletes products from their cart, they are also removed from the database table. 
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
        "username" : request.user.username })
The Print PDF button uses a bit of simple JavaScript, and allows the user to view a PDF preview of their shopping cart, giving them options to either print it immediately or save it as a PDF.
<script> 
    function printPage() { 
      window.print(); 
    } 
</script>







