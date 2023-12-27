# Comercio Application

Comercio is an ecommerce application i built for the purpose of learning, developing and practicing my Devops skills.It was designed with microservice architecture. This is to ensure modulairty, scalability and improve realiablity.

## Overview
These are the components present in this project:

- [Product Service](./product_service/README.md): Handles product related functionalites.
- [User Service](./user_service/README.md): Handles user related functionalities like authentication and authorization

### To be added
- Order Service
- Frontend Service

## Prerequisite
- Docker: For containerizing and managing the microservices.
- Set required environmental variables for the databases. You can also do this by create `.env` file in the project root directory.

    For the User Service DB:

        - MYSQL_ROOT_PASSWORD
        - MYSQL_DATABASE
        - MYSQL_USER
        - MYSQL_PASSWORD

    For the Product Service DB:

        - POSTGRES_USER
        - POSTGRES_PASSWORD

## Installation

1. Clone the repostitory
```bash
git clone https://github.com/Priceless-P/comercio.git
```

2. Navigate to the root directory
3. Run `docker composer up` to start all service
    - user_service API will be accessible via: http://localhost:5001
    - product_service API will be accessible via: http://localhost:5002
