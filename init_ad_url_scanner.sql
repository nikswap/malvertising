CREATE TABLE ad_url_hash_found (
        id INTEGER PRIMARY KEY AUTOINCREMENT
    ,   domain CHAR(100)
    ,   ad_hash CHAR(50)
    ,   ad_url_found CHAR(300)
    ,   added_at datetime default current_timestamp
);

CREATE TABLE ad_url_hash (
        id INTEGER PRIMARY KEY AUTOINCREMENT
    ,   domain CHAR(100)
    ,   ad_hash CHAR(50)
    ,   added_at datetime default current_timestamp
);
