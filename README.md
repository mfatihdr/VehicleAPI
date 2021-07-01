# VehicleAPI
A study contained of 2 tables on PostgreSQL prepared with DRF.


You need to create a table For database based cache with code below;

(env) "python3 manage.py createcachetable"

create database and save as below in settings.py;

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'veh_db',
        'USER': 'veh_admin',
        'PASSWORD': 'passw',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



localhost:127.0.0.1:5432/create_model
localhost:127.0.0.1:5432/create
localhost:127.0.0.1:5432/<veh_id>
localhost:127.0.0.1:5432/<veh_id>/delete
localhost:127.0.0.1:5432/<veh_id>/update
