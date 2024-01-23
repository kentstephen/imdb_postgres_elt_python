-- if you created the database, tables, and got the data can't run copy_from_data the try connecting to psql, 
-- open a terminal, navigate to the directory where this is, then
-- connect by writing: psql -h yourhost -p 5432 -U youruser -d imdb or whatever you called it
-- then write: \i copy_psql.sql

SET client_encoding TO 'UTF8';

\copy title_basics FROM ,title.basics.tsv' DELIMITER E'\t'CSV HEADER QUOTE E'\b' NULL AS '\N';

\copy name_basics FROM 'name.basics.tsv' DELIMITER E'\t' CSV HEADER QUOTE E'\b' NULL AS '\N';

\copy title_principals FROM 'title.principals.tsv' DELIMITER E'\t' QUOTE E'\b' CSV HEADER NULL AS '\N';

\copy title_akas FROM 'title.akas.tsv' DELIMITER E'\t' CSV HEADER QUOTE E'\b' NULL AS '\N';

\copy title_ratings FROM 'title.ratings.tsv' DELIMITER E'\t' CSV HEADER QUOTE E'\b' NULL AS '\N';

\copy title_crew FROM 'title.crew.tsv' DELIMITER E'\t'CSV HEADER QUOTE E'\b' NULL AS '\N';

\copy title_episode FROM 'title.episode.tsv' DELIMITER E'\t' CSV HEADER QUOTE E'\b'NULL AS '\N';