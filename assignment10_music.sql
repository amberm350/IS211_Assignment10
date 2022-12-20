DROP SCHEMA IF EXISTS music;
CREATE SCHEMA music;

DROP TABLE IF EXISTS music_artists;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS songs;

CREATE TABLE music_artists(artist_id int, artist_name varchar(50);

INSERT INTO music_artists(artist_id, artist_name) 
VALUES [(1, "Lady Gaga"),
(2, "Katy Perry")
];

CREATE TABLE albums(album_id int, album_name varchar(100), FOREIGN KEY artist_id REFERENCES music_artists(artist_id));

INSERT INTO albums(album_id, album_name, artist_id);
VALUES [(1, "The Fame", 1),
(2, "Born this Way", 1),
(3, "Teenage Dream", 2),
(4, "Prism", 2)
];

CREATE TABLE songs(song_id int, song_name varchar(100, track_number int, time int, FOREIGN KEY album_id REFERENCES albums(album_id);

INSERT INTO songs(song_id, song_name, track_number, time, album_id);
VALUES [(1, "Pokerface",4,237),
(2, "Just Dance",1,241),
(3, "Born this way", 2,260),
(4, "Judas", 4,249),
(5, "Teenage Dream", 1,223),
(6, "Firework", 4,223),
(7, "Roar", 1, 227),
(8, "Unconditionally", 5,228)
];

SELECT ar.artist_name, al.album_name, s.song_name, s.tracknumber, s.time FROM artist ar INNER JOIN albums al ON ar.artist_id = al.artist_id INNER JOIN songs s ON al.album_id = s.album_id