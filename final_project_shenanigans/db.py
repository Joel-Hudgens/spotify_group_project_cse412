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
searchTrackText = tk.StringVar()
searchAlbumText = tk.StringVar()
root.title("Artist lookup") # Title
root.geometry("500x500") # Window size

# Initialize frames
loginFrame = tk.Frame(root) 
loginFrame.grid(row=0, column=0)
startFrame = tk.Frame(root) 
startFrame.grid(row=0, column=1)
artistFrame = tk.Frame(root)
artistFrame.grid(row=0, column=2)
favFrame = tk.Frame(root)
favFrame.grid(row=0, column=3) 
trackFrame = tk.Frame(root)
trackFrame.grid(row=0, column=4) 
albumFrame = tk.Frame(root)
albumFrame.grid(row=0, column=5) 

# Sets visibility for start frame
def setStartFrame():
    startFrame.grid(row=0, column=0)

# Sets buttons and labels for start frame
def setStartFrameWidgets():
    searchButton = tk.Button(startFrame, text="Search Artist", command=lambda: displayArtistFrame(searchEntry.get()))
    searchButton.grid(row=0, column=1)
    searchEntry = tk.Entry(startFrame, textvariable=searchText)
    searchEntry.grid(row=0, column=0)

    trackFavsButton = tk.Button(startFrame, text="Favorite Tracks", command=lambda: displayFavTrack(searchEntry.get()))
    trackFavsButton.grid(row=3, column=0)
    trackFavsButton.bind("<Return>", displayFavTrack) 

    artistFavsButton = tk.Button(startFrame, text="Favorite Artists", command=lambda: displayFavArtist(searchEntry.get()))
    artistFavsButton.grid(row=4, column=0)
    artistFavsButton.bind("<Return>", displayFavArtist) 

    searchTrackButton = tk.Button(startFrame, text="Search Track", command=lambda: displayTrackFrame(searchTrackEntry.get()))
    searchTrackButton.grid(row=1, column=1)
    searchTrackEntry = tk.Entry(startFrame, textvariable=searchTrackText)
    searchTrackEntry.grid(row=1, column=0)

    searchAlbumButton = tk.Button(startFrame, text="Search Album", command=lambda: displayAlbumFrame(searchAlbumEntry.get()))
    searchAlbumButton.grid(row=2, column=1)
    searchAlbumEntry = tk.Entry(startFrame, textvariable=searchAlbumText)
    searchAlbumEntry.grid(row=2, column=0)

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
    elif currentFrame == 'favFrame':
        clear(favFrame)
        favFrame.grid_forget()
    elif currentFrame == 'trackFrame':
        clear(trackFrame)
        trackFrame.grid_forget()
    elif currentFrame == 'albumFrame':
        clear(albumFrame)
        albumFrame.grid_forget()

    setStartFrameWidgets()
    setStartFrame()
    
# Sets visibility of artist frame.
def setArtistFrame():
    artistFrame.grid(row=0, column=1)

# Sets visibility of fav frame.
def setFavFrame():
    favFrame.grid(row=0, column=1)
#sets visibility of track frame
def setTrackFrame():
    trackFrame.grid(row=0, column=1)

#sets visibility of track frame
def setAlbumFrame():
    albumFrame.grid(row=0, column=1)

 
# Removes all widgets from a frame
# widgets are the buttons, labels, etc from a frame.
def clear(frame):
    widgets = frame.grid_slaves()
    for i in widgets:
        print("teset")
        i.destroy()
 
# Displays artist frame given an artist name.
def displayArtistFrame(artistName):
    
    global currentFrame
    currentFrame = 'artistFrame'
    artistFrame.grid_forget()
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

def displayAlbumFrame(albumName):
    global currentFrame
    currentFrame = 'albumFrame'
    albumFrame.grid_forget()
    clear(albumFrame)
    setAlbumFrame()
    albumTracks = fetchAlbumInfo(albumName)
    print(albumTracks)
    albumLabel = tk.Label(albumFrame, text=albumTracks)
    albumLabel.grid(row=1, column=4, pady=1)

    mainMenuButton = tk.Button(albumFrame, text="Main menu", command=lambda: displayStartFrame())
    mainMenuButton.grid(row=2, column=4)

    hideStartFrame()
    startFrame.grid_forget()
#TRAAAAAAAAAAAAACCCCCCCKKKKKKKKKKKKKKKKKKKKKKK SEEEEEEAAAAAAARRRRRRRRRRCHHHHHHHHHH
def displayTrackFrame(trackName):
    global currentFrame
    currentFrame = 'trackFrame'
    trackFrame.grid_forget()
    clear(trackFrame)
    setTrackFrame()
    trackTracks = fetchTrackInfo(trackName)
    print(trackTracks)
    trackLabel = tk.Label(trackFrame, text=trackTracks)
    trackLabel.grid(row=1, column=4, pady=1)
    mainMenuButton = tk.Button(trackFrame, text="Main menu", command=lambda: displayStartFrame())
    mainMenuButton.grid(row=2, column=4)

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





def displayFavArtist(event=None):
    global currentID
    global currentFrame
    clear(favFrame)
    setFavFrame()
    print(currentID)
    currentFrame = 'favFrame'
    cur.execute(f"select artist_name from artist, follows, listener where artist.artist_id = follows.artist_id and listener.listener_id = follows.listener_id and listener.listener_id = '{currentID}';")
    column = str(cur.fetchall())
    column = column.replace("{","")
    column = column.replace("}","")
    column = column.replace("(","")
    column = column.replace(")","")
    column = column.replace("'","")
    column = column.replace("[","")
    column = column.replace("]","")
    print(column)
    ftLabel = tk.Label(favFrame, text=column.replace(",","\n"))
    ftLabel.grid(row=1, column=4, pady=1)

    mainMenuButton = tk.Button(favFrame, text="Main menu", command=lambda: displayStartFrame())
    mainMenuButton.grid(row=2, column=4, pady=1)
    hideStartFrame()
    startFrame.grid_forget()



def displayFavTrack(event=None):
    global currentID
    global currentFrame
    clear(favFrame)
    setFavFrame()
    currentFrame = 'favFrame'
    cur.execute(f"select track_name from listener, track, likes where listener.listener_id = likes.listener_id and track.track_id = likes.track_id and listener.listener_id = '{currentID}';")
    column = str(cur.fetchall())
    column = column.replace("{","")
    column = column.replace("}","")
    column = column.replace("(","")
    column = column.replace(")","")
    column = column.replace("'","")
    column = column.replace("[","")
    column = column.replace("]","")
    
    print(column)
    ftLabel = tk.Label(favFrame, text=column.replace(",","\n"))
    ftLabel.grid(row=1, column=4, pady=1)
    

    mainMenuButton = tk.Button(favFrame, text="Main menu", command=lambda: displayStartFrame())
    mainMenuButton.grid(row=2, column=4, pady=1)
    hideStartFrame()
    startFrame.grid_forget()


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

loginButton = tk.Button(loginFrame, text="Login", command=lambda: validateUser(usernameEntry.get(), passwordEntry.get()))#("zebra_apple", "x9v3pL!"))
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
    
def fetchTrackInfo(name):
    if("'" in name):
        name = name.replace("'","''")
    cur.execute(f"select track_name, album_name, disc_number, track_number, duration_ms, is_explicit, popularity, preview_url, isrc from track, album where album.album_id = track.album_id and track_name = '{name}';")
    column = cur.fetchall()
    test = column[0]
    print(test)



    if len(column) == 0:
        print("Track not found")
    else:
        return "Track: " + str(test[0]) + "\n" + "Album name: "+ str(test[1]) +"\n" + "Disc number: " + str(test[2]) +"\n" + "Track Number:"+ str(test[3]) +"\n" + "Duration: "+ str(test[4]) +"\n" + "Age appropriate: " + str(test[5]) +"\n" + "Popularity score: " +str(test[6]) +"\n" + "URL Link: " + str(test[7] + "\n" + "isrc: "+ str(test[8]))

def fetchAlbumInfo(name):
    if("'" in name):
        name = name.replace("'","''")
    cur.execute(f"select track_name from track, album where track.album_id = album.album_id and album_name = '{name}';")
    column = str(cur.fetchall())
    column = column.replace("',)", "\n")
    column = column.replace(",", "")
    column = column.replace("'", "")
    column = column.replace("[", "")
    column = column.replace("(", "")
    column = column.replace("]", "")
    column = column.replace(")","")



    if len(column) == 0:
        print("Track not found")
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
