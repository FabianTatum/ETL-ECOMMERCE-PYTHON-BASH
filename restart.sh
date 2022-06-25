#!/bin/bash

docker compose down

sudo rm -r ./data-warehouse/volume

sudo rm ./data-ouput/*.csv
sudo rm ./data-ouput/old/*.csv
sudo mv ./data-input/*.csv ./deltas/
sudo mv ./data-input/old/*.csv ./data-input/

sudo rm logs.txt

touch logs.txt

