# Use this model to define the expeirments you want to run
from muaddib.experiment import Experiment

EXPERIMENT_FOLDER = os.getenv("EXPERIMENT_FOLDER", ".")
DATA_FOLDER = os.getenv("DATA_FOLDER", "data")


experiment1 = Experiment()

experiment2 = Experiment(
                previous_experiment=experiment_1,

)


# Get a dictionary of all objects in the module
module_objects = globals()

# Filter the dictionary to only include instances of the Experiment class
experiments_dict = {obj.name:obj for name, obj in module_objects.items() if isinstance(obj, Experiment)}
experiments_list = [obj for name, obj in module_objects.items() if isinstance(obj, Experiment)]
