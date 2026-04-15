docker cp /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/call_put_data/call_usa_options.csv posgre_sql://var/lib/postgresql/data/
# Opening of the database and creation of the table to store the dataset
docker exec -i posgre_sql \
psql -U user -d time_series < /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/Programmes/query_file.sql
docker exec -it programmes-python_app-1 python3 2_model_train_save.py
docker cp programmes-python_app-1://app/model_for_inference_gcp.pkl /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction
docker cp programmes-python_app-1://app/prediction_call_put.npy /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction
docker cp programmes-python_app-1://app/test_data.npy /Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction











