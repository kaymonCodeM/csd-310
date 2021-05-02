use whatabook;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
user_id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY(user_id),
first_name VARCHAR(75) NOT NULL,
last_name VARCHAR(75) NOT NULL
);

CREATE TABLE book(
book_id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY(book_id),
book_name VARCHAR(200) NOT NULL,
detailsV VARCHAR(500),
author VARCHAR(200) NOT NULL
);

CREATE TABLE wishlist(
wishlist_id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY(wishlist_id),
user_id INT NOT NULL,
CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES user(user_id),
book_id INT NOT NULL,
CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES book(book_id)
);

CREATE TABLE store(
store_id INT NOT NULL PRIMARY KEY,
locale VARCHAR(500) NOT NULL);

-- This is a coffee shop in lincoln called The Mill
INSERT INTO store(store_id,locale) VALUES (1,'4736 Prescott Ave, Lincoln, NE 68506');

/*
https://www.barnesandnoble.com/b/books/barnes-nobles-best-books-of-2020/barnes-nobles-best-fiction-of-2020/_/N-29Z8q8Z2v0i
This website is where I got the information of data to put into my daatabase.
The details are direct quotes towards the Barnes and Nobles website including the book names and authors.
*/
INSERT INTO book(book_name,detailsV,author) VALUES ('The Vanishing Half','ONE OF BARACK OBAMA''S FAVORITE BOOKS OF THE YEAR','Brit Bannett');
INSERT INTO book(book_name,detailsV,author) VALUES ('Deacon King Kong','A Washington Post Notable Novel','James McBride');
INSERT INTO book(book_name,detailsV,author) VALUES ('Hamnet','WINNER OF THE NATIONAL BOOK CRITICS CIRCLE AWARD','Maggie O''Farrell');
INSERT INTO book(book_name,detailsV,author) VALUES ('Mexican Gothic','NEW YORK TIMES BESTSELLER','Silvia Moreno-Garcia');
INSERT INTO book(book_name,detailsV,author) VALUES ('Leave the World Behind','A magnetic novel about two families, strangers to each other, who are forced together on a long weekend gone terribly wrong','Rumaan Alam');
INSERT INTO book(book_name,detailsV,author) VALUES ('The Evening and the Morning','A thrilling and addictive new novel—a prequel to The Pillars of the Earth—set in England at the dawn of a new era: the Middle Ages','Ken Follett');
INSERT INTO book(book_name,detailsV,author) VALUES ('The Cold Millions','The author of the #1 New York Times bestseller Beautiful Ruins','Jess Walter');
INSERT INTO book(book_name,detailsV,author) VALUES ('Memorial','A GOOD MORNING AMERICA BOOK CLUB PICK','Bryan Washington');
INSERT INTO book(book_name,detailsV,author) VALUES ('The Office of Historical Corrections','WINNER OF THE 2021 JOYCE CAROL OATES PRIZE','Danielle Evans');

-- INSERTING USERS
INSERT INTO user(first_name,last_name) VALUES ('Hannah','Ashburn');
INSERT INTO user(first_name,last_name) VALUES ('Sawyer', 'JAY');
INSERT INTO user(first_name,last_name) VALUES ('Kaymon', 'McCain');

-- INSERT WISHLIST
INSERT INTO wishlist(user_id,book_id) VALUES (1,7);
INSERT INTO wishlist(user_id,book_id) VALUES (2,5);
INSERT INTO wishlist(user_id,book_id) VALUES (3,1);
