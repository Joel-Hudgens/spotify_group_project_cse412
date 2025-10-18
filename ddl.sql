-- This file creates the spotify database according to our ER schema from phase 2
-- To create spotify PostgreSQL DB on your local machine:
-- git clone https://github.com/Joel-Hudgens/spotify_group_project_cse412.git
-- Navigate inside the diretory you just cloned
-- In your terminal:
-- createdb spotify
-- psql spotify -f ddl.sql



-- log in with username and password.
-- can like tracks and follow artists
CREATE TABLE Listener (
    listener_id SERIAL PRIMARY KEY, -- auto increment so we have a new id when we INSERT (username,password)
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Artist must have at least one track, but can be followed by any num of listeners
CREATE TABLE Artist (
    artist_id VARCHAR(50) PRIMARY KEY,
    artist_name VARCHAR(100) NOT NULL
);

-- An album must have at least one song. 
CREATE TABLE Album (
    album_id VARCHAR(50) PRIMARY KEY,
    album_name VARCHAR(200),
    release_date VARCHAR(50),  -- because some dates are just years
    label VARCHAR(100),
    copyrights TEXT
);

-- Represents a spotify song
CREATE TABLE Track (
    track_id VARCHAR(75) PRIMARY KEY,
    track_name VARCHAR(200),
    album_id VARCHAR(50),
    disc_number INT,
    track_number INT,
    duration_ms INT,
    is_explicit BOOLEAN,
    popularity INT,
    preview_url TEXT,
    isrc VARCHAR(50),
    FOREIGN KEY (album_id) REFERENCES Album(album_id)
);

-- Weak entity of tracks (1:1 relationship)
CREATE TABLE AudioFeature (
    track_id VARCHAR(75) PRIMARY KEY,
    danceability FLOAT,     -- Some of these are actually ints but are being stored as floats so ill just keep for data integrity
    energy FLOAT,
    key_signature FLOAT,
    loudness FLOAT,
    mode FLOAT,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    time_signature FLOAT,
    FOREIGN KEY (track_id) REFERENCES Track(track_id) ON DELETE CASCADE -- if a track is deleted, its audio features should also be deleted
);

-- M:N relationship between artists and tracks
CREATE TABLE Composes (
    artist_id VARCHAR(50),
    track_id VARCHAR(75),
    PRIMARY KEY (artist_id, track_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (track_id) REFERENCES Track(track_id)
);

-- M:N relationship between listeners and tracks
CREATE TABLE Likes (
    listener_id INTEGER,
    track_id VARCHAR(75),
    liked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- when was the track liked? (current time UTC by default)
    PRIMARY KEY (listener_id, track_id),
    FOREIGN KEY (listener_id) REFERENCES Listener(listener_id),
    FOREIGN KEY (track_id) REFERENCES Track(track_id)
);

-- M:N relationship between listeners and artists
CREATE TABLE Follows (
    listener_id INTEGER,
    artist_id VARCHAR(50),
    PRIMARY KEY (listener_id, artist_id),
    FOREIGN KEY (listener_id) REFERENCES Listener(listener_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);


