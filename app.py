import copy_tsvs_into_pg
import create_db
import drop_tables
import create_tables
import get_data
import delete_tsvs
import insert_into_new_tables
import allow_for_pks
import alter_for_keys
import sample_query


def run_scripts():
    create_db.main()  
    drop_tables.main()  #this file is for running continuously: "kill and fill". Or if you'd like to start over. Like the file says it will drop all the tables
    create_tables.main() 
    get_data.main() 
    copy_tsvs_into_pg.main()
    delete_tsvs.main()
    insert_into_new_tables.main()
    allow_for_pks.main()
    alter_for_keys.main()
    sample_query.main()
if __name__ == "__main__":
    run_scripts()  