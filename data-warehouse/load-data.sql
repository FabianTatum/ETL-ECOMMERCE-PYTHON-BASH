USE store_datawarehouse;

LOAD DATA INFILE '/var/lib/mysql/data-output/Clientes.csv' 
INTO TABLE clientes 
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/Compra.csv' 
INTO TABLE compras
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/CompraOutliers.csv' 
INTO TABLE compras_outliers
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/Gastos.csv' 
INTO TABLE gastos
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/GastosOutliers.csv' 
INTO TABLE gastos_outliers
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/Localidades.csv' 
INTO TABLE localidades
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/Proveedores.csv' 
INTO TABLE proveedores
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/Sucursales.csv'
INTO TABLE sucursale
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY ''
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/Ventas.csv'
INTO TABLE ventas
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY ''
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE '/var/lib/mysql/data-output/VentasOutliers.csv'
INTO TABLE ventas_outlier
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY ''
LINES TERMINATED BY '\n' IGNORE 1 LINES;
