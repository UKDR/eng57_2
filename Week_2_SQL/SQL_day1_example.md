# Week 2  SQL Day 1
## Monday 11/05/2020
### Practical Example


``` Bash

-- creates the database
CREATE DATABASE del_db

-- use the database
USE del_db

-- choose table according to data
CREATE TABLE film_table
(
    -- The INT identitiy is used to increment down so
    -- (1,1) = Starts at 1 and steps by 1
    film_id INT IDENTITY(1,1),

    film_name VARCHAR(20),
    film_type VARCHAR(20),
    date_of_release DATE,
    director VARCHAR(20),
    writer VARCHAR(20),
    star VARCHAR(20),
    film_language VARCHAR(14),
    official_website VARCHAR(60),

    -- we used max because plot summary could be massive
    plot_summary VARCHAR(MAX)

    --  we can choose a primary that is unique. Film_id is unique in the table
    PRIMARY KEY (film_id)

)



CREATE TABLE film_orders
(
    --  film_id becomes the foreign key in the second table
    film_id INT,
    -- each table needs a primary key
    order_id INT PRIMARY KEY IDENTITY(1,1),
    --  INT  doesn't need any values
    number_of_tickets INT,
    cost_of_tickets DECIMAL(5,2)
    -- references shows the foreign keys' table and the foreign key
    FOREIGN KEY (film_id) REFERENCES film_table(film_id) ON DELETE CASCADE
    -- above atatement is combinign the tables together


)

-- deletes the table
DROP TABLE film_orders

-- adding values in order of table creation
INSERT INTO film_table
(
    film_name, film_type, date_of_release, director, writer, star, film_language, official_website, plot_summary
)
VALUES
(
    'bad boys', 'Action/Comedy', '1995-04-27', 'Michael Bay', 'George Gallo', 'Will Smith', 'English', 'www.badboys.co.uk', 'Marcus, a family man, and Mike, a ladies man, are partners in the Miami police. Things get complicated when they assume each others identity while investigating a drug deal'
)


-- shows the final product
SELECT * FROM film_table

-- once the table is made, use ALTER to change something.
-- this adds an extra column called film_rating
ALTER TABLE film_table
ADD film_rating INT(1);

-- Drops the column called film rating

ALTER TABLE film_table
DROP COLUMN film_rating;


--ON DELETE CASCADE-AUTOMATIC

-- shows the film table
SP_HELP film_table

-- deletes the whole table
DROP TABLE film_table

```
