import psycopg2
from pg_config import DB_CONN_STRING

def main():
    conn = psycopg2.connect(DB_CONN_STRING)
    with conn.cursor() as curs:
        curs.execute(''' 
        CREATE TABLE IF NOT EXISTS title_basics (
            tconst VARCHAR(25) NOT NULL,
            titleType TEXT,
            primaryTitle TEXT,
            originalTitle TEXT,
            isAdult BOOLEAN,
            startYear INT,
            endYear INT,
            runtimeMinutes INT,
            genres TEXT
        );

        CREATE TABLE IF NOT EXISTS title_episode (
            tconst VARCHAR(15),
            parentTconst VARCHAR(15),
            seasonNumber INT,
            episodeNumber INT
        );

        CREATE TABLE IF NOT EXISTS name_basics (
            nconst VARCHAR(25) NOT NULL,
            primaryName TEXT,
            birthYear INT,
            deathYear INT,
            primaryProfession TEXT,
            knownForTitles TEXT
        );

        CREATE TABLE IF NOT EXISTS title_crew (
            tconst VARCHAR(15),
            directors TEXT,
            writers TEXT
        );

        CREATE TABLE IF NOT EXISTS title_ratings (
            tconst VARCHAR(15),
            averageRating FLOAT,
            numVotes INT
        );

        CREATE TABLE IF NOT EXISTS title_akas (
            titleId VARCHAR(15),
            ordering INT,
            title TEXT,
            region TEXT,
            language TEXT,
            types VARCHAR(50),
            attributes VARCHAR(255),
            isOriginalTitle BOOLEAN
        );

        CREATE TABLE IF NOT EXISTS title_principals (
            tconst VARCHAR(15),
            ordering INT,
            nconst VARCHAR(15),
            category TEXT,
            job TEXT,
            characters TEXT
        );

        CREATE TABLE IF NOT EXISTS title_directors (
            tconst VARCHAR(25),
            director_nconst VARCHAR(25)
        );

        CREATE TABLE IF NOT EXISTS title_writers (
            tconst VARCHAR(25),
            writer_nconst VARCHAR(25)
        );

        CREATE TABLE IF NOT EXISTS name_known_for (
            nconst VARCHAR(25),
            tconst VARCHAR(25)
        );
                     
        CREATE TABLE name_title_character (
            nconst VARCHAR(15),
            tconst VARCHAR(15),
            character TEXT
        );
        ''')
    conn.commit()
    curs.close()
    conn.close()
    print("Tables created")
if __name__ == "__main__":
    main()
