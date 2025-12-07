# 🛒 UrbanCart — Django E-commerce (Minor Project)

UrbanCart is a Django-based e-commerce website built as a Minor Project for MCA 3rd semester.  
This project will be extended and upgraded into a full Major Project in the next semester.

---

## ✨ Features Implemented (Till Now)

### ✔️ Django Project Setup
- Virtual environment created using `venv`
- Django installed with Python 
<!-- - Pillow installed for image support -->
<!-- - `.gitignore` added to ignore venv/media/migrations -->

### ✔️ Models
- `Product` model (name, price, image, stock, description)
- `OrderRequest` model (temporary order system for Minor project)
- `Category` model (product category filtering)

### ✔️ Admin Panel
- Product, Category, OrderRequest registered
- Custom admin list view with filters & search
- Images uploading working via Django admin

### ✔️ Media & Static Configuration
- Configured `MEDIA_URL` and `MEDIA_ROOT`
- Product images now load correctly in the frontend

### ✔️ Tailwind CSS Integration
<!-- - Removed Bootstrap -->
- Tailwind added for clean UI styling
- Responsive card layout for products

### ✔️ Product Listing Page
- Grid UI (1–4 columns responsive)
- Category badge display
- “Buy Now” button on each product

### ✔️ Product Detail Page
- Individual product view
- Order Request form (Name / Phone / Address)
- Backend saves order to database

### ✔️ Search + Filter System
- Search products by name
- Filter by category
- Price filter (min/max)
- Sorting (Low to High / High to Low)
- Query parameters preserved in pagination

### ✔️ Pagination
- Previous / Next navigation
- Works with filters and sorting
- Supports large product lists

---

## 📦 Tech Stack

### Backend
- Python 3.12
- Django 4.2

### Frontend
- Tailwind CSS
- HTML + Django Templates

### Database
- SQLite3 (Minor project)
<!-- - Will upgrade to PostgreSQL in Major project -->

---

## 📁 Project Structure (Important Folders)

urbancart/
│
├── store/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/store/*.html
│
├── media/products/ ← product images
├── templates/ ← base.html
├── static/ ← tailwind assets
├── requirements.txt
└── README.md


---
<!-- 
## 🚀 Roadmap (Future Work – Major Project Features)

### 🔐 Authentication (Next Step)
- User registration
- Login / Logout
- Profile dashboard
- View order history

### 🛒 Real Cart System
- Add to cart
- Update quantity
- Remove item
- Cart total calculation

### 💳 Payment Integration (Major project)
- Razorpay / Stripe / PayPal

### 🛍️ Full Order System
- Order table (proper)
- Order status (Pending / Processing / Dispatched / Delivered)
- Email notification

### ⭐ Product Management
- Product wishlist
- Product reviews & ratings

### 📦 Category & Filtering Enhancements
- Multiple category filtering
- Price sliders
- Sorting by newest, relevance

### 🌐 Deployment
- Deploy on Render / Railway / PythonAnywhere
- Use PostgreSQL database
- Static + media hosting

---

## 🧪 Testing (Planned)
- Unit tests for views & models
- Form validation tests
- Admin regression testing

--- -->

<!-- ## 📄 License
Open Source — free to use for educational purposes. -->

---

## 👨‍💻 Author
**Siddharth Sundram**  
Project: **UrbanCart — E-commerce Website**
