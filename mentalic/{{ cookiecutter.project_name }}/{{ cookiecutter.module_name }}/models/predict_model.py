from {{ cookiecutter.module_name }}.data.read_data import validation_dataset_X, validation_dataset_Y, validation_benchmark


# Create validation function. it can be as simples as a RMSE imported from somewhere.
# The goal where is to set the function(s) passed on to the experiment for validation. This validation sets the
#   scores used to pick the best cases on each iteration.abs

def save_scores():
    raise NotImplementedError

def validate_model():
    raise NotImplementedError