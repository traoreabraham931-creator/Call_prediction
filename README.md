
# 🧠 Call price prediction
The purpose of this project is to illustrate how predict the price of a call option via a LSTM model with attention layers.

It is worth mentioning that this Machine Learning project focuses on building and evaluating a regression model for call price prediction. Specifically, it demonstrates the full pipeline from data processing to the dockerization of the code as well as its evaluation.

---

## 🚀 Overview

This project deals with a * regression problem * via a simple neural network architecture with LSTM (Long Short Term Memory) with LSTM layers as well as an attention layer. The prokect could be split into four main phases: data cleaning, dockerization of the code, model training and performance evaluation.

> 💡 Ultimate objective: predict the price of a call option as precisely as possible. 

---

## ✨ Data cleaning
For the data cleaning, we proceed as follows:

    * Removal of all of the data values that are not numeric ;
    
    * The missing observations undergo an imputation process via the mean strategy. Specifically, they are replaced by the average of the observed             values.

---

## 🏗️ Project Structure

```
├── output/               # Archives containing the model as well as the predictions
├── call_put_data/        # Raw and processed datasets
├── Call_prediction/      # Source code with the python codes, dockerfiles and the requirement files
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
```

---

## 📊 Dataset

Brief description of the dataset:

* Source: [Add source here]
* Samples: XXXX
* Features: XXXX
* Target: Binary / Multi-class classification

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Train the model:

```bash
python src/train.py
```

Evaluate performance:

```bash
python src/evaluate.py
```

---

## 📈 Results

| Metric    | Score |
| --------- | ----- |
| Accuracy  | XX%   |
| Precision | XX%   |
| Recall    | XX%   |
| F1-score  | XX%   |

> 📌 Replace with your actual results.

---

## 📸 Visualizations

Add plots such as:

* Confusion matrix
* ROC curve
* Feature importance

Example:

```md
![Confusion Matrix](outputs/confusion_matrix.png)
```

---

## 🧪 Models Used

* Logistic Regression
* Decision Tree
* Random Forest
* (Optional) XGBoost / Neural Networks

---

## 🔍 Evaluation Metrics

This project uses:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

---

## 🧠 Key Learnings

* Importance of feature engineering
* Handling class imbalance
* Model selection & tuning
* Interpreting evaluation metrics

---

## 🗺️ Roadmap

* [ ] Hyperparameter tuning
* [ ] Model deployment (API)
* [ ] Add more datasets
* [ ] Improve feature engineering

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you find this project useful, consider giving it a star ⭐

---
