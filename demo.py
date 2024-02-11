# from mlProject.config.mongo_db_connection import MongoDBClient
# from mlProject.logger import logging
# from mlProject.exceptions import CustomException
# import sys

# # instance = MongoDBClient()


# from mlProject.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
# from mlProject.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig
# from mlProject.components.data_ingestion import DataIngestion
# from mlProject.components.data_validation import DataValidation
# from mlProject.components.data_transformation import DataTransformation
# from mlProject.components.model_trainer import ModelTrainer
# from mlProject.components.model_evaluation import ModelEvaluation
# from mlProject.components.model_pusher import ModelPusher

# di_ins=DataIngestion(DataIngestionConfig)
# di_art=di_ins.initiate_data_ingestion()

# dv_ins=DataValidation(data_ingestion_artifact=di_art,data_validation_config=DataValidationConfig)
# dv_art=dv_ins.initiate_data_validation()

# dt_ins=DataTransformation(data_ingestion_artifact=di_art,data_transformation_config=DataTransformationConfig,data_validation_artifact=dv_art)
# dt_art=dt_ins.initiate_data_transformation()

# mt_ins = ModelTrainer(data_transformation_artifact=dt_art, model_trainer_config=ModelTrainerConfig)

# mt_art = mt_ins.initiate_model_trainer()

# me_ins=ModelEvaluation(model_eval_config=ModelEvaluationConfig,data_ingestion_artifact=di_art,model_trainer_artifact=mt_art)
# me_art=me_ins.initiate_model_evaluation()

# mp_ins=ModelPusher(model_evaluation_artifact=me_art, model_pusher_config=ModelPusherConfig)
# mp_art=mp_ins.initiate_model_pusher()


# # from mlProject.entity.config_entity import DataIngestionConfig

# # data_ingestion_config:DataIngestionConfig=DataIngestionConfig()

# # print(data_ingestion_config)

# # from mlProject.config.aws_connection import S3Client

# # s3_cl=S3Client()

from mlProject.pipeline.training_pipeline import TrainPipeline

training=TrainPipeline()

training.run_pipeline()