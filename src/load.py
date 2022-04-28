
import pandas as pd
from helper.conf import *
from functions.helper import load_data


# LOAD DATA
train_values = load_data(TRAIN_VALUES_PATH)
train_labels = load_data(TRAIN_LABELS_PATH)
test_values = load_data(TEST_VALUES_PATH)

## combine values of train and test set 
X_all_raw = pd.concat([train_values, test_values], axis=0, sort=False)

## make report on values
# from pandas_profiling import ProfileReport
# prof = ProfileReport(X_all_raw)
# prof.to_file(output_file='./reports/data_report.html')

print("Data is loaded")