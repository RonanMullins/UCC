DROP TABLE IF EXISTS gigs;

CREATE TABLE gigs
(
    gig_id INTEGER PRIMARY KEY AUTOINCREMENT,
    band TEXT NOT NULL,
    gig_date TEXT NOT NULL
);

INSERT INTO gigs (band, gig_date)
VALUES ('Decaying Shroom', '2022-01-12'),
        ('Prickly Muse', '2022-03-20');