-- load_data.sql
-- Run from the folder where the CSVs are located:
-- psql spotify -f load_data.sql

\COPY artist (artist_id,artist_name) FROM 'artists_cleaned.csv' WITH CSV HEADER;

\COPY album (album_id,album_name,release_date,label,copyrights) FROM 'albums_cleaned.csv' WITH CSV HEADER;

\COPY track (track_id,track_name,album_id,disc_number,track_number,duration_ms,preview_url,is_explicit,popularity,isrc) FROM 'tracks_cleaned.csv' WITH CSV HEADER;

\COPY audiofeature (track_id,danceability,energy,key_signature,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,time_signature) FROM 'audio_features_cleaned.csv' WITH CSV HEADER;

\COPY composes (track_id, artist_id) FROM 'composes_cleaned.csv' WITH CSV HEADER;

-- Insert sample listeners
INSERT INTO Listener (username, password) VALUES
('zebra_apple', 'x9v3pL!'),
('blueberry77', 'qW3rTy!'),
('snapdragon', 'p@ssW0rd'),
('jellyfish', 'a1b2c3d4'),
('taco_bell', 'zXcVbNm!'),
('random_dude', 'h3ll0W0rld'),
('pineapple', 'kLmNoP!'),
('starlight', 'uNiVeRsE1'),
('butterfly', 'fLyAw@y'),
('dragonfruit', 'tR0p1c@l'),
('mystic_owl', 'n1ghtH@wk'),
('cosmic_ray', 'g@l@xy99'),
('shadowfox', 'f0xH0le!'),
('electric_eel', 'sPaRk!eL'),
('honeybadger', 'b@dG3r!'),
('wildcat', 'p@nth3r'),
('silvermoon', 'm00nL1ght'),
('golden_sun', 'sUnSh1ne!'),
('stormcloud', 'r@1nDr0p'),
('firefly', 'gL0wW0rm!');

-- Insert random likes for our sample listeners
INSERT INTO Likes (listener_id, track_id) VALUES
(1, 'spotify:track:1XAZlnVtthcDZt2NI1Dtxo'),
(1, 'spotify:track:1QEEqeFIZktqIpPI4jSVSF'),
(1, 'spotify:track:2RjQ82MtgcR8sgOL2RJQAs'),
(1, 'spotify:track:64VKnOE7xkcDBlShRUpJgd'),
(1, 'spotify:track:4WCn0AgWKBJRjuFvHSfle8'),
(1, 'spotify:track:00FRRwuaJP9KimukvLQCOz'),
(1, 'spotify:track:3vZO25GdYuqFrR1kzZADnp'),
(1, 'spotify:track:4oiwzl01mQDqRWFIa7VI3d'),
(1, 'spotify:track:2xEyclHzLJU0CwKiQ4DwJ4'),
(1, 'spotify:track:5TrIHwld2ERD75B5TfceEt'),
(2, 'spotify:track:6a8GbQIlV8HBUW3c6Uk9PH'),
(3, 'spotify:track:2hdNya0b6Cc2YJ8IyaQIWp'),
(4, 'spotify:track:1NXUWyPJk5kO6DQJ5t7bDu'),
(5, 'spotify:track:5Nu1cp2yi4TlZF4KTmElFD'),
(5, 'spotify:track:1ZvS1DmW1cF0oknYGCVNK7'),
(5, 'spotify:track:43Ui9JiJXhjznzdOTAansW'),
(5, 'spotify:track:051wt8AyLFgYnVuberd3vO'),
(5, 'spotify:track:72WZtWs6V7uu3aMgMmEkYe'),
(6, 'spotify:track:4bEb3KE4mSKlTFjtWJQBqO'),
(7, 'spotify:track:0d2iYfpKoM0QCKvcLCkBao'),
(8, 'spotify:track:5LjSxAIKwyZvQqJ04ZQ0Da'),
(9, 'spotify:track:00qOE7OjRl0BpYiCiweZB2'),
(10, 'spotify:track:3OalxlWH0v14kyBcNBMINt'),
(11, 'spotify:track:0CtkjgZpkgnW7U6WmHsakD'),
(12, 'spotify:track:3NLrRZoMF0Lx6zTlYqeIo4'),
(13, 'spotify:track:09tyJ0VvbLty84iHIV3WQn'),
(14, 'spotify:track:73JqQIGZUZxCVfY54RSpCH'),
(15, 'spotify:track:6K8qKeWo5MsFED7wCR6Kop'),
(16, 'spotify:track:3tP0kdmWRSqmJAt4nR3ykw'),
(17, 'spotify:track:2760p399WNJLX9LGBkjL4Z'),
(18, 'spotify:track:5yJCo7EewUcX9qj5nnk9O2'),
(19, 'spotify:track:2uiyVyP0Rvl0MgB8ehoc07'),
(20, 'spotify:track:2J22VgQALSoekF3KCj1nIk');

-- Insert random follows for our sample listeners
INSERT INTO Follows (listener_id, artist_id) VALUES
(1, 'spotify:artist:6dYrdRlNZSKaVxYg5IrvCH'),
(1, 'spotify:artist:0CrCKxXekxMpkYfMEf8mca'),
(1, 'spotify:artist:69YKwunlA0xl2yMS12cyMu'),
(1, 'spotify:artist:1NFdLYtu29c6NKzd49BdEd'),
(2, 'spotify:artist:0TnOYISbd1XYRBk9myaseg'),
(3, 'spotify:artist:26dSoYclwsYLMAKD3tpOr4'),
(4, 'spotify:artist:1SQRv42e4PjEYfPhS0Tk9E'),
(5, 'spotify:artist:22bE4uQ6baNwSHPVcDxLCe'),
(5, 'spotify:artist:6XpaIBNiVzIetEPCWDvAFP'),
(5, 'spotify:artist:6I3M904Y9IwgDjrQ9pANiB'),
(5, 'spotify:artist:3aVoqlJOYx31lH1gibGDt3'),
(6, 'spotify:artist:08GQAI4eElDnROBrJRGE0X'),
(7, 'spotify:artist:5CiGnKThu5ctn9pBxv7DGa'),
(8, 'spotify:artist:3PhoLpVuITZKcymswpck5b'),
(12, 'spotify:artist:2RTUTCvo6onsAnheUk3aL9'),
(13, 'spotify:artist:320EPCSEezHt1rtbfwH6Ck'),
(14, 'spotify:artist:3sFhA6G1N0gG1pszb6kk1m'),
(15, 'spotify:artist:6eUKZXaKkcviH0Ku9w2n3V'),
(16, 'spotify:artist:2rmQ5EEAIkloNGWdGlvCYM'),
(17, 'spotify:artist:2C0Cu6wbLYQyXl8MDwH2JE'),
(18, 'spotify:artist:4Z1spMbjudmqwjyBPleP7s'),
(19, 'spotify:artist:7Jbs4wPCLaKXPxrTxZ2zaa'),
(20, 'spotify:artist:0SCbttzoZTnLFebDYmAWCm');
