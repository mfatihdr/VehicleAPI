# VehicleAPI<br/>
A study contained of 2 tables on PostgreSQL prepared with DRF.<br/>


You need to create a table For database based cache with code below;<br/>

(env) "python3 manage.py createcachetable"<br/>

create a table and save as below in settings.py;<br/>

DATABASES = {<br/>
    'default': {<br/>
       'ENGINE': 'django.db.backends.postgresql_psycopg2',<br/>
        'NAME': 'veh_db',<br/>
        'USER': 'veh_admin',<br/>
        'PASSWORD': 'passw',<br/>
        'HOST': 'localhost',<br/>
        'PORT': '5432',<br/>
    }<br/>
}<br/>



localhost:127.0.0.1:5432/create_model<br/>
localhost:127.0.0.1:5432/create<br/>
localhost:127.0.0.1:5432/<veh_id><br/>
localhost:127.0.0.1:5432/<veh_id>/delete<br/>
localhost:127.0.0.1:5432/<veh_id>/update<br/>
