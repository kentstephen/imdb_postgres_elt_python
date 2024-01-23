import os
import subprocess
from pg_config import pg_user, pg_password, pg_host, pg_port, pg_database

import os

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def copy_table(table_name, file_name):
    full_file_path = os.path.abspath(file_name)
    copy_query = f"\\copy {table_name} FROM '{full_file_path}' WITH (FORMAT csv, HEADER, DELIMITER '\t', NULL '\\N')"

    try:
        subprocess.run(
            ['psql', 
             '-h', pg_host, 
             '-p', pg_port, 
             '-U', pg_user, 
             '-d', pg_database, 
             '-c', copy_query],
            shell=False,
            check=True,
            text=True,
            input=pg_password,
            env={'PGPASSWORD': pg_password}
        )
        print(f"Copied data into {table_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error copying data into {table_name}: {e}")
        
def main():
 #List of tables and their corresponding file names
    tables_and_files = [
        ("title_ratings", "title.ratings.tsv"),
        ("title_principals", "title.principals.tsv"),
        ("title_episode", "title.episode.tsv"),
        ("title_crew", "title.crew.tsv"),
        ("title_basics", "title.basics.tsv"),
        ("title_akas", "title.akas.tsv"),
        ("name_basics", "name.basics.tsv"),
    ]

    for table, file in tables_and_files:
        copy_table(table, file)

if __name__ == "__main__":
    main()
