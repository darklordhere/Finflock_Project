## Overview

# Django REST Project with CRUD Operations containing 2 tables with primary key and foreign key relationship. In Addition Filter by Name and Date.

## Setup and Running the Project

- Clone the repo
>> git clone repo_link

- Create VirtualEnv and cd main folder
>> python -m venv venv
>> venv\Scripts\activate

- Install django, djangorestframework and django-filter

- Apply migrations
>> python manage.py makemigrations
>> python manage.py migrate

- Create a SuperUser or Directly Run Server as per need
>> python manage.py createsuperuser
>> python manage.py runserver

# Testing CRUD Operations

# API Endpoints

(Method - 1)
>> List all entries: GET /api/table1/
>> Retrieve a specific entry: GET /api/table1/{id}/
>> Create a new entry: POST /api/table1/
>> Update an existing entry: PUT /api/table1/{id}/
>> Delete an entry: DELETE /api/table1/{id}/

(Method - 2)
Note : If wanna see changes realtime then use curl before commands :-)
