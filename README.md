
#  Strike prediction for call options
The purpose of this project is to illustrate how predict the strike of a call option via a LSTM model with attention layers.

It is worth mentioning that this Machine Learning project focuses on building and evaluating a regression model for call price prediction. Specifically, it demonstrates the full pipeline from data processing to the dockerization of the code as well as its evaluation.

---

## Overview

This project deals with a * regression problem * via a simple neural network architecture with LSTM (Long Short Term Memory) with LSTM layers as well as an attention layer. The prokect could be split into four main phases: data cleaning, dockerization of the code, model training and performance evaluation.

> 💡 Ultimate objective: predict the price of a call option as precisely as possible. 

---

## Project Structure

```                  
├── Call_prediction/                # Source code with the python codes, dockerfiles and the requirement files
    ├── 1_dataformatting.py         # Data preprocessing
    ├── 2_model_train_save.py       # Training and save of the model
    ├── Dockerfile_python           # Dockerfile for the Python application
    ├── data_storage_code_launch.sh # Bash file to pre-process the data, store the data in a relational data base, train the model, and save            the outputs.
    ├── docker-compose.yml          # Dockerfile allowing to build the Python app
    ├── env_db.env                  # File containing the user name for the mysql database
    ├── launch-docker.sh            # File to launch in order to build the docker containers for the python app as well as the mysql database
    ├── library.py                  # Library containing various classes and methods
    ├── query_file.sql
    ├── requirements_python.txt     # Text file containing the libraries that have to be installed
    ├── call_put_data/              # Raw and processed datasets
    ├── output/                     # Archives containing the model as well as the predictions    
```

---

## Dataset

* Source: https://optiondata.org/#fieldId
* Features
  - expiration
  - strike
  - bid
  - bid_size
  - ask
  - ask_size
  - delta
  - gamma
  - theta
  - vega
  - implied_volatility

* Target: prediction of the 'right value for the strike' / Regression problem (prediction of real numbers)

---

## Data cleaning
For the data cleaning, we proceed as follows:

    * Removal of all of the data values that are not numeric ;
    
    * The missing observations undergo an imputation process via the mean strategy. Specifically, they are replaced by the average of the             observed values.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/traoreabraham931-creator/Call_prediction.git
```
---

## Usage

Launch a .sh file to build the containers (python and sql)

```bash
./launch-docker.sh 
```

Generate the call dataset from the raw data, store the data in a mysql database, train the model, make the prediction, and export some archives
from the docker containers.

```bash
./data_storage_code_launch.sh
```

---

## Attention-based architecture

The model used is a LSTM-based architecture with some attention layers. Delving into the specifics, the layers are defined as follows:
     - A LSTM-cell with 50 units;
     - A dropout layer ;
     - An attention layer;
     - An output layer with a single unit (prediction of a single value)

---


## 📈 Results
 -----------------------------
| Metrics           | Score   |
| ----------------- | ------- |
| MSE - test        |  19.010 |
 ----------------------------
Roughly speaking, the test error amounts to 19.


