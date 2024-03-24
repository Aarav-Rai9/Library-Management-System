-- SQL Commands to create tables
CREATE TABLE category (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    status VARCHAR(255)
);

CREATE TABLE book (
    id INT PRIMARY KEY,
    category_id INT,
    bookname VARCHAR(255),
    status VARCHAR(255),
    author VARCHAR(255),
    rating FLOAT,
    cost FLOAT,
    FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE library_card (
    id INT PRIMARY KEY,
    student_id INT,
    book_id INT,
    FOREIGN KEY (book_id) REFERENCES book(id)
);

CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    grade VARCHAR(255),
    library_card_id INT,
    FOREIGN KEY (library_card_id) REFERENCES library_card(id)
);
