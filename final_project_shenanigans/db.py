import psycopg2
import tkinter as tk


# Variables
artistIndex = 0
currentFrame = 'loginFrame'
currentUsername = ''
currentID = ''


# GUI
root = tk.Tk()
searchText = tk.StringVar()
root.title("Artist lookup") # Title
root.geometry("500x500") # Window size

# Initialize frames
loginFrame = tk.Frame(root) 
loginFrame.grid(row=0, column=0)
startFrame = tk.Frame(root) 
startFrame.grid(row=0, column=1)
artistFrame = tk.Frame(root)
artistFrame.grid(row=0, column=2)

# Sets visibility for start frame
def setStartFrame():
    startFrame.grid(row=0, column=0)

# Sets buttons and labels for start frame
def setStartFrameWidgets():
    searchButton = tk.Button(startFrame, text="Search", command=lambda: displayArtistFrame(searchEntry.get()))
    searchButton.grid(row=0, column=1)
    searchEntry = tk.Entry(startFrame, textvariable=searchText)
    searchEntry.grid(row=0, column=0)

# Removes start frame.
def hideStartFrame():
    startFrame.grid_forget()

# Checks what the current frame is, and appropriately removes the widgets
# for that page and displays the start page.
def displayStartFrame(event=None):
    global currentFrame
    if currentFrame == 'artistFrame':
        clear(artistFrame)
        artistFrame.grid_forget()
    elif currentFrame == 'loginFrame':
        clear(loginFrame)
        loginFrame.grid_forget()

    setStartFrameWidgets()
    setStartFrame()
    
# Sets visibility of artist frame.
def setArtistFrame():
    artistFrame.grid(row=0, column=1)

 
# Removes all widgets from a frame
# widgets are the buttons, labels, etc from a frame.
def clear(frame):
    widgets = frame.grid_slaves()
    for i in widgets:
        i.destroy()
 
# Displays artist frame given an artist name.
def displayArtistFrame(artistName):
    global currentFrame
    currentFrame = 'artistFrame'
    clear(artistFrame)
    setArtistFrame()
    artistTracks = fetchArtistInfo(artistName)
    artistTrack = artistTracks[artistIndex][1]
    trackID = artistTracks[artistIndex][2]
    artistInformation = tk.Label(artistFrame, text=artistTrack, wraplength=200)
    artistBackButton = tk.Button(artistFrame, text="Back", command=lambda: artistBackButtonPressed(artistName))
    artistNextButton = tk.Button(artistFrame, text="Next", command=lambda: artistNextButtonPressed(artistName, len(artistTracks)))

    artistNextButton.grid(row=1, column=4, pady=25)
    artistInformation.grid(row=0, column=3, pady=25)
    artistBackButton.grid(row=1, column=0, pady=25)

    mainMenuButton = tk.Button(artistFrame, text="Main menu", command=lambda: displayStartFrame())
    mainMenuButton.grid(row=2, column=0)

    advanceButton = tk.Button(artistFrame, text="Advance", command=lambda: advanceButtonPressed(trackID, artistInformation))
    advanceButton.grid(row=2, column=4)
    
    hideStartFrame()
    startFrame.grid_forget()

# Gets artist's previous track and updates frame
def artistBackButtonPressed(artistName):
    global artistIndex
    if artistIndex != 0:
        artistIndex -= 1
    displayArtistFrame(artistName)

# Gets artist's next track and updates frame
def artistNextButtonPressed(artistName, trackSize):
    global artistIndex
    if artistIndex < trackSize - 1:
        artistIndex += 1
    displayArtistFrame(artistName)

# Changes track label and displays audio information
def advanceButtonPressed(trackID, artistInformation):
    cur.execute(f"select * from audiofeature where track_id = '{trackID}';")
    column = cur.fetchall()
    trackData = column[0] 
    
    artistInformation.config(
    text=f"track id = {trackData[0]}\n"
         f"danceability = {trackData[1]}\n"
         f"energy = {trackData[2]}\n"
         f"key signature = {trackData[3]}\n"
         f"loudness = {trackData[4]}\n"
         f"mode = {trackData[5]}\n"
         f"speechiness = {trackData[6]}\n"
         f"acousticness = {trackData[7]}\n"
         f"instrumentalness = {trackData[8]}\n"
         f"liveness = {trackData[9]}\n"
         f"valence = {trackData[10]}\n"
         f"tempo = {trackData[11]}\n"
         f"time signature = {trackData[12]}"
    )


# Checks if user is in the database.
def validateUser(username, password):
    global currentUsername
    global currentID
    cur.execute(f"Select username, password, listener_id from Listener where username = '{username}' and password = '{password}';")
    column = cur.fetchall()
    

    if len(column) == 0:
        print("oopsie poopsie")
    else:
        currentUsername = username
        currentID = column[0][2]
        print(currentID)
        displayStartFrame()

# Creates the account. Does not allow for duplicate usernames.
def registerAccount(username, password):
    cur.execute(f"Select username from Listener where username = '{username}';")
    column = cur.fetchall()

    if len(column) == 0:
        cur.execute(f"INSERT INTO Listener (username, password) VALUES ('{username}', '{password}') ON CONFLICT (listener_id) DO NOTHING;")
        con.commit()
        print("User created")
    else: 
        print("User already exist")
    

# Initial widgets for login page
lbl = tk.Label(loginFrame, text="Username")
lbl.pack(pady=1)
usernameEntry = tk.Entry(loginFrame, textvariable="username")
usernameEntry.pack(pady=1)

lbl2 = tk.Label(loginFrame, text="Password")
lbl2.pack(pady=1)
passwordEntry = tk.Entry(loginFrame, textvariable="password")
passwordEntry.pack(pady=1)

loginButton = tk.Button(loginFrame, text="Login", command=lambda: validateUser(usernameEntry.get(), passwordEntry.get()))
loginButton.pack(pady=1)

registerButton = tk.Button(loginFrame, text="Register", command=lambda: registerAccount(usernameEntry.get(), passwordEntry.get()))
registerButton.pack(pady=1)

# Fetches artist information. Used by artist frame.
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
