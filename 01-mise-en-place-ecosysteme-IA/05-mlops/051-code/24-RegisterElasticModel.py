import pickle
import mlflow
import mlflow.sklearn

# load the model into memory
filename = 'elastic-net-regression.pkl'
loaded_model = pickle.load(open(filename, "rb"))

mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
exp = mlflow.set_experiment(experiment_name="experiment_register_outside")

mlflow.start_run()

mlflow.sklearn.log_model(
    loaded_model,
    'model',
    serialization_format='cloudpickle',
    registered_model_name="elastic-net-regression-outside-mlflow"
)
mlflow.end_run()
