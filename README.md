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
  * Setup the virtual environment
    - ```ps
        py -m venv .venv
        .venv\Scripts\activate
        pip install -r requirements.txt
      ```
  * Run the server and populate
    - ```ps
      py populating.py
      ```
      This command does everything you need to prepare the django environment
        - Execute: 
          * makemigrations
          * migrate
          * runserver
          * create superuser
          * database population