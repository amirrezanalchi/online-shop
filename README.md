Online Shop Project

This project is implemented in Python and serves as an online store application.

Entities
User: Represents a user of the system.
Store: Represents a store within the online platform.
Product: Represents a product available for sale.
Order: Represents an order placed by a user.
Order Item: Represents an individual item within an order.


Implemented Services: The project implements the following services:

User Registration
User Login
CRUD operations for Stores
CRUD operations for Products within each Store
Placing orders by users from available stores
The project is developed in a RESTful architecture. You can find a Postman collection file named online_shop.postman_collection.json in the repository for testing and interacting with the APIs.

Installation: To run the project locally, follow these steps:

1. Clone the repository:

2. Install dependencies:
    pip install -r requirements.txt

3. Run the application:
   python app.py

Make sure to configure any environment variables or database connections as specified in config.py or environment-specific configuration files.

API Documentation
For detailed API documentation, refer to the Postman collection file online_shop.postman_collection.json. 
Import this file into Postman to view and execute requests against the implemented endpoints.

