# CampusSwap

CampusSwap is a dynamic online marketplace built with Vue.js for the frontend and Django for the backend, designed to facilitate the buying and selling of used goods among students. It aims to provide a convenient and competitive platform for students to trade their items.

[![Vue Version](https://img.shields.io/badge/Vue-3.3.11-brightgreen)](https://vuejs.org/)
[![Django Version](https://img.shields.io/badge/Django-5.0.1-orange)](https://www.djangoproject.com/)

## Features

- **User Authentication:** Secure registration and login system for students.
- **Product Listings:** Users can list items for sale with detailed descriptions, categories, pricing, and images.
- **Resource Catalog:** A section for students to share and access academic resources, study materials, and notes.
- **Admin Dashboard:** Dedicated interface for administrators to manage listings, resources, and users.
- **Approval Workflow:** Listings and resources require admin approval before becoming visible to other users.
- **User Management:** Admins can view user information and ban/deactivate users.
- **Search and Filtering:** Users can search for items and filter results based on various criteria like year, branch, type, and condition.
- **Payment Integration:** Integrated Razorpay for secure online transactions.
- **User Profiles:** Personalized settings pages to view and manage listings, resources, starred items, and purchases.
- **Image Uploads:** Seamless image uploading for product listings via ImgBB integration.
- **Markdown Editor:** A rich text editor for creating and editing resource descriptions.

### Key Actions

- **Register:** Create a new student account using your Moodle ID and email.
- **Login:** Access your account with your Moodle ID and password.
- **Buy:** Browse available listings, apply filters, and search for items.
- **Sell:** List items for sale, including details, images, and pricing.
- **Resources:** Access and contribute academic resources.
- **Admin Dashboard:** Manage unapproved listings, resources, and users.

## Tech Stack

- **Frontend:** Vue.js, Vue Router, Vuex, PrimeVue, Axios, Vite
- **Backend:** Django, Django-CORS-Headers, PostgreSQL
- **Languages:** JavaScript, Python, HTML, CSS
- **APIs:** ImgBB API, Razorpay API

## Setup

- Check out `SETUP.md`

## API Reference

- **Auth APIs (`apis/urls.py`):**
  - `/apis/register`: Handles user registration.
  - `/apis/login`: Handles user login.
  - `/apis/logout`: Handles user logout.
  - `/apis/reset_password`: Handles password reset.
  - `/apis/get_phone/<int:moodleID>`: Retrieves user phone number.

- **Product APIs (`products/urls.py`):**
  - `/products/image_url_gen`: Uploads product images.
  - `/products/upload_listing`: Creates a new product listing.
  - `/products/update_listing`: Updates an existing product listing.
  - `/products/get_resource/<int:resourceId>`: Retrieves a specific resource.
  - `/products/user_listings_and_resources/<int:moodleID>`: Gets user's listings and resources.
  - `/products/all_approved_listings`: Fetches all approved product listings.
  - `/products/all_approved_resources`: Fetches all approved resources.
  - `/products/upload_resource`: Creates a new resource listing.
  - `/products/update_resource`: Updates an existing resource listing.
  - `/products/add_star`: Adds/removes a star from a resource.
  - `/products/user_starred_resources/<int:moodleID>`: Fetches resources starred by a user.
  - `/products/simple_search`: Performs a basic search for listings.

- **Admin Action APIs (`admin_actions/urls.py`):**
  - `/admin_actions/get_unapproved_listings_and_resources`: Fetches unapproved items.
  - `/admin_actions/grant_approval`: Grants approval for a listing/resource.
  - `/admin_actions/send_negative_feedback`: Sends feedback for denied items.
  - `/admin_actions/get_negative_feedback/<int:product_id>`: Retrieves negative feedback for a product.
  - `/admin_actions/grant_approval_resource`: Grants approval for a resource.
  - `/admin_actions/send_negative_feedback_resource`: Sends feedback for denied resources.
  - `/admin_actions/get_negative_feedback_resource/<int:resource_id>`: Retrieves negative feedback for a resource.
  - `/admin_actions/get_all_users`: Fetches all active users.
  - `/admin_actions/delete_user`: Deactivates/bans a user.
  - `/admin_actions/get_user_info/<int:moodleID>`: Retrieves information about a user.

- **Payment APIs (`payments/urls.py`):**
  - `/payments/create_order`: Creates a payment order.
  - `/payments/record_payment`: Records payment details after successful transaction.
  - `/payments/get_purchases/<int:moodleID>`: Fetches purchase history for a user.
