mlflow doctor

mlflow doctor --mask-envs

mlflow artifacts list --run-id b18697e8c62945e6adbdef5cb1af6c21

mlflow artifacts download --run-id b18697e8c62945e6adbdef5cb1af6c21 --dst-path cli_artifact

mlflow artifacts log-artifacts --local-dir cli_artifact --run-id b18697e8c62945e6adbdef5cb1af6c21 --artifact-path cli_artifact

mlflow db upgrade sqlite:///mlflow.db

mlflow experiments create --experiment-name cli_experiment

mlflow experiments rename --experiment-id 26 --new-name test1

mlflow experiments delete --experiment-id 26

mlflow experiments restore --experiment-id 26

mlflow experiments search --view "all" 

mlflow experiments csv --experiment-id 6 --filename test.csv

mlflow runs list --experiment-id 6 --view "all"

mlflow runs describe --run-id 97e72d1a3a074e97a4a59b95625cca64

mlflow runs delete --run-id 

mlflow runs restore --run-id 






