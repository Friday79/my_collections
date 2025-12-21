<a id="top"></a>
## My_Collections – Django E-commerce Platform
**My_Collections** is a full-featured e-commerce platform built with Django. It offers a seamless shopping experience for users to browse and purchase **clothing essentials, homeware, and special offers**. The platform includes user registration with **Allauth**,a wishlist, a dynamic shopping bag system, **search functionality**, a secure **Stripe-powered checkout**, and an intuitive **admin dashboard** for managing products and orders.
To Navigate the site, on the  **Homepage** top left corner, when you click **mycollections Logo** it will take you back to the homepage . Next on the right side of mycollections logo is the **Search functionality**, that we can use to search for product. Next to that is the **Account registration**,where we can **register** and create a **profile** and can **logout** of the page or **login** when the account is clicked. As an **Admin user**, you can **login as superuser**, by typing **python3 manage.py createsuperuser**, then fill in your **Username** ,**Email** and **Password** in the terminal.Then navigate to **Admin board** , there you can manage product by **Updating, Editing,Creating and Deleting**.
At the Nav we have all product ,that when we click , we can choose the product we want by **price, rating, category**. Next is **Clothing**, when clicked, we can select the category of clothe we want. Next is **Homeware**,when clicked, we can select the one we want from the list.Next is **Special offer**, when clicked we can also select what we want from the list. At the top right corner of the home page is the **Bag icon** that when clicked we can can see the products we have selected, and the total cost.
There is a shop now link that when clicked, it will take us to the store. If any product is clicked, then in the product details, we can **review, select seize,rate, increase quantity** with the increment and decrement button. At the bottom of the product detail page we click on add to bag, to add the product to bag and click on keep shopping to continue shopping. 
In the bag we will see all the product we have added to the bag,then we can edit or delete product before we click on checkout at the bottom of the page, which then take us to the payment section,where we will fill in our shipping information and make payment, then **Receive Email Comfirmation** after payment.


## Table of Contents

- [My_Collections – Django E-commerce Platform](#my_collections--django-e-commerce-platform)
- [Important Comment](#important-comment)
- [E-Commerce Business Model for MyCollection](#e-commerce-business-model-for-mycollection)
  - [Business Overview](#business-overview)
  - [Value Proposition](#value-proposition)
  - [Target Customers](#target-customers)
  - [Product Offering](#product-offering)
  - [Revenue Streams](#revenue-streams)
  - [Marketing Strategy](#marketing-strategy)
  - [Operations Model](#operations-model)
  - [Cost Structure](#cost-structure)
  - [Competitive Advantage](#competitive-advantage)
- [Live Site](#-live-site)
- [Screenshots](#-screenshots)
- [Social Media Marketing](#social-media-marketing)
- [Flowchart](#flowchart)
- [Wireframes](#wireframes)
- [404 Error Page](#404-error-page)
- [Agile Method](#agile-method)
- [Testing](#testing)
  - [CSS Testing](#css-testing)
  - [HTML Validation](#html-validation)
  - [JavaScript (JSHint) Testing](#jshint-stripe-testing)
  - [Coverage Report Bag](#coverage-report-bag)
- [Deployment](#deployment)
- [How To Use This Project](#how-to-use-this-project)
  - [Fork GitHub Repository](#fork-github-repository)
  - [Clone GitHub Repository](#clone-github-repository)
- [Project Setup After Forking or Cloning](#project-set-up-after-forking-or-cloning)
- [Deployment to Heroku](#deployment-to-heroku)
- [AWS bucket creation](#aws-bucket-creation)
- [Features](#features)
  - [Core Features](#core-features)
  - [User Features](#user-features)
- [Bugs](#bug)
- 
- [Project Structure](#project-structure)
- [Admin Access](#admin-access)

- [Acknowledgments](#acknowledgments)

**E-Commerce Business Model for MyCollection**

1. ## Business Overview

**MyCollection** is an online boutique store that sells curated fashion items and lifestyle accessories.
- The platform allows users to browse products, add items to a shopping bag, securely checkout, and manage their own profiles.

2. ## Value Proposition

MyCollection provides:

- A simple and visually appealing online shopping experience.

- High-quality, handpicked items.

- Secure checkout using Stripe.

- Personalized user accounts for order history and saved details.

- A newsletter for exclusive discounts and product launches.

3. ## Target Customers

- Fashion lovers aged 18–55.

- Online shoppers looking for unique collections.

- People who prefer buying boutique products rather than mass-market items.

- Social media users influenced by lifestyle trends.

4. ## Product Offering

- Clothing (men/women/unisex)

- Accessories (bags, watch, belts, etc.)

- Handcrafted items

- Artwork

- Shoes

- Seasonal “limited collection” drops

- Each product typically includes:

- Name

- Description

- Price

- Category

- Image

- Stock/availability information

5. ## Revenue Streams

- Direct product sales

- Seasonal promotions (Black Friday, summer sale)

- Newsletter-driven campaigns

- Limited edition drops to create demand

6. ## Marketing Strategy

- MyCollection uses multiple digital marketing strategies:

- Social Media Marketing

- Instagram and Facebook pages showing products

- Reels and stories for new arrivals

- Email Marketing

- Newsletter signup form on the homepage

- Exclusive discount codes sent via email

- SEO Strategy

- Relevant keywords ("boutique store", "unique accessories")

- Meta description and Open Graph tags

- Sitemap and robots.txt configured

- Responsive, mobile-friendly UI

- Customer Engagement

- Polls on homepage 

- Comment sections or reviews (if implemented)

- Personalized recommendations (optional)

7. ## Operations Model
- Order Processing Workflow

- Customer adds product to cart.

- Customer checks out securely via Stripe PaymentIntent.

- Order saved to database and Stripe dashboard.

- Stripe webhook confirms successful payment.

- Order email confirmation sent to customer.

- Admin panel used to fulfil orders.

- Inventory Management

- Stock numbers managed through the Django admin panel.

- Customer Support

- Contact form

- Email support (your email: fridexcool@gmail.com
)

8. ## Cost Structure

- Hosting costs (GitHub + Render/Heroku)

- Stripe transaction fees

- Marketing (Facebook/Instagram ads)

- Product sourcing or manufacturing costs

- Domain name registration (optional)

9. ## Competitive Advantage

- MyCollection stands out because:

- Boutique-style curated selection instead of mass-market products.

- Clean, mobile-first design using Bootstrap.

- Fast and secure checkout via Stripe.

- Engaging homepage poll system.

- Newsletter for customer loyalty.




---

## 🔗 Live Site

 [Deployed Site on Heroku](https://mycollections-379ea5dbbc8f.herokuapp.com/)
    [Stripe Payments](https://stripe.com)
    [GitHub Repository](https://github.com/Friday79/my_collections)


---

## 📸 Screenshots

- Home Page
- ![image](https://github.com/user-attachments/assets/5eb821da-d9d6-453d-a6ea-55671820b91f)

- ![image](https://github.com/user-attachments/assets/
d2b7e597-3626-4734-be36-e9f7bf9259a5)

- Display to the shopper the product categories available, providing a link to each category.

- Search Results
- ![image](https://github.com/user-attachments/assets/0d0424a8-c238-46e1-856e-ddef0b788f2d)

- ![image](https://github.com/user-attachments/assets/022bbe38-c7b4-4486-a35a-e5aaf0c0d625)


- Product Detail
- ![image](https://github.com/user-attachments/assets/894b40c2-11b1-4e28-a499-ffe55a1bf600)


**Wishlist**
- ![image](https://github.com/user-attachments/assets/56557a9c-c8a9-4997-a058-49dbcbf29803)

- Enable user to choose a wish product,then later move it to bag or remove from wishlist


**Profile**
- ![image](https://github.com/user-attachments/assets/a4240cfc-a4c6-4f88-bf7a-d908342ea724)

- Provide a form for the registered shopper to update their default information.

- An order history section is present with all registered shopper's past orders information.


## Shopping Bag
- ![image](https://github.com/user-attachments/assets/
5f2ebd43-e33f-44ca-b2ce-ff851fb07540)

- A message alerts the user in case the free delivery threshold has not been reached, displaying the amount left.

- Display all products currently on the shopping bag and their information.

- Allow the user to update the product quantity or remove the product from the shopping bag.

- Display the current total cost including the bag total and delivery costs.

- Provide a "Keep Shopping" button to go back to the products.

- A button to checkout is provided for the shopper to finish the purchase.

## Stripe Checkout
- ![image](https://github.com/user-attachments/assets/bee01ffd-5d4d-4272-a785-c0b2c6ad1e5f)

- Provide a checkout form for the shopper to complete the purchase and provide the necessary contact, shipping and payment information.

- Display an order summary listing all the products to be purchased and their total cost including the bag total and delivery costs.

- Provide a link back to the shopping bag in the case the shopper would like to adjust the products in the shopping bag.

- A message is displayed, informing the shopper the amount to be charged on the provided card.

- Descriptive error messages are displayed in case there is any issue with the payment information provided.

- A button is clearly available for the shopper to complete the order.

- Stripe webhook handler is created in the backend to pass the order information in the case the browser crashes once the checkout completion.


**Order Receipt**
- ![image](https://github.com/user-attachments/assets/d6478eaa-f603-443e-abe0-04798b8833b3)

- Display the order and shopper information to allow the shopper to confirm that the information provided is correct.

- Additionally, informs the shopper that an email has been sent to the email address provided with the same information.

- A link to the organizations we would like the shoppers to support is provided at the bottom of the page.

## Admin Dashboard
- ![image](https://github.com/user-attachments/assets/15bd0a0f-0ad8-4b08-b531-c1298f40af09)

## 404 ERROR PAGE
- ![image](https://github.com/user-attachments/assets/391161ac-a5bc-4c8f-adc9-9052c24cf8db)

- Provided information to the shopper in case the address entered cannot be found.

- A link to come back to the products is present.

- ## Css Testing


- ![Image](https://github.com/user-attachments/assets/e9d64aa4-dfaf-4c3d-9009-39117bb5eb82)

- ## Html validation.
- ![image](https://github.com/user-attachments/assets/fb66c9b5-742e-4675-a9f6-5a7eeb1b8029)

- ![image](https://github.com/user-attachments/assets/9065710c-85d0-46d4-bfb8-e0a5d2cde0b6)

- ## Pep8 for settings.py
- ![image](https://github.com/user-attachments/assets/c6a4ef0e-8ebb-498d-ac10-423d786aec6a)

- ## Pep8 for checkout views.py
- ![image](https://github.com/user-attachments/assets/d8036398-ac74-40cc-8e94-335fceb87cba)

- ## Checkout Css Testing
- ![image](https://github.com/user-attachments/assets/d4d3ef33-d297-496b-b481-94de9a7bd405)

## SOCIAL MEDIA MARKETING

- - ##  Newsletter Signup with Mailchimp For Email Marketing
- - ![image](https://github.com/user-attachments/assets/5c26f95b-0ba3-4d03-b305-a6d6d74c4f52)

- ![image](https://github.com/user-attachments/assets/baa7dac9-af9a-4b91-bcef-d317ac775e5a)


- ## Facebook Business Marketing page For B2C
-  [Mock Facebook Business Page](https://www.facebook.com/people/mycollections)
- ![image](https://github.com/user-attachments/assets/de385d74-5cf2-475c-b8f8-45b5b62e6fe3)

- ## FLOWCHART
- ![image](https://github.com/user-attachments/assets/def88c09-bbec-4060-b7ea-75c5ca940305)

- ## Skeleton
- ## Wireframes
- [Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.
- ![image](https://github.com/user-attachments/assets/6a29f0b2-aa96-411e-b9fc-01196b62883d)
- ![image](https://github.com/user-attachments/assets/2a81ac94-d257-4c83-aaaa-7198ba34bda5)
- ![image](https://github.com/user-attachments/assets/13923cf3-0d96-4d95-863d-4688808a3787)
- ![image](https://github.com/user-attachments/assets/19e27ff6-5ebc-4327-a48f-39100bede94e)
- ![image](https://github.com/user-attachments/assets/5e4f73fd-e2d9-481c-9587-7e4b772f447d)
- ![image](https://github.com/user-attachments/assets/d65ed7fd-5cf9-4b35-9d42-9df69def8a95)
- ![image](https://github.com/user-attachments/assets/9c46e299-ef38-4caf-8c36-9cbed9c5b4f5)

- [Back To Top](#top)

- ## Agile method
- ![image](https://github.com/user-attachments/assets/490dc086-d1f8-41c0-b267-3658019c60b7)
- ![image](https://github.com/user-attachments/assets/a97ea7fb-7c66-4159-aa58-ac3f52c0a43b)
- ![image](https://github.com/user-attachments/assets/63bce6f9-04a9-41db-ae70-13e6d5702633)
- ![image](https://github.com/user-attachments/assets/6de86413-99a5-4197-8704-b85d3a2fda01)
- ![image](https://github.com/user-attachments/assets/7419daaa-d4c0-4a2b-a5f8-0c4106dd96d1)
- ![image](https://github.com/user-attachments/assets/7da69a55-4f2c-42ee-80c2-524818c46f7c)
- ![image](https://github.com/user-attachments/assets/124726d3-ae09-4f7d-ab0d-a73d99ce2405)

- [Back To Top](#top)





- ## jshint Stripe testing
- ![image](https://github.com/user-attachments/assets/3a8d6440-bd57-4573-a629-d17acc032cb9)

## Python Testing & Coverage Reports
## Coverage Report BAG
- ![image](https://github.com/user-attachments/assets/c3766e88-e073-4992-807b-9c4f4da0a660)

- Name                            Stmts   Miss  Cover
---------------------------------------------------
bag/__init__.py                     0      0   100%
bag/admin.py                        1      0   100%
bag/apps.py                         4      0   100%
bag/contexts.py                    28      7    75%
bag/migrations/__init__.py          0      0   100%
bag/models.py                       1      0   100%
bag/templatetags/__init__.py        0      0   100%
bag/templatetags/bag_tools.py       5      0   100%
bag/test_views.py                  40      0   100%
bag/tests.py                        1      0   100%
bag/urls.py                         3      0   100%
bag/views.py                       70     29    59%



- ## Coverage Checkout
- ![image](https://github.com/user-attachments/assets/88cd35e8-9392-40ac-8eaf-8b976f49ab08)

- Name                                              Stmts   Miss  Cover
---------------------------------------------------------------------
checkout/__init__.py                                  1      0   100%
checkout/admin.py                                    12      0   100%
checkout/apps.py                                      6      0   100%
checkout/forms.py                                    18      0   100%
checkout/migrations/0001_initial.py                   6      0   100%
checkout/migrations/0002_auto_20250324_1704.py        4      0   100%
checkout/migrations/0003_alter_order_country.py       5      0   100%
checkout/migrations/0004_order_user_profile.py        5      0   100%
checkout/migrations/__init__.py                       0      0   100%
checkout/models.py                                   51      3    94%
checkout/signals.py                                   9      1    89%
checkout/test_forms.py                               15      0   100%
checkout/test_models.py                              25      0   100%
checkout/test_views.py                               24      0   100%
checkout/tests.py                                     1      0   100%
checkout/urls.py                                      4      0   100%


- ## Coverage Report Products
- ![image](https://github.com/user-attachments/assets/c9088bcd-d174-439d-9c88-01b3ca9afaaf)

- Name                                                 Stmts   Miss  Cover
------------------------------------------------------------------------
products/__init__.py                                     0      0   100%
products/admin.py                                       14      0   100%
products/apps.py                                         4      0   100%
products/forms.py                                       20      0   100%
products/migrations/0001_initial.py                      6      0   100%
products/migrations/0002_alter_category_options.py       4      0   100%
products/migrations/0003_alter_product_image.py          4      0   100%
products/migrations/0004_product_has_sizes.py            4      0   100%
products/migrations/0005_review.py                       6      0   100%
products/migrations/__init__.py                          0      0   100%
products/models.py                                      31      0   100%
products/test_forms.py                                  38      0   100%
products/test_models.py                                 30      0   100%
products/test_views.py                                  49      0   100%
products/tests.py                                        1      0   100%
products/urls.py                                         3      0   100%
products/views.py                                      102     47    54%
products/widgets.py                                      7      0   100%

- ## coverage report profiles
- ![image](https://github.com/user-attachments/assets/652af5ec-c403-4460-a759-ee04be8ec5f7)


- Name                                  Stmts   Miss  Cover
- ---------------------------------------------------------
- profiles/__init__.py                      0      0   100%
- profiles/admin.py                         1      0   100%
- profiles/apps.py                          4      0   100%
- profiles/forms.py                        18      1    94%
- profiles/migrations/0001_initial.py       8      0   100%
- profiles/migrations/__init__.py           0      0   100%
- profiles/models.py                       21      0   100%
- profiles/test_forms.py                   23      0   100%
- profiles/test_models.py                  13      0   100%
- profiles/test_views.py                   33      0   100%
- profiles/tests.py                         1      0   100%
- profiles/urls.py                          3      0   100%
- profiles/views.py                        25      0   100%

- [Back To Top](#top)

## Deployment
The project was developed using[Gitpod](https://www.gitpod.io/). workspace. The code was commited to  [Git](https://git-scm.com/). and pushed to GitHub using the terminal. The web application is deployed on Heroku as  [GitHub](https://github.com/your-username/my_collections). Pages is not able to host a Python project. Static and media files are being stored in AWS S3. The repository is hosted on Github.

## How To Use This Project
To use and further develop this project you can either fork or clone the repository.

## Fork GitHub Repository
By forking the GitHub repository you can make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository, by using the following steps:

1. Log in to GitHub.
2. Navigate to the main page of the GitHub Repository that you want to fork.
3. At the top right of the Repository just below your profile picture, locate the "Fork" button.
4. You should now have a copy of the original repository in your GitHub account.
5. Changes made to the forked repository can be merged with the original repository via a pull request.
## Clone Github Repository
By cloning a GitHub repository you can create a local copy on your computer of the remote repository. The developer who clones a repository can synchronize their copy of the codebase with any updates made by fellow developers with push or pull request. Cloning is done by using the following steps:

1. Log in to GitHub.
2. Navigate to the main page of the GitHub Repository that you want to clone.
3. Above the list of files, click the dropdown called "Code".
4. To clone the repository using HTTPS, under "HTTPS", copy the link.
5. Open Git Bash.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type git clone, and then paste the URL you copied in Step 4.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
8. 
Press Enter. Your local clone will be created.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
Changes made on the local machine (cloned repository) can be pushed to the upstream repository directly if you have a write access for the repository. Otherwise, the changes made in the cloned repository are first pushed to the forked repository, and then a pull request is created.
Click [Here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Project Set Up After Forking or Cloning
1. Install all dependencies by typing in the CLI pip3 install -r requirements.txt

2. Create a .gitignore file and env.py file in the project's root directory. Add the env.py file to .gitignore.

3. Inside the env.py file, enter the project's environment variables:

## import os

os.environ.setdefault("SECRET_KEY", <your_secret_key>)
os.environ.setdefault("DEVELOPMENT", '1')
os.environ.setdefault("STRIPE_PUBLIC_KEY", <your_key>)
os.environ.setdefault("STRIPE_SECRET_KEY", <your_key>)
os.environ.setdefault("STRIPE_WH_SECRET", <your_key>)
You can get the keys from:

- "SECRET_KEY" can be generated using Django Secret Key Generator
- "STRIPE_PUBLIC_KEY" and "STRIPE_SECRET_KEY" can be generated by creating a stripe account. The keys are found in 'Developers' Section, under 'API Keys'.
- In the Developer Section, under 'Webhooks', add a new endpoint. "STRIPE_WH_SECRET". On Endpoint URL, enter:
https://<your_host_url>/checkout/wh/
Select to listen to all events, and create endpoint, and you can view your "STRIPE_WH_SECRET".
- Make migrations to setup the inital database operations.

python3 manage.py makemigrations 
python3 manage.py migrate 
5. Load data for the database or create data manually.

python3 manage.py loaddata <app_name>
6. Create a super user.

python3 manage.py create superuser
The **project** should now complete to run and can now be used for development. To run the **project**, type in the CLI terminal: python3 manage.py runserver

## Deployment to Heroku
This **project** is deployed on Heroku for production, with all static and media files stored on AWS S3. These are steps to deploy on Heroku:

1. Navigate to Heroku.com, create a new account or login if you already have an account. On the dashboard page, click "Create New App" button. Give the app a name, the name must be unique with hypens between words. Set the region closest to you, and click "Create App".

2. On the resources tab, provision a new Heroku Postgres database.

3. Configure variables on Heroku by navigating to Settings, and click on Reveal Config Vars. You may not have all the values yet. Add the others as you progress through the steps.

Varables	Key
AWS_ACCESS_KEY_ID	your_access_key_id_from_AWS
AWS_SECRET_ACCESS_KEY	your_secret_access_key_from_AWS
DATABASE_URL	your_database_url
EMAIL_HOST_PASS	your_app_password_from_your_email
EMAIL_HOST_USER	your_email_address
SECRET_KEY	your_secret_key
STRIPE_PUBLIC_KEY	your_stripe_public_key
STRIPE_SECRET_KEY	your_stripe_secret_key
USE_AWS	True
4. If you haven't install it, install dj_database_url and psycopg2.

pip3 install dj_database_url
pip3 install psycopg2-binary
Note: you don't have to do this if you've installed all dependencies in the requirements.txt file.

4. Set up a new database for the site by going to the project's settings.py and importing dj_database_url. Comment out the database's default configuration, and replace the default database with a call to dj_database_url.parse and pass it the database URL from Heroku (you can get it from your config variables in your app setting tab)

DATABASES = {
  'default': dj_database_url.parse('YOUR_DATABASE_URL_FROM_HEROKU')
}
6. Run migrations

python3 manage.py migrate
7. Import data to the database.

- Make sure your manage.py file is connected to your sqlite3 database.
- Use this command to backup your current database and load it into a db.json file:
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
- Connect your manage.py file to your postgres database
- Then use this command to load your data from the db.json file into postgres:
./manage.py loaddata db.json
8. Set up a new superuser, fill out the username, email address, and password.

python3 manage.py create superuser
9. Remove the database config from Heroku and uncomment the original config. Add a conditional statement to define that when the app is running on Heroku. we connect to Postgres, and otherwise, we connect to Sqlite.

if 'DATABASE_URL' in os.environ:
   DATABASES = {
      'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
   }
else:
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
      }
   }
10. Install gunicorn which will act as the webserver, and put it on the requirements.txt.

pip3 install gunicorn
pip3 freeze > requirements.txt
Note: you don't have to do this if you've installed all dependencies in the requirements.txt file. 11. Create a Procfile, to tell Heroku to create a web dyno, which will run unicorn and serve the Django app.

11. Inside the Procfile:

web: gunicorn my_collections.wsgi:application
12. Login to Heroku through CLI, using heroku login. Once logged in, disable the collect static temporarily, so that Heroku won't try to collect static files when it deploys.
heroku config:set DISABLE_COLLECTSTATIC=1 
And add the hostname of the Heroku app to allowed hosts in the project's settings.py, and also add localhost so that Gitpod will still work as well:

ALLOWED_HOSTS = ['mycollections-379ea5dbbc8f.herokuapp.com', 'localhost']
13. Add, commit, and push to gitpod and then to Heroku. After pushing to gitpod as usual, initialize git remote first:
heroku git:remote -a shoes-and-more
Then push to Heroku:

git push heroku main
14. Go to the app's dashboard on Heroku and go to Deploy. Connect the app to Github by clicking Github and search for the repository. Click connect. Also enable the automatic deploy by clicking Enable Automatic Deploys, so that everytime we push to github, the code will automatically be deployed to Heroku as well.
15. Go back to settings.py and replace the secret key setting with the call to get it from the environment, and use empty string as a default.
SECRET_KEY = os.environ.get('SECRET_KEY', '')
Set debug to be true only if there's a variable called development in the environment.

DEBUG = 'DEVELOPMENT' in os.environ
## AWS Bucket Creation
All static and media files in this project are stored in [Amazon Web Services S3](https://aws.amazon.com/) bucket which is a cloud based storage service. You can create your own bucket by following these steps:

1. Go to [Amazon Web Service website](https://aws.amazon.com/) and click on Create An AWS Account, or login if you already have an account.

2. Login to your new account, go to AWS Management Console and find service S3. Click on Create Bucket.

- Give it a name (I recommend naming your bucket to match the Heroku app name), and choose region closest to you.
- In Object Ownership section, choose ACLS enabled. and Bucket Owner Preffered.
- Uncheck box 'Block All Public Access'.
- Check box 'I acknowledge that the current settings might result in this bucket and the objects within becoming public.'
- Click on Create Bucket, and your bucket is created.
3. Click on your newly created bucket, and navigate to the Properties tab. Scroll down to the bottom until you find Static Website Hosting. Click on Edit, then enable.

- Hosting type: choose Host a Static Website
- Index document: index.html
- Error document: error.html
- Click on Save Changes.
4. Navigate to the Permissions tab. Scroll down to the bottom until you find Cross-origin resource sharing (CORS). Click on Edit, and paste in this Cors Configuration below, which is going to set up the required access between the Heroku app and this S3 bucket. Click on Save Changes.

[
   {
      "AllowedHeaders": [
         "Authorization"
      ],
      "AllowedMethods": [
         "GET"
      ],
      "AllowedOrigins": [
         "*"
      ],
      "ExposeHeaders": []
   }
]
Still on the Permissions tab, find Bucket policy, click on Edit, and then go to Policy Generator.

- Select Type of Policy: choose S3 Bucket Policy
- Effect: choose Allow
- Principal: *
- Actions: select GetObject
- Fill in the Amazon Resource Name (ARN), from the Bucket ARN back in the Bucket Policy
- Click on the Add Statement and then Generate Policy. Copy the policy and paste in the bucket policy editor.
- Add a slash star on to the end of the resource key (because we want to allow access to all resources in this bucket). Click Save. The resource key should look like this
"Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*",  
Still on Permissions tab, go to Access Control List (ACL) section, click Edit and enable List for Everyone (public access), and accept the warning box.

5. With the bucket ready, now we need to create a user to access it through another service called IAM which stands for Identity and Access Management. Go back to the service menu and open IAM.
a. Create a group for our user to live in.
Click User Groups, and then create a new group with a name you want. I gave the group the name: manage-shoes-and-more. Scroll down to the bottom and click on Create Group.
b. Create an access policy giving the group access to the S3 bucket that has been created.

- Click on Policy, and then Create Policy. Go to the JSON tab, and then select import managed policy, which will let us import one that AWS has pre-built for full access to S3. Search for S3, then import the AmazonS3FullAccess policy.
- Because we only want to allow full access to our new bucket and everything within it, paste the bucket ARN (from the bucket policy page in s3) in the JSON editor.
"Resource": [
   "arn:aws:s3:::YOUR_BUCKET_NAME",
   "arn:aws:s3:::YOUR_BUCKET_NAME/*"
]
Now click on Next:Tags, then click Next:Review.

- Give the review policy a name and a description, then click Create Policy. The policy has now been created.
c. Finally, assign the user to the group so it can use the policy to access all our files.

- Go to User Groups, and select the group. Go to the Permissions tab, open the Add Permissions dropdown, and click Attach Policies.
- Select the policy and click Add permissions at the bottom.
- Create a user to put in the group, by going to the Users page, and clicking Add Users.
- Set a user name, give them access type: Programmatic access, and then click Next: Permissions.
- Check on the group that has the policy attached. Click Next: Tags, then click Next: Review, and lastly Create User.
- Download the csv file and save it.
## Connect Django to AWS Bucket
Note: If you've forked the repository, all of these steps are already done/ written on the files. Make sure you've installed all dependencies in the requirements.txt file, add all the AWS-related Config Vars to Heroku, and remove the DISABLE_COLLECTSTATIC variable from Heroku.
Here are the steps I took to connect Django to AWS:

1. Install two new packages: boto3 and django-storages. Freeze them into requirements.txt.

pip3 install boto3
pip3 install django-storages 
pip3 freeze > requirements.txt  
2. Add storages to the Installed Apps in settings.py.

3. In settings.py, we need to set cache control, set bucket configurations, set static and media files location, and override static and media URLs in production. We'll only want to do this on Heroku, so add an if statement as well.

if 'USE_AWS' in os.environ:
   ## Cache control
   AWS_S3_OBJECT_PARAMETERS = {
      'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
      'CacheControl': 'max-age=94608000',
   }

   ## Bucket Config
   AWS_STORAGE_BUCKET_NAME = 'YOUR_BUCKET_NAME'
   AWS_S3_REGION_NAME = 'YOUR_REGION'
   AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
   AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
   AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

   ## Static and media files
   STATICFILES_STORAGE = 'custom_storages.StaticStorage'
   STATICFILES_LOCATION = 'static'
   DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
   MEDIAFILES_LOCATION = 'media' 

   ## Override static and media URLs in production
   STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
   MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
Set the Config Vars on Heroku. On your app's dashboard on Heroku, go to Settings and click Reveal Convig Vars. Set this variables:

Variables	Value
AWS_ACCESS_KEY_ID	your access key id from the csv file that you've downloaded before
AWS_SECRET_ACCESS_KEY	your secret access key from the csv file that you've downloaded before
USE_AWS	True
Also remove the COLLECTSTATIC variable from the Config Vars.

4. We then want to tell Django that in production we want to use S3 to store our static files whenever someone runs collectstatic, and that we sent any uploaded images to go there as well.
Create a custom_storages.py file in your project's root directory, and inside it, include the Static and Media Storage locations:

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
   location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
   location = settings.MEDIAFILES_LOCATION
5. Finally, push these changes on Github.

git add .
git commit -m "Your commit message"
git push

- [Back To Top](#top)


##  Features

##  Core Features
- **Product Categories**: Clothing Essentials, Homeware, Special Offers.
- **Search Functionality**: Real-time product search using keywords.
- **User Authentication**: Register, login, and logout via **Django Allauth**.
- **Shopping Bag**: Add, update, and remove products with quantity management.
- **Stripe Integration**: Secure checkout and payment process.
- **Admin Panel**: CRUD operations for products, orders, and offers.

##  User Features
- Register / Log in / Log out
- Login success message.
- ![image](https://github.com/user-attachments/assets/bbcadf63-5f18-4f35-bb43-3675968969b0)

- Browse and search products
- Searching an empty bar

- ![image](https://github.com/user-attachments/assets/e12006ea-f970-4117-91df-7a6b62fde12a)

- Add items to shopping bag

- ![image](https://github.com/user-attachments/assets/7eed775d-c644-495d-a080-fccfec83da72)

- Update or remove items

- ![image](https://github.com/user-attachments/assets/5acfe8ee-d135-4b67-ac9e-1dcbcedb0371)
- ![image](https://github.com/user-attachments/assets/b2eec2f3-bee1-4644-a6c5-7728acc2bf5e)

- Proceed to secure checkout

- ![image](https://github.com/user-attachments/assets/62cac024-ef3a-491d-8df3-f532c07927b3)

- Receive email confirmation after payment
- Message sent confirmation on contact page.

- ![image](https://github.com/user-attachments/assets/7453d58a-f32c-430b-9ff9-a482371239e6)

## BUG
- There was a bug making the page to crash, but has been fixed.
- How it was fixed
- inspected the page
-  click on application then click on cookies
-  Under the cookies, click your url then clear.

## Languages Used
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
## Libraries and Frameworks
- [Django](https://www.djangoproject.com/) was used as web framework.

- [Django Template](https://jinja.palletsprojects.com/en/stable/) was used as a templating language for Django to display backend data to HTML.

- [Bootstrap 5](https://getbootstrap.com/) was used throughout the website to help with styling and responsiveness.

- [Google Fonts](https://fonts.google.com/) was used to import the font into the html file, and were used on all parts of the site.

- [Font Awesome](https://fontawesome.com/) was used throughout the website to add icons for aesthetic and UX purposes.

- [jQuery](https://jquery.com/) 3.6.0 was used as a JavaScript library to help writing less JavaScript code.

## Packages / Dependencies Installed
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication, registration, and account management.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Form was used to control the rendering of the forms.

- [Django Countries](https://pypi.org/project/django-countries/) was used to provide country choices for use with forms and a country field for models.

- [Pillow](https://pillow.readthedocs.io/en/stable/) was used to add image processing capabilities.

- [Gunicorn](https://gunicorn.org/) was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.

## Database Management
- [SQLite](https://sqlite.org/index.html) was used as a single-file database during development.

- [Heroku Postgres](https://www.heroku.com/postgres/) database was used in production, as a service based on PostgreSQL provided by Heroku.

## Payment Service
- [Stripe](https://stripe.com/en-nl) was used to process all online payments transactions.
## Cloud Storage
- [Amazon Web Service S3](https://aws.amazon.com/s3/) was used to store all static and media files in production.
## Tools and Programs
- [Git](https://git-scm.com/)

 - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://www.gitpod.io/)

 - GitPod was used for writing code, committing, and then pushing to GitHub.
- [GitHub](https://github.com/)
 - GitHub was used to store the projects code after being pushed from Git.

- [Heroku](https://www.heroku.com/)

 - Heroku was used to deploy the website.


- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used during development process for code review and to test responsiveness.
- [W3C Markup Validator](https://validator.w3.org/)

 - W3C Markup Validator was used to validate the HTML code.
W3C CSS Validator

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code.
- [JSHint](https://jshint.com/)

 - The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.
- [Favicon.io](https://favicon.io/) was used to create the site favicon.

- [Back To Top](#top)

## Technologies Used

| Area             | Technology                         |
|------------------|------------------------------------|
| Framework        | Django 4.2                          |
| Frontend         | HTML5, CSS3, JavaScript, Bootstrap |
| Backend          | Python 3.12                        |
| Authentication   | Django Allauth                    |
| Payments         | Stripe                             |
| Media Storage    | Aws3                         |
| Deployment       | Heroku                             |
| Environment Vars | dj-database-url                  |
| Database         | PostgreSQL (Production), SQLite (Dev) |

[Back To Top](#top)

## Installation Instructions

1. **Clone this repository**

bash
git clone https://github.com/Friday79/my_collections.git
cd my_collections
Create a virtual environment

bash
Kopiera
Redigera
python3 -m venv my_env
source my_env/bin/activate
Install dependencies

bash
Kopiera
Redigera
pip install -r requirements.txt
Set up environment variables

Create a .env file in the root:

env
Kopiera
Redigera
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_local_or_prod_database
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
STRIPE_PUBLIC_KEY=your_stripe_pub_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WH_SECRET=your_stripe_webhook_secret
Apply Migrations & Run Server

bash
Kopiera
Redigera
python manage.py migrate
python manage.py runserver
## Testing
To run tests:

bash
Kopiera
Redigera
python manage.py test
Testing includes:

-Model validations


Form submissions

Checkout flow

Bag logic

User auth flows

## Project Structure
- php
- Kopiera
- Redigera
- my_collections/

- │
- ├── bag/                # Shopping bag logic
- ├── checkout/           # Stripe integration
- ├── products/           # Products, categories, offers
- ├── profiles/           # User profiles & order history
- ├── templates/          # HTML templates
- ├── static/             # Static files (CSS, JS, images)
- ├── media/              # Uploaded images via Aws3
- ├── my_collections/     # Project settings and URLs
- ├── manage.py

## Admin Access
Superusers can:

Add/edit/delete products

View and manage orders

Manage categories and offers

Create a superuser:

bash
Kopiera
Redigera
python manage.py createsuperuser
Access admin at:

bash
Kopiera
Redigera
/admin/
## Deployment
Steps:
Push to GitHub

Connect to Heroku 

Set config vars as per .env

Add buildpacks for:

Python

Run migrations & collect static

bash
Kopiera
Redigera
python manage.py migrate
python manage.py collectstatic

## Product reviews and ratings
- python3 manage.py runserver
- on the nav bar click on product
- Then you can review and rate the product

## Code
- The code in Code Institute's video on the Boutique Ado project was used as the main reference point to set up an e-commerce / online store project using HTML, CSS, JS, Python+Django, PostgreSQL database, Stripe, and AWS S3 as storage.



## Acknowledgments
1. My mentor and the tutor team
2. Code Institute - for learning materials, guidance and walkthrough project. was helpful for this project
3. My partner, for her unconditional love, help and continued support through the whole course. Without you I wouldn't been able to make this happen.

- [Back To Top](#top)
