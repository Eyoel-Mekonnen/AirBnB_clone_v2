-- creates database
-- Grants permission to database and user

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
<<<<<<< HEAD
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db .* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema .* TO hbnb_dev@localhost;
=======
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
>>>>>>> ef3b3cf29f517e48855a4c02104d18532fba330b
