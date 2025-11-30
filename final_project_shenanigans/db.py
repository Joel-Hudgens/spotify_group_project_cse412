import psycopg2
import tkinter as tk

# GUI
root = tk.Tk()
root.title("Artist lookup") # Title
root.geometry("500x400") # Window size

# Initialize frames
startFrame = tk.Frame(root) 
startFrame.grid(row=0, column=0)
artistFrame = tk.Frame(root)
artistFrame.grid(row=0, column=1)
 
# Removes all widgets from a frame
# widgets are the buttons, labels, etc from a frame.
def clear(frame):
    widgets = frame.grid_slaves()
    for i in widgets:
        i.destroy()
 
# TODO: Add GUI to properly display artist information and songs
def displayArtistFrame(searchEvent):
    clear(artistFrame)
    text = searchEntry.get()
    print(f"Search Clicked: {text}")
    tk.Label(artistFrame, text="Hello").grid(row=0, column=0) # Remove the label and entry for actual info
    tk.Entry(artistFrame).grid(row=1, column=0)

    
 
# persistent start buttons
searchButton = tk.Button(startFrame, text="Search", command=displayArtistFrame)
searchButton.grid(row=0, column=1)
searchEntry = tk.Entry(startFrame)
searchEntry.grid(row=0, column=0)
searchEntry.bind("<Return>", displayArtistFrame) # Allows you to press enter to search



def fetchArtistInfo(name):
    cur.execute(f"select Artist.artist_name,track.track_name from track, composes, artist where track.track_id = composes.track_id and composes.artist_id = artist.artist_id and artist.artist_name = '{name}';")
    column = cur.fetchall()

    if len(column) == 0:
        print("Artist not found")
    else:
        for i in column:
            print(i)

    

#Instructions:
#first connect to the spotify database then edit in your information below(pretty sure its just database and user)
#connecting to database also change database and user(when in postgre \du for users and \l for database)
con = psycopg2.connect(
    host = "localhost",
    database = "spotify",
    user = "",
    password = "",
    port = "8888"
)

cur = con.cursor()

#query shenanigans
#cur.execute("select Artist.artist_name,track.track_name from track, composes, artist where track.track_id = composes.track_id and composes.artist_id = artist.artist_id and artist.artist_name = 'KSI';")
fetchArtistInfo("Pitbull")


cur.close()

con.close()

root.mainloop() # Displays GUI

