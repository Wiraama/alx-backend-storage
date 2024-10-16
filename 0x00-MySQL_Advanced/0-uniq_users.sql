-- script to create table user with the requirements
-- if table exist it will fail
-- to be executed on any database
CREATE TABLE IF NOT EXISTS user (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
);
