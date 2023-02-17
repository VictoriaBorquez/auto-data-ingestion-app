# Web scraping - SEA - SEIA (<img src="https://user-images.githubusercontent.com/66185308/219544687-7a92774b-c2bc-48cc-b9ff-efda4e7bf22a.png" width="80"> + <img src="https://user-images.githubusercontent.com/66185308/219544998-7c87fa3b-10e0-4ec1-bbf3-fdc52473a03d.png" width="80">  +  <img src="https://user-images.githubusercontent.com/66185308/219648943-7c47db95-aecb-443f-a6ed-48da61e863e8.png" width="120"> )

Proyecto creado en el framework **Django**, que realiza un web scraping a través de **Selenium** de la página del Sistema de Evaluación de Impacto Ambiental (https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php) para extraer datos de la tabla de proyectos. Los datos son convertidos en un json y se guardan en un modelo de base de datos de **postgreSQL**, los cuales son visualizados a través de una tabla en el navegador.

## :gear: Requerimientos
- Django
- PostgreSQL
- Selenium

## :memo: Instrucciones

- **Clonar repositorio**:

  ```
  git clone https://github.com/VictoriaBorquez/auto-data-ingestion-app.git
  ```
  
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

:warning: **Dada la cantidad de datos que tiene la tabla (>2000 registros), se extraen los primeros 10 registros, para modificar esto ver línea 27 del archivo views.py**

## :open_book: Documentación
Django: https://www.djangoproject.com/start/overview/

PostgreSQL: https://www.postgresql.org/

Selenium: https://selenium-python.readthedocs.io/
