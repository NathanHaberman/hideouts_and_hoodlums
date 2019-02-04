# To start the server:
# sudo systemctrl start postgresql.service

# To access the database:
# sudo -u postgres psql

database_info = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hnh',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}