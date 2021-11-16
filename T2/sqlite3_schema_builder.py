import os
import sqlite3

db_filename = 'fruitshop.db'
schema_filename = 'fruitshop_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print ('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print ('Inserting initial data')

        conn.execute("""
        insert into project (name, description, deadline)
        values ('Project 1', 'Python Module of the Week', '2010-11-01')
        """)

    else:
        print ('Database exists, assume schema does, too.')

# read all projects
with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute("""
    select * from project
    """)
    for row in cursor.fetchall():
        name, description, deadline = row
        print ('Project details for ``%s` (`%s`) due %s' % (description, name, deadline))

        # print ('Name = %s \nDescription: %s \t\t(%s)' % (name, description, deadline))

    # print ('Project table has these columns:')
    # for colinfo in cursor.description:
    #     print (colinfo)
