-- demo_queries.sql
-- Required demo queries for Step 3

-----------------------------------------------------
-- INSERT demo: add a new listener and sample likes
-----------------------------------------------------
INSERT INTO Listener (username, password)
VALUES ('demo_username', 'password123')
ON CONFLICT (listener_id) DO NOTHING;

-- Demo likes (top 3 most popular tracks)
WITH top_tracks AS (
SELECT track_id FROM Track ORDER BY popularity DESC NULLS LAST LIMIT 3
)
INSERT INTO Likes (listener_id, track_id)
SELECT 1, track_id FROM top_tracks
ON CONFLICT DO NOTHING;

-- Demo follow (first 2 artists)
WITH some_artists AS (
SELECT artist_id FROM Artist LIMIT 2
)
INSERT INTO Follows (listener_id, artist_id)
SELECT 1, artist_id FROM some_artists
ON CONFLICT DO NOTHING;

-----------------------------------------------------
-- UPDATE demo: increase popularity of a track
-----------------------------------------------------
UPDATE Track
SET popularity = COALESCE(popularity, 0) + 1
WHERE track_id = (
SELECT track_id FROM Track ORDER BY popularity DESC NULLS LAST LIMIT 1
);

-----------------------------------------------------
-- DELETE demo: unlike one track
-----------------------------------------------------
DELETE FROM Likes
WHERE listener_id = 1
AND track_id = (
SELECT track_id FROM Track ORDER BY popularity DESC NULLS LAST LIMIT 1
);

-----------------------------------------------------
-- SELECT demo #1: Top 10 energetic tracks
-----------------------------------------------------
SELECT t.track_name AS track_name, a.album_name AS album_name, af.energy
FROM Track t
JOIN Album a ON t.album_id = a.album_id
JOIN AudioFeature af ON af.track_id = t.track_id
ORDER BY af.energy DESC
LIMIT 10;

-----------------------------------------------------
-- SELECT demo #2: Average danceability by album
-----------------------------------------------------
SELECT a.album_name AS album_name, AVG(af.danceability) AS avg_danceability, COUNT(*) AS num_tracks
FROM Track t
JOIN Album a ON t.album_id = a.album_id
JOIN AudioFeature af ON af.track_id = t.track_id
GROUP BY a.album_name
HAVING COUNT(*) >= 5
ORDER BY avg_danceability DESC
LIMIT 10;
