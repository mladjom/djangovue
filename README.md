# Django + Vue + GraphQL



## What is it about?



## Get started

```bash
python -m venv ~/.virtualenvs/djangovue

```bash
source ~/.virtualenvs/djangovue/bin/activate

```bash
cd backend

```bash
python manage.py runserver


### Setup

```bash
# Install Python dependencies
pip -r requirements.txt

# Create sqlite3 database and apply migrations
./manage.py migrate

# Install Vue dependencies
cd frontend
npm install
cd ..

# Create an admin account
./manage.py createsuperuser
```

### Run 

```bash
# Run development server
./manage.py runserver

# Run frontend in dev mode
cd frontend
npm serve
```

### Build

```bash
# Build frontend
cd frontend 
npm build

# Collect static files
cd ..
./manage.py collectstatic
```