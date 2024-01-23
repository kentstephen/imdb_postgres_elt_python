import psycopg2
from concurrent.futures import ThreadPoolExecutor
from pg_config import DB_CONN_STRING

def insert_missing_tconst():
    conn = psycopg2.connect(DB_CONN_STRING)
    try:
        with conn.cursor() as curs:
            insert_query = """
            WITH MissingTconst AS (
                SELECT DISTINCT tconst
                FROM (
                    SELECT parenttconst as tconst FROM title_episode WHERE parenttconst IS NOT NULL
                    UNION
                    SELECT titleid as tconst FROM title_akas WHERE titleid IS NOT NULL
                    UNION
                    SELECT tconst FROM title_crew WHERE tconst IS NOT NULL
                    UNION
                    SELECT tconst FROM title_episode WHERE tconst IS NOT NULL
                    UNION
                    SELECT tconst FROM title_principals WHERE tconst IS NOT NULL
                    UNION
                    SELECT tconst FROM title_ratings WHERE tconst IS NOT NULL
                    UNION
                    SELECT tconst FROM title_directors WHERE tconst IS NOT NULL
                    UNION
                    SELECT tconst FROM title_writers WHERE tconst IS NOT NULL
                    UNION
                    SELECT tconst FROM name_known_for WHERE tconst IS NOT NULL
                ) AS combined_tconsts
            )
            INSERT INTO title_basics (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
            SELECT m.tconst, 'ANOMALY', NULL, NULL, NULL, NULL, NULL, NULL, NULL
            FROM MissingTconst m
            LEFT JOIN title_basics tb ON m.tconst = tb.tconst
            WHERE tb.tconst IS NULL;
            """
            curs.execute(insert_query)
        conn.commit()
        print("Inserted missing tconst data into title_basics")
    except Exception as e:
        print(f"Error inserting missing tconst data: {e}")
        conn.rollback()
    finally:
        conn.close()

def insert_missing_nconst():
    conn = psycopg2.connect(DB_CONN_STRING)
    try:
        with conn.cursor() as curs:
            insert_query = """
            WITH MissingNconst AS (
                SELECT DISTINCT nconst
                FROM (
                    SELECT nconst FROM title_principals WHERE nconst IS NOT NULL
                    UNION
                    SELECT director_nconst as nconst FROM title_directors WHERE director_nconst IS NOT NULL
                    UNION
                    SELECT writer_nconst as nconst FROM title_writers WHERE writer_nconst IS NOT NULL
                    UNION
                    SELECT nconst FROM name_known_for WHERE nconst IS NOT NULL
                ) AS combined_nconsts
            )
            INSERT INTO name_basics (nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles)
            SELECT mn.nconst, 'ANOMALY', NULL, NULL, NULL, NULL
            FROM MissingNconst mn
            LEFT JOIN name_basics nb ON mn.nconst = nb.nconst
            WHERE nb.nconst IS NULL;
            """
            curs.execute(insert_query)
        conn.commit()
        print("Inserted missing nconst data into name_basics")
    except Exception as e:
        print(f"Error inserting missing nconst data: {e}")
        conn.rollback()
    finally:
        conn.close()

def main():
    print("Running SQL queries to find distinct ID's that are not in the parent tables and updating the parent tables with the missing ID's to allow for constraints")

    # Execute the insert operations concurrently
    with ThreadPoolExecutor() as executor:
        executor.submit(insert_missing_tconst)
        executor.submit(insert_missing_nconst)

if __name__ == "__main__":
    main()
