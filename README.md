# Questimate

Investing for Everyone

## Installation

### A). Build on Your Local Machine :
#### Steps:
1. Add `media`Directory:  
    ```bash
     mkdir media
   ```
2. Add `.env`:  
    ```bash
     touch sterling_square/.env
   ```
    ```bash
     nano sterling_square/.env
   ```
   paste following:
    ```bash
     DB_NAME="<db name>"
     DB_USER="<db username>"
     DB_PASS="<db password>"
     DB_HOST="<db host>"
     DB_PORT="<db port>"
     BASE_URL="<base url of the application>"
     CHROME_DRIVER="Headless Chrome Driver Path/URL"
     CACHE_LOCATION="/var/run/redis/redis-server.sock"
     STERLING_SQUARE_API_KEY="Zerodha Account API Key"
     STERLING_SQUARE_API_SECRET="Zerodha Account Secret Key"
     STERLING_SQUARE_USER_ID="Zerodha Account USER ID"
     STERLING_SQUARE_PASS="Zerodha Account Password"
     STERLING_SQUARE_PIN="Zerodha Account PIN"
     FINANCIAL_MODEL_GRP_API_KEY="API key for Financial Model Group API key"
     EOD_HISTORICAL_DATA_API_KEY="API key for EOD Historical Data API key"
   ```
3. Run:  
    ```bash
     docker-compose up --build -d
   ```
4. Run Migrations:  
    ```bash
     docker exec -it django python3 manage.py makemigrations
   ```
   ```bash
     docker exec -it django python3 manage.py migrate
   ```
5. Update Credentials:
    ```bash
     docker exec -it django python3 manage.py resync_creds
   ```
6. Load Symbols:
    ```bash
     docker exec -it django python3 manage.py load_symbols
   ```
7. Update Company Information:
    ```bash
     docker exec -it django python3 manage.py get_company_info
   ```
8. Update holidays:
    ```bash
     docker exec -it django python3 manage.py get_holidays
   ```


### B). Build on Your Production Server :
#### Steps:
1. Add `media`Directory:  
    ```bash
     mkdir media
   ```
2. Add `.env`:  
    ```bash
     touch sterling_square/.env
   ```
    ```bash
     nano sterling_square/.env
   ```
   paste following:
    ```bash
     DB_NAME="<db name>"
     DB_USER="<db username>"
     DB_PASS="<db password>"
     DB_HOST="<db host>"
     DB_PORT="<db port>"
     BASE_URL="<base url of the application>"
     CHROME_DRIVER="Headless Chrome Driver Path/URL"
     CACHE_LOCATION="/var/run/redis/redis-server.sock"
     STERLING_SQUARE_API_KEY="Zerodha Account API Key"
     STERLING_SQUARE_API_SECRET="Zerodha Account Secret Key"
     STERLING_SQUARE_USER_ID="Zerodha Account USER ID"
     STERLING_SQUARE_PASS="Zerodha Account Password"
     STERLING_SQUARE_PIN="Zerodha Account PIN"
     FINANCIAL_MODEL_GRP_API_KEY="API key for Financial Model Group API key"
     EOD_HISTORICAL_DATA_API_KEY="API key for EOD Historical Data API key"
   ```
3. Run:  
    ```bash
     docker-compose -f docker-compose-deploy.yml up --build -d
   ```
4. Run Migrations:  
    ```bash
     docker exec -it django1 python3 manage.py makemigrations
   ```
    ```bash
     docker exec -it django1 python3 manage.py migrate
   ```
5. Update Credentials:
    ```bash
     docker exec -it django1 python3 manage.py resync_creds
   ```
6. Load Symbols :
    ```bash
     docker exec -it django1 python3 manage.py load_symbols
   ```
7. Update Company Information:
    ```bash
     docker exec -it django1 python3 manage.py get_company_info
   ```
8. Update holidays:
    ```bash
     docker exec -it django1 python3 manage.py get_holidays
   ```
9. Run Background Script: 

   Install dependencies:
    ```bash
     pip3 install schedule==1.1.0
   ```
   Run Script:
    ```bash
     python3 bg_script.py
   ```
   
## Important Instructions:
* Add Buying Power: 

   * On Local Machine:
        ```bash
         docker exec -it django python3 manage.py add_money
       ```
   * On Server:
        ```bash
         docker exec -it django1 python3 manage.py add_money
       ```
       OR
   * By API:
        ```bash
         /accounts/buyingpower/
       ```
* Restart Containers:
    ```bash
     docker restart $(docker ps -q)
   ```
     OR
    ```bash
     docker restart $(docker ps -a -q)
   ```
* Ports:
    Service      | Port
    -----------  | -------------
    Niginx       | 80
    Database     | 8080
    Flower       | 8888
    Django       | 8000
    Daphne       | 9000
    Selenium     | 4444
    Redis        | 6379
    Postgres     | 5432

## Contributing


## License