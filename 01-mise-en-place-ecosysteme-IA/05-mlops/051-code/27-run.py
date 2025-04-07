import mlflow

parameters={
    "alpha":0.3,
    "l1_ratio":0.3
}

experiment_name = "Project exp 1"
entry_point = "ElasticNet"

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    parameters=parameters,
    experiment_name=experiment_name
)