CREATE DATABASE billing_system;
USE billing_system;

CREATE TABLE bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100),
    quantity INT,
    price FLOAT,
    total FLOAT
);
