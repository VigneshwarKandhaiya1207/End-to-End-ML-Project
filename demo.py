# from mlProject.config.mongo_db_connection import MongoDBClient
# from mlProject.logger import logging
# from mlProject.exceptions import CustomException
# import sys

# instance = MongoDBClient()


from mlProject.entity.artifact_entity import DataIngestionArtifact
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.components.data_ingestion import DataIngestion

di_ins=DataIngestion(DataIngestionConfig)
di_art=di_ins.initiate_data_ingestion()