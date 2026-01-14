import os
import zipfile
from src.Brain_Tumor_Detection.utils.common import get_size
from src.Brain_Tumor_Detection.logger import logging
from src.Brain_Tumor_Detection.entity.config_entity import (DataIngestionConfig)


class dataingestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def extract_zip_file(self):
        """
        Unzipping organizes the data into the 'artifacts/data_ingestion' folder 
        so the next stages can easily access the images.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            logging.info(f"Extracting to: {unzip_path}")
            zip_ref.extractall(unzip_path)
