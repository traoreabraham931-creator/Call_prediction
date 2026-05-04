import psycopg2

import pandas as pd

import os

import numpy as np

import json

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input
from tensorflow.keras.models import Model


tf.random.set_seed(1)
tf.keras.utils.set_random_seed(1)   
tf.config.experimental.enable_op_determinism()


class AttentionLayer(tf.keras.layers.Layer):
    #https://www.geeksforgeeks.org/nlp/adding-attention-layer-to-a-bi-lstm/
    def __init__(self, **kwargs):
        super(AttentionLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        # Trainable weights for attention mechanism
        init=tf.keras.initializers.GlorotUniform(seed=0)(shape=(input_shape[-1], input_shape[-1]))

        self.W = self.add_weight(name="att_weight", shape=(input_shape[-1], input_shape[-1]),
                                 initializer=init, trainable=True)
        self.b = self.add_weight(name="att_bias", shape=(input_shape[-1],),
                                 initializer="zeros", trainable=True)
        
        init=tf.keras.initializers.GlorotUniform(seed=0)(shape=(input_shape[-1],))
        
        self.u = self.add_weight(name="att_u", shape=(input_shape[-1],),
                                 initializer=init, trainable=True)

        super(AttentionLayer, self).build(input_shape)

    def call(self, inputs):
        # Score computation
        v = tf.tanh(tf.tensordot(inputs, self.W, axes=1) + self.b)
        vu = tf.tensordot(v, self.u, axes=1)
        alphas = tf.nn.softmax(vu)

        # Weighted sum of input
        output = tf.reduce_sum(inputs * tf.expand_dims(alphas, -1), axis=1)
        return output, alphas


class Architecture:

   def __init__(self, shape):
        self.ml_model = None
        self.shape = shape
       
   def  model_recovery(self):
        # Définition du modèle
        ncols = self.shape
        inputs = Input(shape=(ncols-4,1))
        # First - layer - LSTM
        first_layer = LSTM(50, activation='relu', return_sequences=True)(inputs)
        # Second layer - Attention
        attention_out, attention_weights = AttentionLayer()(first_layer)
        outputs = Dense(1, activation='relu')(attention_out)
        self.ml_model = Model(inputs, outputs)
        self.ml_model.compile(optimizer='adam', loss='mean_squared_error')       
        


class Call_Put_processing:
    def __init__(self, address, nb_obs):
        self.data=None
        self.address = address
        self.nb_obs = nb_obs
        
    def append_multiple_data(self, address):
        """
        
        This method is used to concatenate vertically many frames with the
        same number of columns
        
        Args:
            address: the address that contains all of the data files
            
        Returns:
            None
        """
    
    def replace_missing(self):
        columns = [col for col in self.data.columns if self.data[col].dtypes == 'float64']
        for col in columns:
            self.data[col] = self.data[col].fillna(self.data[col].mean())

    def load_and_format(self):
        all_files = [name for name in os.listdir(self.address) if "options" in name]
        print(all_files)
        all_data = pd.DataFrame()
        for file in all_files:
            frame = pd.read_csv(self.address+"/"+file)
            print(frame.head())
            all_data = pd.concat([all_data,frame])
        
        
        all_data_numeric = all_data[[col for col in all_data.columns if all_data[col].dtypes == 'float64' or col in ["type", "expiration"]]]
        
        self.data = all_data_numeric
         
        
        
    def save(self, address, file_name):
        """
        
        This method allows to split the values for calls and puts, and
        save a dataframe in csv format with the separators being ;
        
        Args:
            address: the storage address
            filename: the name of the file
            
        Returns:
            None
        
        """
        call = self.data[self.data["type"] == "call"].iloc[:self.nb_obs,:]
        put = self.data[self.data["type"] == "put"].iloc[:self.nb_obs,:]
        call = call[[col for col in call.columns if col != "type"]]
        put = put[[col for col in put.columns if col != "type"]]
        call.to_csv(address+"/"+"call_"+file_name+".csv",sep=",", index=False)
        put.to_csv(address+"/"+"put_"+file_name+".csv",sep=",", index=False)