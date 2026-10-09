CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

INSERT INTO products (name, price) VALUES
    ('Laptop', 55000.00),
    ('Headphones', 2500.00),
    ('Keyboard', 1800.00);
