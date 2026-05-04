import psycopg2

import joblib

import pandas as pd

import numpy as np

from library import AttentionLayer, Architecture

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input
from tensorflow.keras.models import Model

tf.random.set_seed(1)
tf.keras.utils.set_random_seed(1)   
tf.config.experimental.enable_op_determinism()




connexion =  psycopg2.connect(user="user", host="posgre_sql", password ="FelixRegina%1234", database="time_series", port = 5432)
curr = connexion.cursor()
curr.execute("SELECT * FROM {0}".format("call_data"))
data = pd.DataFrame(curr.fetchall())

col_names = []
for elt in curr.description:
    col_names.append(elt[0])

data= data.rename(columns={i:col_names[i] for i in range(len(col_names))})

print(data.head())

#data = pd.read_csv("/app/call_usa_options.csv")

train = data.iloc[:9000,:]
x_train = train[[col for col in data.columns if col not in ["expiration","strike", "bid_size","ask_size"]]].to_numpy()
print("The columns for training are {0}".format([col for col in data.columns if col not in ["expiration","strike", "bid_size","ask_size"]]))
y_train = train[["strike"]].to_numpy()
[nrows,ncols] = x_train.shape
x_train = x_train.reshape(nrows, ncols, 1)
x_train = x_train.astype(np.float32)
y_train = y_train.astype(np.float32)
print(x_train.shape)
print(y_train.shape)

shape = data.shape[1]
architecture = Architecture(shape)
architecture.model_recovery()
architecture.ml_model.fit(x_train, y_train, epochs=100, shuffle=False)
joblib.dump(architecture.ml_model, 'model_for_inference_gcp.pkl')

# Test of the model
test = data.iloc[9000:,:]
x_test = test[[col for col in data.columns if col not in ["expiration","strike", "bid_size","ask_size"]]].to_numpy()
y_test = test[["strike"]].to_numpy()
[nrows,ncols] = x_test.shape
x_test = x_test.reshape(nrows, ncols, 1)
x_test = x_test.astype(np.float32)
y_test = y_test.astype(np.float32)
prediction = architecture.ml_model.predict(x_test)
print(prediction.shape)
np.save('prediction_call_put.npy', prediction)
np.save('test_data.npy', y_test)







        