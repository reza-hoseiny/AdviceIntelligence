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
        insert into inventory (name, description, capacity)
        values ('inventory1', 'Fruit inventory', '2010')
        """)

    else:
        print ('Database exists, assume schema does, too.')

# read all projects
with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute("""
    select * from inventory
    """)
    for row in cursor.fetchall():
        name, description, deadline = row
        print ('Inventory details for ``%s` (`%s`) due %s' % (description, name, capacity))

        