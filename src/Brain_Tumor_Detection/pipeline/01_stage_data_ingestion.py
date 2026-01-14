import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.Brain_Tumor_Detection.logger import logging
from src.Brain_Tumor_Detection.config.configuration import ConfigurationManager
from src.Brain_Tumor_Detection.components.data_ingestion import dataingestion
STAGE_NAME = "Data Ingestion" 

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        # Step 1: Load the configuration
        config = ConfigurationManager()
        
        # Step 2: Get data ingestion specific configuration
        data_ingestion_config = config.get_data_ingestion_config()

        # Step 3: Use the configuration to extract the dataset
        data_ingestion = dataingestion(config=data_ingestion_config)
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logging.info(f"\n\n ----------{STAGE_NAME} started ------------------- \n\n")
        
        # Instantiate and run the data ingestion training pipeline
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        logging.info("Data ingestion pipeline execution initiated")
        
        data_ingestion_pipeline.main()
        
        logging.info("Data ingestion pipeline execution completed successfully")
        logging.info(f"\n\n ----------{STAGE_NAME} completed ------------------- \n\n")

    except Exception as e:
        # Log any error to the log file or console
        logging.exception(e)
        raise e
