import numpy as np
import pandas as pd

predictions = np.load("./output/prediction_call_put.npy")
real_test_data = np.load("./output/test_data.npy")

comparisons = pd.DataFrame()
comparisons["predictions"] = predictions.reshape(-1)
comparisons["real_test"] = real_test_data.reshape(-1)

comparisons.plot()

