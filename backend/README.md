# Django + Vue + GraphQL



## What is it about?
 Djangovue, is a project under development combining Django, Vue, and GraphQL to build a blog. It includes both a backend (Django) and frontend (Vue),


### Setup

```bash
python -m venv ~/.virtualenvs/djangovue

```bash
source ~/.virtualenvs/djangovue/bin/activate

```bash
cd backend

```bash


```bash

```bash
# Install Python dependencies
pip -r requirements.txt

```bash
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py seed_data
python manage.py inspectdb
```bash
# Run development server
./manage.py runserver



```bash
# Usefull commands
django-admin makemessages -l <language_code> --ignore=templates/*
django-admin compilemessages -l <language_code>
pip freeze > requirements.txt

# Install Vue dependencies
cd frontend
npm install
cd ..


# Run frontend in dev mode
cd frontend
npm serve
```

### Build

```bash
# Build frontend
cd frontend 
npm build
