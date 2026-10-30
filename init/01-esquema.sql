CREATE TABLE IF NOT EXISTS productos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  precio NUMERIC(10,2)
);

INSERT INTO productos (nombre, precio) VALUES
  ('Teclado', 25.50),
  ('Mouse', 12.00);
