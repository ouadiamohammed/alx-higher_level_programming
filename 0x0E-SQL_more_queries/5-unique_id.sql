-- creates table with unique default id and name
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));