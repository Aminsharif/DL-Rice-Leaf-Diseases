from riceLeafDiseases.config.configuration import ConfigurationManager
from riceLeafDiseases.exception import ExceptionHandle
from riceLeafDiseases.components.data_ingestion import DataIngestion
import os

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise ExceptionHandle(os, e)