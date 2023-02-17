# API Bike Santiago ( <img src="https://user-images.githubusercontent.com/66185308/219544687-7a92774b-c2bc-48cc-b9ff-efda4e7bf22a.png" width="80"> + <img src="https://user-images.githubusercontent.com/66185308/219544998-7c87fa3b-10e0-4ec1-bbf3-fdc52473a03d.png" width="80">  + <img src="https://user-images.githubusercontent.com/66185308/219545154-84a0c617-7ed1-4d7d-90fc-1ca6829732da.png" width="80"> )
Proyecto creado en el framework **Django**, que obtiene data de la API pública citybik - Bike Santiago (http://api.citybik.es/v2/networks/bikesantiago) con la biblioteca de Python **requests**, y la guarda en una base de datos de **postgreSQL** y la muestra en el navegador a través de una tabla.

## :gear: Requerimientos
- Django
- PostgreSQL
- Requests

## :memo: Instrucciones

- **Instalar Request** (*Ver sección documentación :open_book: *):
  ```
  python3 -m pip install requests
  ```


- **Crear BD y usuario en PostgreSQL**

  En consola, escribir lo siguiente para acceder a postgres:
  ```
  psql postgres
  ```
  Ingresar los siguientes comandos para crear base de datos y usuario con sus permisos:
  ```
  CREATE DATABASE myproject;
  CREATE USER myprojectuser WITH PASSWORD 'password';
  ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
  ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
  ALTER ROLE myprojectuser SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
  \q
  ```
- **Migraciones:**
  ```
  python3 manage.py makemigrations sea
  python3 manage.py migrate
  ```

- **Run project:** 
  ```
  python3 manage.py runserver
  ```
  Abrir navegador: http://127.0.0.1:8000/home/

## :open_book: Documentación
Django: https://www.djangoproject.com/start/overview/

PostgreSQL: https://www.postgresql.org/

Requests: https://requests.readthedocs.io/en/latest/
