import psycopg2
import tkinter as tk

# Variables
artistIndex = 0
currentFrame = 'startFrame'


# GUI
root = tk.Tk()
searchText = tk.StringVar()
root.title("Artist lookup") # Title
root.geometry("500x400") # Window size

# Initialize frames
startFrame = tk.Frame(root) 
startFrame.grid(row=0, column=0)
artistFrame = tk.Frame(root)
artistFrame.grid(row=0, column=1)
advanceFrame = tk.Frame(root)
advanceFrame.grid(row=0, column=2)

def setStartFrame():
    startFrame.grid(row=0, column=0)

def hideStartFrame():
    startFrame.grid_forget()

def displayStartFrame(event=None):
    print("called")
    global currentFrame
    if currentFrame == 'artistFrame':
        clear(artistFrame)
        artistFrame.grid_forget()
    elif currentFrame == 'advanceFrame':
        clear(advanceFrame)
        advanceFrame.grid_forget()

    setStartFrame()
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
    global currentFrame
    currentFrame = 'artistFrame'
    clear(artistFrame)
    setArtistFrame()
    artistName = searchEntry.get()
    artistTracks = fetchArtistInfo(artistName)
    artistTrack = artistTracks[artistIndex][1]
    trackID = artistTracks[artistIndex][2]
    artistInformation = tk.Label(artistFrame, text=artistTrack)
    artistBackButton = tk.Button(artistFrame, text="Back", command=lambda: artistBackButtonPressed(artistName))
    artistNextButton = tk.Button(artistFrame, text="Next", command=lambda: artistNextButtonPressed(artistName, len(artistTracks)))


    artistNextButton.grid(row=1, column=4, pady=50)
    artistInformation.grid(row=0, column=3, pady=50)
    artistBackButton.grid(row=1, column=0, pady=50)

    mainMenuButton = tk.Button(artistFrame, text="Main menu", command=lambda: displayStartFrame())
    mainMenuButton.grid(row=2, column=0, pady=100)

    advanceButton = tk.Button(artistFrame, text="Advance", command=lambda: advanceButtonPressed(trackID))
    advanceButton.grid(row=2, column=4, pady=100)

    hideStartFrame()
    startFrame.grid_forget()

def displayArtistFrameGiven(artistName):
    global currentFrame
    currentFrame = 'artistFrame'
    clear(artistFrame)
    setArtistFrame()
    artistTracks = fetchArtistInfo(artistName)
    artistTrack = artistTracks[artistIndex][1]
    trackID = artistTracks[artistIndex][2]
    artistInformation = tk.Label(artistFrame, text=artistTrack)
    artistBackButton = tk.Button(artistFrame, text="Back", command=lambda: artistBackButtonPressed(artistName))
    artistNextButton = tk.Button(artistFrame, text="Next", command=lambda: artistNextButtonPressed(artistName, len(artistTracks)))

    artistNextButton.grid(row=1, column=4, pady=50)
    artistInformation.grid(row=0, column=3, pady=50)
    artistBackButton.grid(row=1, column=0, pady=50)

    mainMenuButton = tk.Button(artistFrame, text="Main menu", command=lambda: displayStartFrame())
    mainMenuButton.grid(row=2, column=0, pady=100)

    advanceButton = tk.Button(artistFrame, text="Advance", command=lambda: advanceButtonPressed(trackID))
    advanceButton.grid(row=2, column=4, pady=100)
    
    hideStartFrame()
    startFrame.grid_forget()

# Gets artist's previous track and updates frame
def artistBackButtonPressed(artistName):
    global artistIndex
    if artistIndex != 0:
        artistIndex -= 1
    displayArtistFrameGiven(artistName)

# Gets artist's next track and updates frame
def artistNextButtonPressed(artistName, trackSize):
    global artistIndex
    if artistIndex < trackSize - 1:
        artistIndex += 1
    displayArtistFrameGiven(artistName)

# TODO: make button take you to advanceFrame and display information 
def advanceButtonPressed(trackID):
    cur.execute("select * from audiofeature where track_id = 'spotify:track:1XAZlnVtthcDZt2NI1Dtxo';")
    column = cur.fetchall()
    print(column)
 
# persistent start buttons
# Reason I can't just use the method is because displayArtistFrameSearch relies on searchEntry
# instantiation 
searchButton = tk.Button(startFrame, text="Search", command=displayArtistFrameSearch)
searchButton.grid(row=0, column=1)
searchEntry = tk.Entry(startFrame, textvariable=searchText)
searchEntry.grid(row=0, column=0)
searchEntry.bind("<Return>", displayArtistFrameSearch) # Allows you to press enter to search




def fetchArtistInfo(name):
    cur.execute(f"select Artist.artist_name, track.track_name, track.track_id from track, composes, artist where track.track_id = composes.track_id and composes.artist_id = artist.artist_id and artist.artist_name = '{name}';")
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
