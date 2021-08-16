# ProjectX
ProjectX is a user-friendly tool that displays laptops and mobile phones pre-scraped from popular Japanese e-commerce websites on a single app - for customers to search, compare and select the best product according to their preference.

## Project Functionalities
- **Login and Registration System:** 
Register a new user, Login with a user, Logout of a user.
- **Product Search:** 
Search for a laptop or phone from multiple retailers.
- **Search Filtering:** 
Filter search by Price & Retailer.
- **Search History:** 
View history of all searches made on the website.
- **Shopping Cart**: 
Add product to cart, View cart, Remove specific product from cart, Remove all products from cart, Print PDF of cart. _Feature available only when a user is logged in_.

## Languages Used

- Python (Django)
- HTML
- CSS

## How To Run Our Project

1. Clone the entire repository.
2. Run the python scraping files to add product details to your local MySQL database. 

_**Since this project was predominantly designed to showcase Python-database connectivity, the scraping program was designed to be a one-time process. There is a high probability that you may encounter issues with HTTP requests while running the scraping files. Hence, this is one reason why you may not be able to run our project!**_ 

3. Open your Terminal (Mac) and run the following lines of code:-

   Use appropriate command to navigate into the project directory:
   
    `cd projectx`
   
   Activate a virtual environment (optional):
   
    `virtualenv env`  
    
    `source env/bin/activate` &nbsp; #look for the path to your directory
    
    Run the server:
    
    `python3 manage.py runserver` 

## Project Walkthrough 
 
### Web Scraping: 

**_NOTE:_ This project does NOT automate the web scraping process.**

Web scraping refers to the extraction of data from a website. To perform this task, we made use of the Python-based Beautiful Soup library. It allows us to parse through the HTML code of a website and extract the required information. 

To perform web scraping, a comprehensive knowledge of the various HTML tags is necessary, as the data you intend to scrape is embedded within these various tags. The web browser’s ‘Inspect Element’ feature comes into hand here, which allows you to view the HTML code of any section of the web page that you’re currently viewing. This helps us decipher the location of the information we intend to extract.

![image](https://user-images.githubusercontent.com/69211573/128525767-68ff78e9-63bb-4d66-ae4d-dffb444a66eb.png)

<img src="https://user-images.githubusercontent.com/69211573/128526150-eda62424-4f04-42a3-afee-190df27a9637.png" height="200" width="1500">


![image](https://user-images.githubusercontent.com/69211573/128526183-d6d1a253-8151-42ac-bbee-1861a6355eed.png)

Our project borrows data from renowned Japanese retailers, namely Yodobashi Camera, Bic Camera, Nojima, Yamada Denki, Kakaku, Rakuten, and many others. For each e-commerce website, we programmed a code that recursively parsed through hundreds of pages of product results and extracted the product’s name, price, URL and image. We first added these details to a CSV file for keeping simple track of the items scraped. Then, we added these records to a MySQL Database, namely ‘products’, separated into two tables: ‘phones’ and ‘laptops’. 

### Search Algorithm:
By incorporating Python-MySQL connectivity, we first developed a search algorithm that takes the user’s search input and displays details of relevant products from our database. We made use of MySQL’s full-text search feature, which displays all closely-matched records from the database, and ranks them by relevance. 


### Django:

Our website is basically a product of a Django-based project. Django is a free-to-use high-level Python Web framework that encourages clean rapid project developments, by using the model-template-views architectural pattern.

Once we obtained all the product details and developed the search algorithm, we incorporated it into a new Django project and continued to develop our project further.

### Product Search:
Our website provides you with a beautiful search bar, that lets you search for your desired product. The results are displayed in a very attractive manner- clearly showing the products’ images, names, prices & the name of the retailer that sells the product. Clicking on the product name instantly takes you to the product’s original link from the retailer. 

![image](https://user-images.githubusercontent.com/69211573/128526487-9b82c451-ca42-46eb-b5a2-43319590a316.png)

To program our search queries, we used Django’s raw function, that lets us execute raw SQL queries on Django models. For example:
 
### Filtering Search Results:
The product results can be further narrowed down using our smart filtering system, which allows the user to filter their searches: (1) By Retailer & (2) By Price
![image](https://user-images.githubusercontent.com/69211573/128526771-ee263f8a-570d-4630-9da0-a89d6e2164c1.png)


### Search History:
This functionality allows us to see the history of all searches made (as well as the date and time of the search) when no user is logged in, and also the search history of each specific user when he/she is logged in! 

![image](https://user-images.githubusercontent.com/69211573/128526845-83ae53d3-bb69-45d7-a572-fbc6d791245e.png)

### Login and Registration System:
New user registrations can be made by visiting the ‘Sign Up’ page. It is as simple as entering the relevant fields such as username, name, email and password, and proceeding to click the Register button. 

![image](https://user-images.githubusercontent.com/69211573/128526928-dd173fc4-2dfc-4976-813b-b0f4942633ab.png)

Failure to correctly re-enter your password, leaving fields empty, or signing up with a username that already exists, will give you an appropriate error message. To avoid accounts with duplicate usernames, we add every new user’s details to a new MySQL table userlist to our database. And by using simple Python-MySQL connectivity, we make the program check through the list of users to avoid duplicate registrations. 

Once a new account is registered, the user can log into the website by visiting the ‘Login’ page.
By entering their username and password, the user can successfully login. Entering invalid credentials will give you an appropriate error message. 
Once logged in, the user is redirected to the home page where he/she is welcomed with their first name! Logged in users can enjoy the benefit of the shopping cart feature, which will be explained at detail in a later section.

![image](https://user-images.githubusercontent.com/69211573/128527129-59d16ab1-7299-4fa3-8c5d-f9c87bcbc034.png)

### Shopping Cart:
This feature allows a registered user to add a product to their shopping cart, by simply clicking the Add to Cart button next to a product:

![image](https://user-images.githubusercontent.com/69211573/128527243-a970ec37-e7dd-40f9-bfea-7754e8811864.png)

Users can view their cart by visiting the ‘My Cart’ page. Here, they also have the ability to (1) remove any product from their cart, (2) remove all products from the cart, and (3) to print a PDF of their cart. The shopping cart is an exclusive feature only  available to registered users when they’re logged in. 

![image](https://user-images.githubusercontent.com/69211573/128527303-22aab629-12d5-4c45-964d-7371947e4805.png)

To store the cart details of a particular user, we designed the program to create a new MySQL table for every registered user under their username. Every time a user adds an item to their cart, the corresponding product details are added to the user’s own table on our database. And every time someone deletes products from their cart, they are also removed from the database table. 

The Print PDF button uses a bit of simple JavaScript, and allows the user to view a PDF preview of their shopping cart, giving them options to either print it immediately or save it as a PDF.

![image](https://user-images.githubusercontent.com/69211573/128527363-5df37ada-fea5-46e6-9a6b-fcaaf879d454.png)

## Group Members									  
[Debashish Sahoo](https://github.com/debashishsahoo) <br>
Aditya Sundar <br>
Darshan Shivakumar

## License & Code Re-Use
The code for this project is released under the [GPL-3.0 License](./LICENSE). We ask that you please include a link back to this GitHub repository.
