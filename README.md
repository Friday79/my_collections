
**My_Collections** is a full-featured e-commerce platform built with Django. It offers a seamless shopping experience for users to browse and purchase **clothing essentials, homeware, and special offers**. The platform includes user registration with **Allauth**, a dynamic shopping bag system, **search functionality**, a secure **Stripe-powered checkout**, and an intuitive **admin dashboard** for managing products and orders.
To Navigate the site, on the  **Homepage** top left corner, when you click **mycollections Logo** it will take you back to the homepage . Next on the right side of mycollections logo is the **Search functionality**, that we can use to search for product. Next to that is the **Account registration**,where we can **register** and create a **profile** and can **logout** of the page or **login** when the account is clicked. As an **Admin user**, you can **login as superuser**, by typing **python3 manage.py createsuperuser**, then fill in your **Username** ,**Email** and **Password** in the terminal.Then navigate to **Admin board** , there you can manage product by **Updating, Editing,Creating and Deleting**.
At the Nav we have all product ,that when we click , we can choose the product we want by **price, rating, category**. Next is **Clothing**, when clicked, we can select the category of clothe we want. Next is **Homeware**,when clicked, we can select the one we want from the list.Next is **Special offer**, when clicked we can also select what we want from the list. At the top right corner of the home page is the **Bag icon** that when clicked we can can see the products we have selected, and the total cost.
There is a shop now link that when clicked, it will take us to the store. If any product is clicked, then in the product details, we can **review, select seize,rate, increase quantity** with the increment and decrement button. At the bottom of the product detail page we click on add to bag, to add the product to bag and click on keep shopping to continue shopping. 
In the bag we will see all the product we have added to the bag,then we can edit or delete product before we click on checkout at the bottom of the page, which then take us to the payment section,where we will fill in our shipping information and make payment, then **Receive Email Comfirmation** after payment.

**IMPORTANT COMMENT**
- Database_url code was in settings.py which was destrimental to this project but have been remove from settings.py


---

## 🔗 Live Site

👉 [Deployed Site on Heroku](https://mycollections-379ea5dbbc8f.herokuapp.com/)

---

## 📸 Screenshots

- Home Page
- ![image](https://github.com/user-attachments/assets/5eb821da-d9d6-453d-a6ea-55671820b91f)

- Search Results
- ![image](https://github.com/user-attachments/assets/0d0424a8-c238-46e1-856e-ddef0b788f2d)


- Product Detail
- ![image](https://github.com/user-attachments/assets/894b40c2-11b1-4e28-a499-ffe55a1bf600)



- Shopping Bag
- ![image](https://github.com/user-attachments/assets/5f2ebd43-e33f-44ca-b2ce-ff851fb07540)

- Stripe Checkout
- ![image](https://github.com/user-attachments/assets/bee01ffd-5d4d-4272-a785-c0b2c6ad1e5f)

- Admin Dashboard
- ![image](https://github.com/user-attachments/assets/15bd0a0f-0ad8-4b08-b531-c1298f40af09)

- ## Css Testing


- ![Image](https://github.com/user-attachments/assets/e9d64aa4-dfaf-4c3d-9009-39117bb5eb82)

- ## Checkout Css Testing
- ![image](https://github.com/user-attachments/assets/d4d3ef33-d297-496b-b481-94de9a7bd405)

## SOCIAL MEDIA MARKETING

- - ##  Newsletter Signup with Mailchimp For Email Marketing
- ![image](https://github.com/user-attachments/assets/baa7dac9-af9a-4b91-bcef-d317ac775e5a)


- ## Facebook Business Marketing page For B2C
- ![image](https://github.com/user-attachments/assets/de385d74-5cf2-475c-b8f8-45b5b62e6fe3)

- ## FLOWCHART
- ![image](https://github.com/user-attachments/assets/def88c09-bbec-4060-b7ea-75c5ca940305)

- ## Agile method
- ![image](https://github.com/user-attachments/assets/490dc086-d1f8-41c0-b267-3658019c60b7)
- ![image](https://github.com/user-attachments/assets/a97ea7fb-7c66-4159-aa58-ac3f52c0a43b)
- ![image](https://github.com/user-attachments/assets/63bce6f9-04a9-41db-ae70-13e6d5702633)
- ![image](https://github.com/user-attachments/assets/6de86413-99a5-4197-8704-b85d3a2fda01)
- ![image](https://github.com/user-attachments/assets/7419daaa-d4c0-4a2b-a5f8-0c4106dd96d1)
- ![image](https://github.com/user-attachments/assets/7da69a55-4f2c-42ee-80c2-524818c46f7c)
- ![image](https://github.com/user-attachments/assets/124726d3-ae09-4f7d-ab0d-a73d99ce2405)







- ## jshint Stripe testing
- ![image](https://github.com/user-attachments/assets/3a8d6440-bd57-4573-a629-d17acc032cb9)

- ## Coverage Report BAG
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
---------------------------------------------------------
profiles/__init__.py                      0      0   100%
profiles/admin.py                         1      0   100%
profiles/apps.py                          4      0   100%
profiles/forms.py                        18      1    94%
profiles/migrations/0001_initial.py       8      0   100%
profiles/migrations/__init__.py           0      0   100%
profiles/models.py                       21      0   100%
profiles/test_forms.py                   23      0   100%
profiles/test_models.py                  13      0   100%
profiles/test_views.py                   33      0   100%
profiles/tests.py                         1      0   100%
profiles/urls.py                          3      0   100%
profiles/views.py                        25      0   100%


## 🚀 Features

### 🌟 Core Features
- **Product Categories**: Clothing Essentials, Homeware, Special Offers.
- **Search Functionality**: Real-time product search using keywords.
- **User Authentication**: Register, login, and logout via **Django Allauth**.
- **Shopping Bag**: Add, update, and remove products with quantity management.
- **Stripe Integration**: Secure checkout and payment process.
- **Admin Panel**: CRUD operations for products, orders, and offers.

### 👤 User Features
- Register / Log in / Log out
- Browse and search products
- Add items to shopping bag
- Update or remove items
- Proceed to secure checkout
- Receive email confirmation after payment

## BUG
- There was a bug making the page to crash, but has been fixed.
- How it was fixed
- inspected the page
-  click on application then click on cookies
-  Under the cookies, click your url then clear.

## ⚙️ Technologies Used

| Area             | Technology                         |
|------------------|------------------------------------|
| Framework        | Django<4                          |
| Frontend         | HTML5, CSS3, JavaScript, Bootstrap |
| Backend          | Python 3.12                        |
| Authentication   | Django Allauth                    |
| Payments         | Stripe                             |
| Media Storage    | Cloudinary                         |
| Deployment       | Heroku                             |
| Environment Vars | dj-database-url                  |
| Database         | PostgreSQL (Production), SQLite (Dev) |

---

## 🛠️ Installation Instructions

1. **Clone this repository**

bash
git clone https://github.com/yourusername/my_collections.git
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
🧪 Testing
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

🗂️ Project Structure
php
Kopiera
Redigera
my_collections/
│
├── bag/                # Shopping bag logic
├── checkout/           # Stripe integration
├── products/           # Products, categories, offers
├── profiles/           # User profiles & order history
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # Uploaded images via Cloudinary
├── my_collections/     # Project settings and URLs
├── manage.py
🧑‍💻 Admin Access
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
🌐 Deployment
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

Product reviews and ratings
- python3 manage.py runserver
- on the nav bar click on product
- Then you can review and rate the product



🙌 Acknowledgments
1. My mentor and the tutor team

2.Code Institute - for learning materials, guidance and walkthrough project.


