import psycopg2


#connecting to database also change database and user(when in postgre \du for users and \l for database)
con = psycopg2.connect(
    host = "localhost",
    database = "spotify",
    user = "maxickar",
    password = "pp",
    port = "8888"
)

cur = con.cursor()


#query shenanigans
cur.execute("Select * From artist")

column = cur.fetchall()

for i in column:
    print(i)


cur.close()

con.close()