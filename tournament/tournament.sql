-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE restaurants(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
);

CREATE TABLE Match(
   ID INT PRIMARY KEY     NOT NULL,
   WINNERID       TEXT    NOT NULL,
   LOSERID        TEXT    NOT NULL,
);
