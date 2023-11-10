from {{ cookiecutter.module_name }}.data.read_data import training_data
# If more data need to be used, import from data.read
fit_args = {}
compile_args = {}

# TODO: DEVS: apply logic for genetor possibity, and for class weights 
train_dataset_X, train_dataset_Y, weights = training_data
if weights:
    fit_args["sample_weights"]=weights


# Define yout training method(s), with the following arguments:

# It is used in the default train command, or you can pass it as training_fn to the Experiment class object
# Any methods you want to create for training should have the same args, and then you pass them as training_fn to the respective Case/Experiment.
def train_model(model_to_train=None, X=train_dataset_X,Y=train_dataset_Y,
fit_args=fit_args,compile_args=compile_args,model_name="experiment_model"
):
    raise NotImplementedError