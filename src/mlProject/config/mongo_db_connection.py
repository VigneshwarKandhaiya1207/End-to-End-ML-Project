from mlProject.logger import logging
from mlProject.exceptions import CustomException
from mlProject.constants import DATABASE_NAME,MONGODB_URL_KEY
import pymongo
import certifi
import os
import sys

ca=certifi.where()

class MongoDBClient():
    client = None
    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URL_KEY
                logging.info(mongo_db_url)
                if mongo_db_url is None:
                    raise CustomException(f"Environment key {MONGODB_URL_KEY} is not set.",sys)
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=certifi.where())
                self.client=MongoDBClient.client
                self.database=self.client[database_name]
                self.database_name=database_name
                logging.info("MongoDB connection is successful")
        except Exception as e:
            raise CustomException(e,sys)

