import psycopg2
import tkinter as tk

# Variables
artistIndex = 0

# GUI
root = tk.Tk()
root.title("Artist lookup") # Title
root.geometry("500x400") # Window size

# Initialize frames
startFrame = tk.Frame(root) 
startFrame.grid(row=0, column=0)
artistFrame = tk.Frame(root)
artistFrame.grid(row=0, column=1)

def setStartFrame():
    startFrame.grid(row=0, column=0)

def setArtistFrame():
    artistFrame.grid(row=0, column=1)
 
# Removes all widgets from a frame
# widgets are the buttons, labels, etc from a frame.
def clear(frame):
    widgets = frame.grid_slaves()
    for i in widgets:
        i.destroy()
 
# Both displays do the same thing, but the first one does it from the searchEntry 
# and the other does it from an input artist name
def displayArtistFrameSearch(event=None):
    clear(artistFrame)
    artistName = searchEntry.get()
    print(f"Search Clicked: {artistName}")
    artistTracks = fetchArtistInfo(artistName)
    artistTrack = artistTracks[artistIndex][1]
    artistInformation = tk.Label(artistFrame, text=artistTrack)
    artistBackButton = tk.Button(artistFrame, text="Back", command=lambda: artistBackButtonPressed(artistName))
    artistNextButton = tk.Button(artistFrame, text="Next", command=lambda: artistNextButtonPressed(artistName, len(artistTracks)))


    artistNextButton.grid(row=0, column=2)
    artistInformation.grid(row=0, column=1)
    artistBackButton.grid(row=0, column=0)

    clear(startFrame)
    startFrame.grid_forget()

def displayArtistFrameGiven(artistName):
    clear(artistFrame)
    print(f"Search Clicked: {artistName}")
    artistTracks = fetchArtistInfo(artistName)
    artistTrack = artistTracks[artistIndex][1]
    artistInformation = tk.Label(artistFrame, text=artistTrack)
    artistBackButton = tk.Button(artistFrame, text="Back", command=lambda: artistBackButtonPressed(artistName))
    artistNextButton = tk.Button(artistFrame, text="Next", command=lambda: artistNextButtonPressed(artistName, len(artistTracks)))

    artistNextButton.grid(row=0, column=2)
    artistInformation.grid(row=0, column=1)
    artistBackButton.grid(row=0, column=0)
    

    clear(startFrame)
    startFrame.grid_forget()

def artistBackButtonPressed(artistName):
    global artistIndex
    if artistIndex != 0:
        artistIndex -= 1
    displayArtistFrameGiven(artistName)

def artistNextButtonPressed(artistName, trackSize):
    global artistIndex
    if artistIndex < trackSize - 1:
        artistIndex += 1
    displayArtistFrameGiven(artistName)
 
# persistent start buttons
searchButton = tk.Button(startFrame, text="Search", command=displayArtistFrameSearch)
searchButton.grid(row=0, column=1)
searchEntry = tk.Entry(startFrame)
searchEntry.grid(row=0, column=0)
searchEntry.bind("<Return>", displayArtistFrameSearch) # Allows you to press enter to search



def fetchArtistInfo(name):
    cur.execute(f"select Artist.artist_name,track.track_name from track, composes, artist where track.track_id = composes.track_id and composes.artist_id = artist.artist_id and artist.artist_name = '{name}';")
    column = cur.fetchall()

    if len(column) == 0:
        print("Artist not found")
    else:
        return column

    

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


root.mainloop() # Displays GUI

cur.close()

con.close()
