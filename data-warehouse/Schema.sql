DROP SCHEMA IF EXISTS store_datawarehouse;
CREATE SCHEMA store_datawarehouse;

USE store_datawarehouse;

DROP TABLE IF EXISTS clientes;
CREATE TABLE IF NOT EXISTS clientes (
	Cliente_id			INTEGER,
	Provincia			VARCHAR(50),
	Nombres				VARCHAR(80),
	Domicilio			VARCHAR(150),
	Telefono			VARCHAR(30),
	Edad				INTEGER,
	Localidad			VARCHAR(80),
	Latitud				DECIMAL(13,10),
	Longitud			DECIMAL(13,10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

DROP TABLE IF EXISTS compras;
CREATE TABLE IF NOT EXISTS compras (
  Compra_id				INTEGER,
  Fecha 				DATE,
  Producto_id			INTEGER,
  Proveedor_id			INTEGER,
  Cantidad				INTEGER,
  Precio				DECIMAL(10,2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

DROP TABLE IF EXISTS compras_outliers;
CREATE TABLE IF NOT EXISTS compras_outliers (
  Compra_id				INTEGER,
  Fecha 				DATE,
  Producto_id			INTEGER,
  Proveedor_id			INTEGER,
  Cantidad				INTEGER,
  Precio				DECIMAL(10,2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;


DROP TABLE IF EXISTS gastos;
CREATE TABLE IF NOT EXISTS gastos (
  	Gasto_id 		INTEGER,
    Fecha			DATE,
  	Sucursal_id 	INTEGER,
  	TipoGasto_id 	INTEGER,
  	Monto 			DECIMAL(10,2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;	

DROP TABLE IF EXISTS gastos_outliers;
CREATE TABLE IF NOT EXISTS gastos_outliers (
  	Gasto_id 		INTEGER,
    Fecha			DATE,
  	Sucursal_id 	INTEGER,
  	TipoGasto_id 	INTEGER,
  	Monto 			DECIMAL(10,2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;	

DROP TABLE IF EXISTS localidades;
CREATE TABLE IF NOT EXISTS localidades (
	Codigo_Censal	INTEGER,
	Localidad		VARCHAR(50),
	Municipio		VARCHAR(80),
	Departamento	VARCHAR(80),
	Provincia		VARCHAR(80),
	Longitud		DECIMAL(13,10),
	Latitud			DECIMAL(13,10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;	

DROP TABLE IF EXISTS proveedores;
CREATE TABLE IF NOT EXISTS proveedores (
	Proveedor_id		INTEGER,
	Nombres				VARCHAR(80),
	Direccion			VARCHAR(150),
	Localidad			VARCHAR(80),
	Provincia			VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

DROP TABLE IF EXISTS sucursales;
CREATE TABLE IF NOT EXISTS sucursales (
	Sucursal_id		INTEGER,
	Sucursal		VARCHAR(40),
	Direccion		VARCHAR(150),
	Localidad		VARCHAR(80),
	Provincia		VARCHAR(50),
	Latitud			DECIMAL(13,10),
	Longitud		DECIMAL(13,10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

DROP TABLE IF EXISTS ventas;
CREATE TABLE IF NOT EXISTS ventas (
  Venta_id			INTEGER,
  Fecha 			DATE,
  Fecha_Entrega		DATE,
  Canal_id			INTEGER, 
  Cliente_id		INTEGER, 
  Sucursal_id		INTEGER,
  Empleado_id		INTEGER,
  Producto_id		INTEGER,
  Precio			DECIMAL(10,2),
  Cantidad			INTEGER
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

DROP TABLE IF EXISTS ventas_outliers;
CREATE TABLE IF NOT EXISTS ventas_outliers (
  Venta_id			INTEGER,
  Fecha 			DATE,
  Fecha_Entrega		DATE,
  Canal_id			INTEGER, 
  Cliente_id		INTEGER, 
  Sucursal_id		INTEGER,
  Empleado_id		INTEGER,
  Producto_id		INTEGER,
  Precio			DECIMAL(10,2),
  Cantidad			INTEGER
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;


SHOW TABLES;