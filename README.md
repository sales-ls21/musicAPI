#Installation Instructions

1. If you don't have Python version 2.7, 3.2, 3.3, 3.4, or 3.5: install the latest version of Python
2. If you don't have Django version 1.8, 1.9 or 1.10: install the latest version of Django.
3. Run git clone git@github.com:sales-ls21/musicAPI.git in a folder where you'd like to keep this project.
4. Run cd musicAPI to navigate into the created directory.
5. Run python manage.py makemigrations to build the needed database.
6. Run python manage.py migrate.
7. Run python manage.py runserver to start the Django server.
8. Navigate to http://localhost:8080 to view the API resources.

#How to Use The API

1.Follow the steps above to run this app locally. Since this is a RESTful API, you can go to the root URL (http://localhost:8000/) to see all resources available and which methods can be used on each resource.

2. You can access the admin interface at http://localhost:8080/admin.
