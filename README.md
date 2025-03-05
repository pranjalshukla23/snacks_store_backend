# MyStore API

Welcome to the MyStore API! This API allows you to manage products and handle shopping cart operations like adding products to the cart.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
  - [Add Product](#apiadd_product)
  - [Add to Cart](#apiadd_to_cart)
- [Testing the APIs](#testing-the-apis)

## Requirements

To run this project, you'll need:

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- SQLite or another database engine (SQLite is used by default)

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/pranjalshukla23/snacks_store_backend
    cd snacks_store_backend
    ```

2. **Set up a virtual environment**:
    - For Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional)**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

    Your project will now be running at `http://127.0.0.1:8000/`.

## Running the Project

To run the project locally, follow the steps above for setting up and activating the environment. Then use the Django development server to run it.

1. **Start the Django development server**:
    ```bash
    python manage.py runserver
    ```

    The API will be available at `http://127.0.0.1:8000/`.

2. You can now test the APIs.

## API Endpoints

### Add Product (`/api/add-product/`)

This endpoint allows you to add a new product to the store database.

**Method**: `POST`

**Request Body**:
```json
{
  "product_code": "GR1",
  "name": "Green Tea",
  "price": 5.00
}

### Get All Products (`/api/products/`)

This endpoint allows you to get all the products from the database.

**Method**: `GET`

### Add Product To Cart (`/api/add-to-cart/`)

This endpoint allows you to add a new product to the shopping cart and get the updated final price and quantities added in the cart.

**Method**: `POST`

**Request Body**:
```json
{
  "products": [
    {
      "product_code": "GR1",
      "quantity": 1
    }   
  ]
}


