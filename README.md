# real-estate
Project developed as a technical challenge for the position of Software Developer.

- Install the necessary packages:

``` pip install -r requirements.txt ```

- Create the migrations to run on the Database:

``` python manage.py makemigrations ```

- Run the changes:

``` python manage.py migrate ```

- Create a superuser:

``` python manage.py createsuperuser ```

- Running the application:

``` python manage.py runserver ```

The application has authentication requirements associated with the username and password created when running the previous command (createsuperuser).

- Recommended website for CPF field validation: https://bit.ly/3FdAUW2

Use dates in the following format: month/day/year

