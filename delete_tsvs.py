import os

# List of filenames to delete
file_names_to_delete = [
    "title.ratings.tsv",
    "title.principals.tsv",
    "title.episode.tsv",
    "title.crew.tsv",
    "title.basics.tsv",
    "title.akas.tsv",
    "name.basics.tsv",
]

def main():
    # Loop through the filenames and delete each file
    for filename in file_names_to_delete:
        try:
            os.remove(filename)
            print(f"Successfully deleted {filename}")
        except OSError as e:
            print(f"Error deleting {filename}: {e.strerror}")
if __name__ == "__main__":
    main()
