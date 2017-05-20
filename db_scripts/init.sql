CREATE DATABASE IF NOT EXISTS microurl;

GRANT ALL PRIVILEGES ON microurl.* TO 'microurl'@'%' IDENTIFIED BY "password";
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS Micros (
    ID CHAR(64) PRIMARY KEY,
    micro_link TEXT NOT NULL,
    real_link TEXT NOT NULL,
    creation INT NOT NULL,
    expiration INT NOT NULL,
    hits INT DEFAULT 0,
    public BOOL NOT NULL
);
