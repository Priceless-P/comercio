# Product Service
This is designed to a scalable and efficient in managing all product related functionalites within a larger system such as comercio application or as a standalone project. important component of . It provides an API for creating, retrieving and deleying products.

## Technologies used

- Python Flask Famework
- PostgresSQL Database
- Flask-SQLAlchemy ORM
- Docker

## Features
- Create Product: Add new product with fields such as name, price, slug and image.
- Retrieve Product: Fetch all products or one using its `slug`
- Delete Product: Delete product using product `slug`
- Prometheus Monitoring: Prometheus client integration allows the microservice to expose metrics, providing a way to monitor the service health, performance resulting better observabilty and troubleshooting
- Dockerization: [DockerFile](./Dockerfile) and [docker-compose](./docker-compose.yml) handles encapsulation of the microservice and its dependencies, this ensures consisten deployment across different environment and reduces errors.
- API Documentation is done with Swagger


## Requirements
- Python 3.x
- Docker

## Installation and Usage
0. Set up environment variables
    - Create `.env` file
    - Set the following variable
        - ENVIRONMENT_CONFIGURATION='config.DevelopmentConfig' or 'config.ProductionConfig' depending if its a devlopment or production environment
        - DEV_DATABASE_URL='postgresql://username:password@host/dbname'
        - PROD_DATABASE_URL='postgresql://username:password@host.docker.internal/dbname'
        I am using localhost ad dev environment and docker as prod environment
        
1. Clone the repostitory
```bash
git clone https://github.com/Priceless-P/comercio.git
```

2. Navigate to the product directory
```bash
cd comercio/product_service
```

3. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run the microservice
```bash
flask run
```