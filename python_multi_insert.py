import psycopg2
 
# forming connection
conn = psycopg2.connect(
    database="ehub",
    user='postgres',
    password='root',
    host='127.0.0.1',
    port='5432'
)
 
conn.autocommit = True
 
# creating a cursor
cursor = conn.cursor()
 
# list of rows to be inserted
values = [('rachel', 67), ('ross1234', 150), ('nick', 95)]
 
# executing the sql statement
cursor.executemany("INSERT INTO classroom (name,marks) VALUES(%s,%s) ON CONFLICT(name) do update set marks=excluded.marks", values)
 
# select statement to display output
sql1 = '''select * from classroom;'''
 
# executing sql statement
cursor.execute(sql1)
 
# fetching rows
for i in cursor.fetchall():
    print(i)
 
# committing changes
conn.commit()
 
# closing connection
conn.close()