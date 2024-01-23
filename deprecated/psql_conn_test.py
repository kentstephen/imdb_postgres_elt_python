import subprocess
from pg_config import pg_user, pg_password, pg_host, pg_port, pg_database
import shutil


# Find the psql path
psql_path = shutil.which("psql")
if not psql_path:
    raise FileNotFoundError("psql executable not found in PATH")

try:
    subprocess.run(
        [psql_path,
         '-h', pg_host,
         '-p', pg_port,
         '-U', pg_user,
         '-d', pg_database],
        check=True,
        text=True,
        env={'PGPASSWORD': pg_password}
    )
except subprocess.CalledProcessError as e:
    print(f"Failed to connect to psql: {e}")
