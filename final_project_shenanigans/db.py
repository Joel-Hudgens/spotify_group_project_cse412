import psycopg2

#Instructions:
#first connect to the spotify database then edit in your information below(pretty sure its just database and user)
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
cur.execute("select Artist.artist_name,track.track_name from track, composes, artist where track.track_id = composes.track_id and composes.artist_id = artist.artist_id and artist.artist_name = 'KSI';")

column = cur.fetchall()

for i in column:
    print(i)


cur.close()

con.close()
