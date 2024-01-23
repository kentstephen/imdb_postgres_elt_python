import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pg_config import pg_user, pg_password, pg_host, pg_port, pg_database


def main():
    
    conn = psycopg2.connect(
        host=pg_host,
        port=pg_port,
        user=pg_user,
        password=pg_password,
        database='postgres'
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curs = conn.cursor()

    check_db_query = f"SELECT 1 FROM pg_database WHERE datname = '{pg_database}'"
    curs.execute(check_db_query)
    if not curs.fetchone():
        curs.execute(f"CREATE DATABASE {pg_database}")
        print(f"Created database {pg_database}")
    else:
        print(f"{pg_database} databse found")

    curs.close()
    conn.close()

if __name__ == "__main__":
    main()
