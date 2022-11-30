to run this code:

create virtual env
    
    python -m venv venv

activate venv

    source venv/bin/activate
    or
    .\venv\Scripts\Activate.ps1

install requirements.txt
    
    pip install -r requirements.txt

initialize postgres db

    docker-compose up --build --no-deps -d db 

migrate models

    python manage.py migrate

load data

    python manage.py loaddata db2.json

run project

    python manage.py runserver


    
    