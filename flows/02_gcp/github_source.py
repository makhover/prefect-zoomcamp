from prefect.deployments import Deployment
from etl_web_to_gcs import etl_ny_taxi_files_to_gcs
from prefect.filesystems import GitHub 

storage = GitHub.load("github-prefect-repo")

deployment = Deployment.build_from_flow(
     flow=etl_ny_taxi_files_to_gcs,
     name="github-exercise",
     storage=storage,
     entrypoint="flows/02_gcp/etl_web_to_gcs.py:etl_ny_taxi_files_to_gcs")

if __name__ == "__main__":
    deployment.apply()