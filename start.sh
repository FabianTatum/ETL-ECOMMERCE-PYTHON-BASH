#!/bin/bash

### Preparando servicios

if [[ ! -z $1 ]];
then
    sudo mv ./data-input/*.csv ./data-input/old
    ### Pasar archivos de salida antiguos a carpeta old
    sudo mv ./deltas/*.csv ./data-input/
    sudo mv ./data-ouput/*.csv ./data-ouput/old
else
    sudo service mysql restart
    ### Levantamiento de container de MariaDB para nuestro datawarehouse
    sudo docker compose up -d
    ### Espera de 15 segundos
    for ((i=10; i>0; i--)); do
        sleep 2 & 
        echo "Constuyendo volumen, Espere..." 
        wait 
    done
    echo "--------------------------------"
    echo "Iniciando Base de Datos MariaDB en Docker"
    echo "--------------------------------"

    echo "--------------------------------"
    echo "Creación de Tablas En Data Warehouse Iniciada"
    echo "--------------------------------"

    mariadb -h 127.0.0.1 -P 3333 -u root --password=1234 < "$PWD/data-warehouse/Schema.sql"

    echo "--------------------------------"
    echo "Creación de Tablas de Data Warehouse Finalizada"
    echo "--------------------------------"
fi

### Inicio de ETL con Python
python3 main.py

echo "--------------------------------"
echo "Carga de datos en Data Warehouse Iniciada"
echo "--------------------------------"

docker cp ./data-ouput/ db-maria:/var/lib/mysql

sleep 1

mariadb -h 127.0.0.1 -P 3333 -u root --password=1234 < "$PWD/data-warehouse/load-data.sql"

echo "--------------------------------"
echo "Carga de datos en Data Warehouse Finalizada"
echo "--------------------------------"