CREATE TABLE IF NOT EXISTS users(
    id SERIAL,
    name VARCHAR(20),
    last_name VARCHAR(20) DEFAULT ''
);
