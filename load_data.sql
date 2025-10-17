-- load_data.sql
-- Run from the folder where the CSVs are located:
-- psql spotify -f load_data.sql

\COPY artist (artist_id,name)
FROM 'artists.csv' WITH CSV HEADER;

\COPY album (album_id,name,release_date,label,copyrights)
FROM 'albums_cleaned.csv' WITH CSV HEADER;

\COPY track (track_id,name,album_id,disc_number,track_number,duration_ms,preview_url,is_explicit,popularity,isrc)
FROM 'tracks_cleaned.csv' WITH CSV HEADER;

\COPY audiofeature (track_id,danceability,energy,key_signature,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,time_signature)
FROM 'audio_features_cleaned.csv' WITH CSV HEADER;