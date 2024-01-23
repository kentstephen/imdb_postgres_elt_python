#fill in your creds

pg_database = 'imdb' #you can call the db whatever you want, just change here
pg_user = 'your_user' 
pg_password = 'your_password'
pg_host = 'localhost' # your host
pg_port = '5432' 
DB_CONN_STRING = f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
