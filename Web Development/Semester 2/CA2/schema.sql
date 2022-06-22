DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY, 
    password TEXT NOT NULL 
);

DROP TABLE IF EXISTS leaderboard;

CREATE TABLE leaderboard
(
    user_id TEXT NOT NULL, 
    score INT NOT NULL,
    time FLOAT NOT NULL
);

SELECT * FROM users;
SELECT * FROM leaderboard;
