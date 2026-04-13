#!/bin/bash

docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker-compose -f /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/Programmes/docker-compose.yml up
docker cp /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/call_put_data/call_usa_options.csv posgre_sql://var/lib/postgresql/data/
docker exec -it posgre_sql psql -U user -d time_series






