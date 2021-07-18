-- creates a table users
CREATE TABLE IF NOT EXISTS `users` (
       `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       `email` VARCHAR(256) NOT NULL UNIQUE,
       `name` VARCHAR(256)
);
