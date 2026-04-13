#!/bin/bash
# deletion of all of the existing containers
docker rm -vf $(docker ps -aq)
# deletion of all of the existing images
docker rmi -f $(docker images -aq)
# creation of the new docker containers
docker-compose -f /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/Programmes/docker-compose.yml up








