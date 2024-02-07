# from mlProject.config.mongo_db_connection import MongoDBClient
# from mlProject.logger import logging
# from mlProject.exceptions import CustomException
# import sys

# instance = MongoDBClient()


from mlProject.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from mlProject.entity.config_entity import DataIngestionConfig,DataValidationConfig
from mlProject.components.data_ingestion import DataIngestion
from mlProject.components.data_validation import DataValidation

di_ins=DataIngestion(DataIngestionConfig)
di_art=di_ins.initiate_data_ingestion()

dv_ins=DataValidation(data_ingestion_artifact=di_art,data_validation_config=DataValidationConfig)
dv_art=dv_ins.initiate_data_validation()


# from mlProject.entity.config_entity import DataIngestionConfig

# data_ingestion_config:DataIngestionConfig=DataIngestionConfig()

# print(data_ingestion_config)