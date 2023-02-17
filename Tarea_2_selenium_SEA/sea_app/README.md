# Web scraping - SEA (Django + postgreSQL + Selenium)
Proyecto que realiza un web scraping a través de **Selenium** de la página del Sistema de Evaluación de Impacto Ambiental (https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php) para extraer datos de la tabla de proyectos. Los datos son convertidos en un json y se guardan en un modelo de base de datos de postgreSQL, los cuales son visualizados a través de una tabla en el navegador.

## :gear: Requerimientos
- Django
- PostgreSQL
- Selenium

## :memo: Instrucciones

- **Instalar Selenium y webdriver-manager** (*Ver sección documentación :open_book: *):
  ```
  pip install selenium
  pip install webdriver-manager
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

Selenium: https://selenium-python.readthedocs.io/
