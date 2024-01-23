
from pg_config import DB_CONN_STRING, pg_database
import psycopg2
import csv
import sys

def main():
    sql_query = ('''
SELECT
    nb.primaryname AS james_bond,
    CAST(AVG(tr.averagerating) AS DECIMAL(10,2)) AS avg_bond_rating
FROM name_basics nb
INNER JOIN title_principals tp ON nb.nconst = tp.nconst
INNER JOIN title_basics tb ON tp.tconst = tb.tconst
INNER JOIN name_title_character ntk ON nb.nconst = ntk.nconst AND tb.tconst = ntk.tconst
INNER JOIN title_ratings tr ON tb.tconst = tr.tconst
WHERE
    ntk.character = 'James Bond'
    AND tp.category = 'actor'
    AND tb.titletype = 'movie'
GROUP BY
    nb.primaryname
ORDER BY
    avg_bond_rating DESC;
''')
        
    
    
    print(f"\nHere is a sample query with output, give it a sec:\n{sql_query}")

    try:
        conn = psycopg2.connect(DB_CONN_STRING)
        with conn, conn.cursor() as curs:
            curs.execute(sql_query)
            # Fetch the column names
            columns = [desc[0] for desc in curs.description]
            # Fetch all rows
            rows = curs.fetchall()
            # Create a CSV writer that outputs to the console
            writer = csv.writer(sys.stdout)
            # Write the header (column names)
            writer.writerow(columns)
            # Write the rows
            writer.writerows(rows)
    except Exception as e:
        print(f"An error occurred: {e}")
    print("\nAll the Bonds with some unexpected entries...\n\nGood luck with your queries!")
if __name__ == "__main__":
    main()