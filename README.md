# DRF-RESTAPI-server-with-auth

A simple REST API server for multiple user To-Do list with JWT authentication. Created with Django Rest Framework.
 
# Features
- multiuser system
    every user can only see/edit schedules date that created by their own.
    When user send a request to register new schedule, user id is extracted from request 
    and will be set to 'owner' field automatically.
    
- JWT Token Authentication
    Using djangorestframework-simplejwt package and djoser package
    
- Query filtering
    easy to get nessesary data. 
    e.g. access api/v1/schedules?date_from=2020-1-1&date_to=2020-1-3 to get only schedules between 
    specified days.  
 
# Requirement
 
* Python 3.6.5
 
Environments under venv is tested.
 
# Installation
 
Install required libraries.
 
```bash
pip install -r requirements.txt
```
 
# Usage

First, migrate database

```bash
python manage.py makemigrations
python manage.py migrate
```

Then, create super user.

```bash
python manage.py createsuperuser
```

Finally, run test server
```bash
python manage.py runserver
```
and api endpoint is available at localhost:8000/api/v1/

See localhost:8000/docs/ to check and test available api

Make sure access /api/v1/auth/jwt/ to get token and set it to header before access API.
You can see example HTTP requests on test.sh

Also, admin page on /admin is useful to manage users and schedules

# Note
 
tested Environment:
 - python 3.8.2
 - Manjaro Linux 20.0 x86_64

 
# Author
 
* hiro2620
 
# License
 
"DRF-RESTAPI-server-with-auth" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
 
It's good to create front app in the way you like.
Enjoy create your own to-do apps!

Thank you!