# 🛍️ My_Collections

**My_Collections** is a full-featured e-commerce platform built with Django. It offers a seamless shopping experience for users to browse and purchase **clothing essentials, homeware, and special offers**. The platform includes user registration with **Allauth**, a dynamic shopping bag system, **search functionality**, a secure **Stripe-powered checkout**, and an intuitive **admin dashboard** for managing products and orders.

---

## 🔗 Live Site

👉 [Deployed Site on Heroku](https://mycollections-379ea5dbbc8f.herokuapp.com/.com)

---

## 📸 Screenshots

*Add relevant screenshots here once deployed:*
- Home Page
- ![image](https://github.com/user-attachments/assets/5eb821da-d9d6-453d-a6ea-55671820b91f)

- Search Results
- ![image](https://github.com/user-attachments/assets/53ca0939-6c80-4bb1-94ed-93cf2bd5dd6a)

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


---

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

---

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
| Environment Vars | `dj-database-url`                  |
| Database         | PostgreSQL (Production), SQLite (Dev) |

---

## 🛠️ Installation Instructions

1. **Clone this repository**

```bash
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



🙌 Acknowledgments
1. Django Docs

2. Stripe

3. Cloudinary

4.Code Institute - for learning materials, guidance and walkthrough project.



