DROP TABLE IF EXISTS demo;
CREATE TABLE demo
(
    id   serial PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO demo(name)
VALUES ('minions');