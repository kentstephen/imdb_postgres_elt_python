import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pg_config import DB_CONN_STRING

def main():
    # change name here if you want to call it something else
    conn = psycopg2.connect(DB_CONN_STRING)

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curs = conn.cursor()

    # Retrieve the list of tables
    curs.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public'")
    tables = curs.fetchall()

    # Drop each table
    for table in tables:
        curs.execute(f"DROP TABLE IF EXISTS {table[0]} CASCADE")
        print(f"Dropped table {table[0]}")

    curs.close()
    conn.close()

if __name__ == "__main__":
    main()
