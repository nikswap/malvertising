CREATE TABLE domainnames (
        id INTEGER PRIMARY KEY AUTOINCREMENT
    ,   domain CHAR(100)
    ,   http_status CHAR(100)
    ,   added_at datetime default current_timestamp
);

CREATE TABLE forwards (
        id INTEGER PRIMARY KEY AUTOINCREMENT
    ,   domainid INTEGER
    ,   forward_to CHAR(100)
    ,   added_at datetime default current_timestamp
);



