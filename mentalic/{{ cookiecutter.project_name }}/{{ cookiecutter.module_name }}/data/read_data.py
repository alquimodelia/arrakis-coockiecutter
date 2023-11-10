import os

PROCESSED_FILE_PATH = os.getenv("PROCESSED_FILE_PATH")

# Read data from the file

# Define the following from the dataset:
# Training Data
train_dataset_X=None
train_dataset_Y=None
weights=None
training_data = train_dataset_X, train_dataset_Y, weights

# Testing Data
test_dataset_X=None
test_dataset_X=None
test_dataset_Y = test_dataset_X, test_dataset_Y

# Validation/Benchmark
validation_dataset_X, validation_dataset_Y = None, None
validation_benchmark = None # to compare to validation_dataset_Y /predictions