python3 ./1_dataformatting.py
docker cp ./call_put_data/call_usa_options.csv posgre_sql://var/lib/postgresql/data/
# Opening of the database and creation of the table to store the dataset
docker exec -i posgre_sql \
psql -U user -d time_series < ./query_file.sql
docker exec -it python_app python3 2_model_train_save.py
docker cp python_app://app/model_for_inference_gcp.pkl ./output
docker cp python_app://app/custom_attention.weights.h5 ./output
docker cp python_app://app/prediction_call_put.npy ./output
docker cp python_app://app/test_data.npy ./output
docker cp python_app://app/loss_function.npy ./output
docker cp python_app://app/norm_gradient.npy ./output










