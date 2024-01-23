import psycopg2
from concurrent.futures import ThreadPoolExecutor
from pg_config import DB_CONN_STRING

def insert_title_directors():
    conn = psycopg2.connect(DB_CONN_STRING)
    insert_query = """
    INSERT INTO title_directors (tconst, director_nconst)
    SELECT tc.tconst, unnest(string_to_array(tc.directors, ',')) AS director_nconst
    FROM title_crew tc
    WHERE tc.directors IS NOT NULL AND tc.directors <> '';
    """
    try:
        with conn.cursor() as curs:
            curs.execute(insert_query)
        conn.commit()
        print("Inserted data into title_directors")
    except Exception as e:
        print(f"Error inserting data into title_directors: {e}")
        conn.rollback()
    finally:
        conn.close()

def insert_title_writers():
    conn = psycopg2.connect(DB_CONN_STRING)
    insert_query = """
    INSERT INTO title_writers (tconst, writer_nconst)
    SELECT tc.tconst, unnest(string_to_array(tc.writers, ',')) AS writer_nconst
    FROM title_crew tc
    WHERE tc.writers IS NOT NULL AND tc.writers <> '';
    """
    try:
        with conn.cursor() as curs:
            curs.execute(insert_query)
        conn.commit()
        print("Inserted data into title_writers")
    except Exception as e:
        print(f"Error inserting data into title_writers: {e}")
        conn.rollback()
    finally:
        conn.close()

def insert_name_known_for():
    conn = psycopg2.connect(DB_CONN_STRING)
    insert_query = """
    INSERT INTO name_known_for (nconst, tconst)
    SELECT nb.nconst, unnest(string_to_array(nb.knownfortitles, ',')) AS tconst
    FROM name_basics nb
    WHERE nb.knownfortitles IS NOT NULL AND nb.knownfortitles <> '';
    """
    try:
        with conn.cursor() as curs:
            curs.execute(insert_query)
        conn.commit()
        print("Inserted data into name_known_for")
    except Exception as e:
        print(f"Error inserting data into name_known_for: {e}")
        conn.rollback()
    finally:
        conn.close()

def name_title_character():
    conn = psycopg2.connect(DB_CONN_STRING)
    insert_query = """
    INSERT INTO name_title_character (nconst, tconst, character)
    SELECT
        tp.nconst,
        tp.tconst,
        unnest(string_to_array(trim(both '[]" ' from tp.characters), '","')) AS character
    FROM
        title_principals tp
    WHERE
        tp.characters IS NOT NULL AND tp.characters <> '';
    """
    try:
        with conn.cursor() as curs:
            curs.execute(insert_query)
        conn.commit()
        print("Inserted data into name_title_character")
    except Exception as e:
        print(f"Error inserting data into name_title_character: {e}")
        conn.rollback()
    finally:
        conn.close()

def main():
    print("Inserting data into new tables to bypass array data types")

    # Execute insert operations concurrently
    with ThreadPoolExecutor() as executor:
        tasks = [insert_title_directors, insert_title_writers, insert_name_known_for, name_title_character]
        executor.map(lambda func: func(), tasks)

if __name__ == "__main__":
    main()
