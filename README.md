# FAST-BANK BACKEND

## Project Description 🌐
  RESTFUL API for a digital bank, demonstrating knowledge in backend development, HTTP protocols, authentication and authorization, REST design, MVC architecture and application of business rules

## Main Requirements 
  * Endpoints protected by JWT authentication;
  * Creating new users and accounts (Natural and Legal);
  * Apply for card and loans upon approval;
  * Allow transfers between existing accounts;
  * Allow installments of purchases;
  * Allow installments payment; 
  * Transaction history;

## Used Technologies 💻📚
  * Python 🐍
  * Django
    - Django REST Framework
    - Djoser
    - Jazzmin
  * Insomnia

## Executing the project
  Setup the virtual environment
  ```ps
  py -m venv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
  ```
  Setup the environment variables according to .env.examples
  ```ps
  IP = ''
  PORT = ''
  SECRET_KEY = '' 
  ```
  Run the command below to generate de Django Secret Key
  ```ps
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
  Run the server and populate
  ```ps
  py client.py
  ```
  This command does everything you need to prepare the django environment: 
    - makemigrations
    - migrate
    - runserver
    - create superuser
    - database population

## ENDPOINTS 🏁
  If endpoint has ```authorization=True``` use {"Authorization": "Bearer <jwt_access>"}
### USERS
  ``` authorization=False ```
  ```ps
  /api/v1/auth/users/
  ```
  ```` POST METHOD ````

  ```json
  {
    "register_number": <int>,
    "picture": "<str>",
    "password": "<str>"
  }
  ```

### JWT
``` authorization=False ```
  ```ps
  /api/v1/auth/jwt/create/
  ```

  ```` POST METHOD ````

  ```json
  {
    "register_number": <int>,
    "password": "<str>"
  }
  ```
  ``` RETRUN EXAMPLE ```
  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
  }
  ```
  You need the {"access": "jwt"}

### NATURAL PEOPLE
``` authorization=True ```
  ```ps
  /api/v1/natural-people/
  ```
  ```` POST METHOD ````

  ```json
  {
    "user": <user_RN_fk>,
    "name": "<str>",
    "birth_date": "<yyyy-mm-dd>",
    "cpf": "<str>",
    "rg": "<str>",
    "social_name": "<str>"
  }
  ```

### LEGAL PEOPLE
``` authorization=True ```
  ```ps
  /api/v1/legal-people/
  ```
  ```` POST METHOD ````

  ```json
  {
    "user": <user_RN_fk>,
    "fantasy_name": "<str>",
    "establishment_date": "<yyyy-mm-dd>",
    "cnpj": "<str>",
    "municipal_registration": "<str>",
    "state_registration": "<str>",
    "legal_nature": "<str>"
  }
  ```

### ADDRESSES
``` authorization=True ```
  ```ps
  /api/v1/addresses/
  ```
  ```` POST METHOD ````

  ```json
  {
    "user": <user_RN_fk>,
    "street": "<str>",
    "number": "<str>",
    "neighborhood": "<str>",
    "city": "<str>",
    "state": "<str>",
    "cep": "<str>"
  }
  ```

### EMAILS
``` authorization=True ```
  ```ps
  /api/v1/emails/
  ```
  ```` POST METHOD ````

  ```json
  {
    "user": <user_RN_fk>,
    "email": "<email>"
  }
  ```

### PHONES
``` authorization=True ```
  ```ps
  /api/v1/phones/
  ```
  ```` POST METHOD ````

  ```json
  {
    "user": <user_RN_fk>,
    "area_code": "<str>",
    "prefix_number": "<str>",
    "phone_number": "<str>"
  }
  ```

### ACCOUNTS
``` authorization=True ```
```ps
/api/v1/accounts/
```
```` POST METHOD ````

```json
{
  "type": "<str>"
}
```
The value for "type" needs to be "Savings" or "Current"

```` GET METHOD ````
```json
{
    "user": [
      654321
    ],
    "agency": 1,
    "number": 1112,
    "type": "Current",
    "balance": "275.25",
    "credit_limit": "500.00",
    "is_active": true
}
```


### INVESTMENTS
``` authorization=True ```
```ps
/api/v1/investments/
```
```` POST METHOD ````

```json
{
  "type": "<str>",
  "contribution": <float>,
  "admin_fee": <float>,
  "period": "<yyyy-mm-dd>", 
  "risc_rate": <float>,
  "profitability": <float>,
  "is_active": <boolean>
}
```

```` GET METHOD ````
```json
{
  "id": 1,
  "type": "LCA",
  "contribution": "135.25",
  "admin_fee": "1.50",
  "period": "2030-12-11",
  "risc_rate": "2.30",
  "profitability": "15.60",
  "is_active": true
}
```

### ACCOUNTS INVESTMENTS
``` authorization=True ```
```ps
/api/v1/investments/account/new/
```
```` POST METHOD ````

```json
{
  "id_account": <account_fk>,
  "id_investment": <investment_fk>
}
```

```` GET METHOD ```` 

For GET Method need to pass the query parameter "?account=<account_number>"
```json
{
  "id_account": 1111,
  "id_investment": 1
}
```

### INSTALLMENTS
``` authorization=True ```

```` GET METHOD ```` 

GET all installments

For GET Method need to pass the query parameter "?account=<account_number>"
```json
{
  "id": 1,
  "id_account": 1111,
  "number": "1",
  "expiration_date": "2023-10-18",
  "payment_date": null,
  "payment_amount": "419.53",
  "paid": false
}
```

GET installment final amount

For GET Method need to pass the query parameter "?account=<account_number>&final=true"
```json
{
  "Installment final amount": 927.45
}
```

### CARDS
``` authorization=True ```
```ps
/api/v1/cards/
```
```` POST METHOD ````

```json
{
  "id_account": <account_fk>,
}
```


```` GET METHOD ```` 

For GET Method need to pass the query parameter "?account=<account_number>"
```json
{
  "id_account": 1111,
  "number": "570054397143",
  "expiration_date": "2027-06-22",
  "flag": "Mastercard",
  "verification_code": "843",
  "is_active": true
}
```

### CARDS TRANSACTIONS
``` authorization=True ```
```ps
/api/v1/card-transactions/
```
```` POST METHOD ````

```json
{
  "id_account": <account_fk>,
  "id_card": <card_fk>,
  "operation": <str>,
  "amount": <float>
}
```

### LOANS
``` authorization=True ```
```ps
/api/v1/loans/
```
```` POST METHOD ````

```json
{
  "id_account": <account_fk>,
  "amount_request": <float>,
  "installment_amount": <int>,
  "observation": <str>
}
```

```` GET METHOD ```` 

For GET Method need to pass the query parameter "?account=<account_number>"
```json
{
  "id_account": 1111,
  "request_date": "2023-10-11",
  "amount_request": "1459.25",
  "interest_rate": "15.00",
  "installment_amount": 4,
  "observation": "personal use"
}
```

### PIX
``` authorization=True ```
```ps
/api/v1/pix/
```
```` POST METHOD ````

```json
{
  "id_account": <account_fk>,
  "id_receiver_account": <account_fk>
  "amount": <float> 
}
