-- Create databse if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

-- set password for the user
ALTER USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges on performance_schema to hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
