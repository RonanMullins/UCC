DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY, 
    password TEXT NOT NULL 
);

-- INSERT INTO users (user_id, password) VALUES ('admin','123');

DROP TABLE IF EXISTS contact;

CREATE TABLE contact
(
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
);

DROP TABLE IF EXISTS instruments;

CREATE TABLE instruments
(
    instrument_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT NOT NULL,
    image TEXT NOT NULL

);

INSERT INTO instruments (name, category, price, description, image)
VALUES

    --electric guitars

    ('Fender Stratocaster','electric guitar', 749.99, 'Know for its versatility, the Fender Stratocaster can handle any genre of music.','fender_stratocaster.jpg'),
    ('Squier Stratocaster','electric guitar', 179.99,'Designed by Fender, this guitar offers the Fender Stratocaster experience at an affordable price.','squier_stratocaster.jpg'),
    ('Gibson Les Paul','electric guitar', 2699.99,'The Les Paul is an iconic guitar in rock and heavy metal music.','gibson_lp.jpg'),
    ('Epiphone Les Paul','electric guitar', 549.99, 'A timeless classic made affordable. It delivers a warm tone of traditional rock, along with that nostalic look.','epiphone_lp.jpg'),
    

    --acoustic guitars

    ('Martin acoustic guitar','acoustic guitar', 999.99, 'The Martin acoustic guitar offers a timeless warm tone.','martin_acoustic.jpg'),
    ('Taylor acoustic guitar','acoustic guitar', 845.99,'The Taylor acoustic guitar gives clear and punchy tones, perfect for playing with other instruments.','taylor_acoustic.jpg'),
    ('Fender acoustic guitar','acoustic guitar', 129.99, 'This budget friendly guitar is perfect for beginners. Its easy playing and sounds great!','fender_acoustic.jpg'),
    ('Yamaha acoustic guitar','acoustic guitar', 409.99,'This Yamaha is a joy to play and hear. A great all-rounder guitar that is a joy to play and hear.','yamaha_acoustic.jpg'),

    --wind instruments 

    ('Kazoo','wind', 1.99, 'It''s a Kazoo','kazoo.jpg'),
    ('Tin Whistle','wind', 28.99,'This high quality Tin Whistle produces the perfect whislte sound.','tin_whistle.jpg'),
    ('John Packer Saxophone','wind', 349.99, 'This John Packer saxophone is perfect for beginners. It offers a remarkable vibrant tone for its price point.','jp_saxophone.jpg'),
    ('Yamaha Flute','wind', 632.99,'Yamaha flutes are characterised by their excellent response and intonation.','yamaha_flute.jpg');

DROP TABLE IF EXISTS orders;

CREATE TABLE orders
(   
    order_no INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    address TEXT NOT NULL,
    delivery_type TEXT NOT NULL,
    delivery_date TEXT NOT NULL,
    instrument_id INTEGER NOT NULL,
    names TEXT NOT NULL,
    categories TEXT NOT NULL,
    prices TEXT NOT NULL,
    total REAL NOT NULL
);

SELECT * FROM users;
SELECT * FROM contact;
SELECT * FROM instruments;
SELECT * FROM orders;