-- Para crear la tabla "personas" en la BD:

CREATE TABLE personas (
      dni VARCHAR(10) NOT NULL,
      nombre VARCHAR(50) NOT NULL,
      apellido VARCHAR(50) NOT NULL,
      fecha_nacimiento DATE NOT NULL,
      PRIMARY KEY (dni)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
