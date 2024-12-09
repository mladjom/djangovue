# Django + Vue + GraphQL



## What is it about?
Under development. Not to be used.


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
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_data

```bash
# Run development server
./manage.py runserver



```bash
# Usefull commands
django-admin makemessages -l <language_code>
django-admin compilemessages -l <language_code>


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
