python3 ./1_dataformatting.py
docker cp ./call_put_data/call_usa_options.csv posgre_sql://var/lib/postgresql/data/
# Opening of the database and creation of the table to store the dataset
docker exec -i posgre_sql \
psql -U user -d time_series < ./query_file.sql
docker exec -it call_prediction-python_app-1 python3 2_model_train_save.py
docker cp call_prediction-python_app-1://app/model_for_inference_gcp.pkl ./output
docker cp call_prediction-python_app-1://app/prediction_call_put.npy ./output
docker cp call_prediction-python_app-1://app/test_data.npy ./output











