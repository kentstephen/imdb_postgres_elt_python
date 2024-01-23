import psycopg2
from pg_config import DB_CONN_STRING

def execute_query(conn, query):
    try:
        with conn.cursor() as curs:
            curs.execute(query)
            print(f"Executed: {query[:50]}...")
            conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error executing query: {query[:50]}...: {e}")

def main():
    # Create a database connection
    conn = psycopg2.connect(DB_CONN_STRING)

    # Primary key statements
    primary_key_statements = [
        "ALTER TABLE name_basics ADD PRIMARY KEY (nconst);",
        "ALTER TABLE title_basics ADD PRIMARY KEY (tconst);"
    ]

    for query in primary_key_statements:
        execute_query(conn, query)

    # Foreign key statements
    foreign_key_statements = [
        "ALTER TABLE title_episode ADD FOREIGN KEY (parenttconst) REFERENCES title_basics (tconst);",
        "ALTER TABLE title_akas ADD FOREIGN KEY (titleId) REFERENCES title_basics (tconst);",
        "ALTER TABLE title_ratings ADD FOREIGN KEY (tconst) REFERENCES title_basics (tconst);",
        "ALTER TABLE title_crew ADD FOREIGN KEY (tconst) REFERENCES title_basics (tconst);",
        "ALTER TABLE title_principals ADD FOREIGN KEY (tconst) REFERENCES title_basics (tconst);",
        "ALTER TABLE title_principals ADD FOREIGN KEY (nconst) REFERENCES name_basics (nconst);",
        "ALTER TABLE title_directors ADD FOREIGN KEY (director_nconst) REFERENCES name_basics (nconst);",
        "ALTER TABLE title_directors ADD FOREIGN KEY (tconst) REFERENCES title_basics (tconst);",
        "ALTER TABLE title_writers ADD FOREIGN KEY (writer_nconst) REFERENCES name_basics (nconst);",
        "ALTER TABLE title_writers ADD FOREIGN KEY (tconst) REFERENCES title_basics (tconst);",
        "ALTER TABLE name_known_for ADD FOREIGN KEY (tconst) REFERENCES title_basics (tconst);",
        "ALTER TABLE name_known_for ADD FOREIGN KEY (nconst) REFERENCES name_basics (nconst);"
        "ALTER TABLE name_title_character ADD FOREIGN KEY (tconst) REFERENCES title_basics (tconst);",
        "ALTER TABLE name_title_character ADD FOREIGN KEY (nconst) REFERENCES name_basics (nconst);"
    ]

  

# Execute foreign key statements concurrently
    
    for query in foreign_key_statements:
        execute_query(conn, query)

    # Close the connection
    conn.close()
    print("Process completed, congratulations!\nYou created a database and tables,\ndownloaded and extracted public tsv's from imdb.com\ncopied that data into Postgres\nthen you recreated the schema and allowed for constriants")
    
# Run the main function
if __name__ == "__main__":
    main()
