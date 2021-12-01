DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    genre VARCHAR(255),
    author_id INT REFERENCES authors(id)
);

INSERT INTO authors (name) VALUES ('Stephen');
INSERT INTO books (title,year, genre, author_id) VALUES ('The Shinning', 1980, 'Horror',1);