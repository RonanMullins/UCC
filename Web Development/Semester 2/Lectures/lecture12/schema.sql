DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY, 
    password TEXT NOT NULL 
);

DROP TABLE IF EXISTS wines;

CREATE TABLE wines
(
    wine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT

);

INSERT INTO wines (name, price, description)
VALUES
    ('Dingo Dribble', 12.33, 'Goes well with snake steak'),
    ('Emu Emission', 17.99,'A spunky wine for every ocassion!');
