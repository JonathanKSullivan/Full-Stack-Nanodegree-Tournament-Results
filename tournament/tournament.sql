-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE DATABASE tournament;
\c tournament
CREATE TABLE players  (
   id         SERIAL    NOT NULL,
   name       TEXT    NOT NULL,
   wins       INT    NOT NULL,
   matches    INT   NOT NULL
);

CREATE TABLE matches  (
   id           SERIAL     NOT NULL,
   winner       INT    NOT NULL,
   loser        INT    NOT NULL
);
