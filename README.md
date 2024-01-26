# Get IMDB data into Postgres with SQL
## Using a Python Program

![erd](https://github.com/kentstephen/imdb_postgres_elt_python/blob/main/diagrams/imdb_schema.png)

This is the result schema. Taking 7 unrelated tables and adding relationships and more tables for ease of use

## This project a continuation of [imdb_postgres_elt](https://github.com/kentstephen/imdb_postgres_elt)

The Python program runs the complete ELT of that repo, but a little easier. I'll refer you to the link above for the description of the SQL transformations 

## First you need to enter your credentials in [pg_config.py](https://github.com/kentstephen/imdb_postgres_elt_python/blob/main/pg_config.py)

This will allow the Python files therein to interact with your Postgres server

## Next go to [app.py](https://github.com/kentstephen/imdb_postgres_elt_python/blob/main/app.py)

This runs the whole thing, the full version of [imdb_postgres_elt](https://github.com/kentstephen/imdb_postgres_elt) in a more streamlined way

## In the end

You will end up with a database with new tables that unnest arrays and a schema with a lot more granularity

## Enjoy, and let me know what you think!
