import psycopg2
import os
from concurrent.futures import ThreadPoolExecutor
from pg_config import DB_CONN_STRING

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def copy_table(table_file_pair):
    table_name, file_name = table_file_pair
    conn = psycopg2.connect(DB_CONN_STRING)

    # Use os.path.abspath to get the full path of the file
    full_file_path = os.path.abspath(file_name)
    copy_query = f"""
    COPY {table_name} FROM '{full_file_path}' 
    WITH (FORMAT csv, DELIMITER E'\t', NULL '\\N', QUOTE E'\b', HEADER);
    """
    try:
        with conn.cursor() as curs:
            curs.execute(copy_query)
            conn.commit()
            print(f"Copied data into {table_name}")
    except Exception as e:
        print(f"Error copying data into {table_name}: {e}\n\ntry the client side with file copy_psql.sql")
        conn.rollback()
    finally:
        conn.close()

def main():
    print("Copying data into pg tables")

    # List of tables and their corresponding file names
    tables_and_files = [
        ("title_ratings", "title.ratings.tsv"),
        ("title_principals", "title.principals.tsv"),
        ("title_episode", "title.episode.tsv"),
        ("title_crew", "title.crew.tsv"),
        ("title_basics", "title.basics.tsv"),
        ("title_akas", "title.akas.tsv"),
        ("name_basics", "name.basics.tsv"),
    ]

    # Execute copy operations concurrently
    with ThreadPoolExecutor() as executor:
        executor.map(copy_table, tables_and_files)

if __name__ == "__main__":
    main()
