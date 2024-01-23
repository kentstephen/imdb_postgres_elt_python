import requests
import gzip
import shutil
import os
# List of TSV file URLs

gz_file_urls = [
    "https://datasets.imdbws.com/title.ratings.tsv.gz",
    "https://datasets.imdbws.com/title.principals.tsv.gz",
    "https://datasets.imdbws.com/title.episode.tsv.gz",
    "https://datasets.imdbws.com/title.crew.tsv.gz",
    "https://datasets.imdbws.com/title.basics.tsv.gz",
    "https://datasets.imdbws.com/title.akas.tsv.gz",
    "https://datasets.imdbws.com/name.basics.tsv.gz",
]

def main():
    print("Downloading and extracting tsvs from imdb.com")
    for url in gz_file_urls:
        # Download the gzip file
        filename = url.split("/")[-1]
        gz_path = filename
        with open(gz_path, 'wb') as file:
            response = requests.get(url)
            file.write(response.content)

        # Extract the gzip file
        tsv_path = filename[:-3]  # Remove .gz from filename
        with gzip.open(gz_path, 'rb') as f_in:
            with open(tsv_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        

        # Delete the gzip file
        try:
            os.remove(gz_path)
        except PermissionError as e:
            print(f"Error deleting file {gz_path}: {e}")

if __name__ == "__main__":
    main()