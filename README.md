# Get IMDB data into Postgres with SQL
## Using a Python Program

This is a continuation of [imdb_postgres_elt](https://github.com/kentstephen/imdb_postgres_elt)

This Python program runs the complete ELT of that repo, but a little easier. I'll refer you to the link above for the description of the SQL transformations 

## First you need to enter your credentials in [pg_config.py](https://github.com/kentstephen/imdb_postgres_elt_python/blob/main/pg_config.py)

This will allow the .py and SQL therein to interact with your Postgres server

## Next go to [app.py](https://github.com/kentstephen/imdb_postgres_elt_python/blob/main/app.py)

This runs the whole thing, the full version of [imdb_postgres_elt](https://github.com/kentstephen/imdb_postgres_elt) in a more streamlined way

## In the end

You will end up with a database with new tables that unnest arrays and a schema with a lot more granularity

## Enjoy, and let me know what you think!
