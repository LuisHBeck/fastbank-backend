# FAST-BANK BACKEND

* ## Project Description 🌐
  RESTFUL API for a digital bank, demonstrating knowledge in backend development, HTTP protocols, authentication and authorization, REST design, MVC architecture and application of business rules

* ## Main Requirements 
  * Endpoints protected by JWT authentication;
  * Creating new users and accounts (Natural and Legal);
  * Apply for card and loans upon approval;
  * Allow transfers between existing accounts;
  * Allow installments of purchases;
  * Allow installments payment; 
  * Transaction history;

* ## Used Technologies 💻📚
  * Python 🐍
  * Django
    - Django REST Framework
    - Jazzmin
  * Insomnia

* ## Executing the project
  Setup the virtual environment
  ```ps
  py -m venv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
  ```
  Run the server and populate
  ```ps
  py populating.py
  ```
  This command does everything you need to prepare the django environment: 
    - makemigrations
    - migrate
    - runserver
    - create superuser
    - database population

* ## ENDPOINTS 🏁
  ### USERS

    ```ps
    /api/v1/auth/users/
    ```
    ```` POST METHOD ````

    ```json
    {
      "register_number": <int>,
      "picture": <str>,
      "password": <str>
    }
    ```

  ### JWT

    ```ps
    /api/v1/auth/jwt/create/
    ```

    ```` POST METHOD ````

    ```json
    {
      "register_number": <int>,
      "password": <str>
    }
    ```
    You need the {"access": token}

  ### NATURAL PEOPLE
    ```ps
    /api/v1/natural-people/
    ```
    ```` POST METHOD ````

    ```json
    {
      "user": <user_RN_fk>,
      "name": <str>,
      "birth_date": <yyyy-mm-dd>,
      "cpf": <str>,
      "rg": <str>,
      "social_name": <str>
    }
    ```

  ### LEGAL PEOPLE
    ```ps
    /api/v1/legal-people/
    ```
    ```` POST METHOD ````

    ```json
    {
      "user": <user_RN_fk>,
      "fantasy_name": <str>,
      "establishment_date": <yyyy-mm-dd>,
      "cnpj": <str>,
      "municipal_registration": <str>,
      "state_registration": <str>,
      "legal_nature": <str>
    }
    ```

  ### ADDRESSES
    ```ps
    /api/v1/addresses/
    ```
    ```` POST METHOD ````

    ```json
    {
      "user": <user_RN_fk>,
      "street": <str>,
      "number": <str>,
      "neighborhood": <str>,
      "city": <str>,
      "state": <str>,
      "cep": <str>
    }
    ```

  ### EMAILS
    ```ps
    /api/v1/emails/
    ```
    ```` POST METHOD ````

    ```json
    {
      "user": <user_RN_fk>,
      "email": <email>
    }
    ```

  ### PHONES
    ```ps
    /api/v1/phones/
    ```
    ```` POST METHOD ````

    ```json
    {
      "user": <user_RN_fk>,
      "area_code": <str>,
      "prefix_number": <str>,
      "phone_number": <str>
    }
    ```


