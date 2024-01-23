import os
import subprocess
import shutil
from pg_config import pg_user, pg_password, pg_host, pg_port, pg_database

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    # Find the psql path
    psql_path = shutil.which("psql")
    if not psql_path:
        raise FileNotFoundError("psql executable not found in PATH")
    
    try:
        subprocess.check_call(
            [
                psql_path, '-q',
                '-U', pg_user,
                '-h', pg_host,
                '-p', str(pg_port),
                '-d', pg_database,
                '-f', 'copy_psql.sql'
            ],
            text=True,
            env={'PGPASSWORD': pg_password}
        )
    except subprocess.CalledProcessError as ex:
        print(f"Failed to invoke psql: {ex}")



if __name__ == "__main__":
    main()
