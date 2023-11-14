import os

import numpy as np
import pandas as pd
from alquitable.generator import get_dataset

PROCESSED_FILE_PATH = os.getenv("PROCESSED_FILE_PATH")


# Read data from the file
dataset = pd.read_csv(PROCESSED_FILE_PATH, index_col=0)
time_cols = ["hour", "day", "month", "year", "day_of_year", "day_of_week", "week_of_year"]


columns_Y = os.getenv("TARGET_COLUMN")
alloc_column = os.getenv("ALLOCATION_COLUMN")
y_columns = columns_Y
datetime_col = "datetime"



X_timeseries = 168
Y_timeseries = 24
frac = 1
train_features_folga = 24
skiping_step=1
keep_y_on_x=True

get_dataset_args={
    "y_columns":columns_Y,
    "time_moving_window_size_X":X_timeseries,
    "time_moving_window_size_Y":Y_timeseries,
    "frac":frac,
    "keep_y_on_x":keep_y_on_x,
    "train_features_folga":train_features_folga,        
    "skiping_step":skiping_step,
    "time_cols":time_cols,
    "alloc_column":alloc_column,
}
dataset_to_use = dataset.copy()

train_dataset_X, train_dataset_Y, test_dataset_X, test_dataset_Y, gen = get_dataset(dataset_to_use,**get_dataset_args)

mean = np.nanmean(dataset[columns_Y].values)


# TODO: change this weight thingy
weights = None
weight = None #"delta_mean"

# if weight:
#     if "delta_mean" in  weight or "both" in weight:
#         train_dataset_Y_values = train_dataset_Y_values or train_dataset_Y
#         samples_weights = np.abs(train_dataset_Y_values - mean)
#         weights = samples_weights
#     if "freq" in  weight or "both" in weight:
#         freq_weights = get_freq_samples(train_dataset_labels)
#         weights = freq_weights
#     if "both" in weight:
#         weights = freq_weights*samples_weights

# Training Data
training_data = train_dataset_X, train_dataset_Y, weights

# Testing Data
testing_data = test_dataset_X, test_dataset_Y

validation_dataset = dataset.copy()
validation_dataset["date"] = pd.to_datetime(validation_dataset["datetime"])
years_to_use = [2019,2020,2021,2022]
year_mask = validation_dataset["date"].dt.year.isin(years_to_use)
validation_dataset[year_mask][columns_Y]

validation_dataset["hour_in_year"] = (validation_dataset["date"].dt.hour)+(24*(validation_dataset["day_of_year"]-1))
mask_before = validation_dataset["date"].dt.year == min(years_to_use)-1
max_hour = max(validation_dataset[mask_before]["hour_in_year"])

mask_last_hours = validation_dataset["hour_in_year"] > (max_hour - X_timeseries)
mask_before = mask_before & mask_last_hours

mask_after = validation_dataset["date"].dt.year == max(years_to_use)+1
mask_after_hours = validation_dataset["hour_in_year"] < Y_timeseries
mask_after = mask_after & mask_after_hours

mask_data = mask_before | year_mask | mask_after

validation_dataset = dataset[mask_data].copy()


get_dataset_args["skiping_step"] = 24
validation_dataset_X, validation_dataset_Y, _, _, gen = get_dataset(validation_dataset.copy(),**get_dataset_args)



validation_benchmark = validation_dataset[alloc_column].iloc[X_timeseries:-Y_timeseries].values.reshape(validation_dataset_Y.shape)

