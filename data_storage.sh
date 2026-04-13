docker cp /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/call_put_data/call_usa_options.csv posgre_sql://var/lib/postgresql/data/
# Opening of the database and creation of the table to store the dataset
docker exec -i posgre_sql \
psql -U user -d time_series < /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/Programmes/query_file.sql










