import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.Brain_Tumor_Detection.config.configuration import ConfigurationManager
from src.Brain_Tumor_Detection.components.prepare_base_model import PrepareBaseModel
from src.Brain_Tumor_Detection.logger import logging


STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Step 1: Manage and fetch the configuration
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        
        # Step 2: Prepare the base model using the component
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        
        # Step 3: Fetch the original pre-trained model (e.g., VGG16)
        prepare_base_model.get_base_model()
        
        # Step 4: Add custom layers and compile the model
        prepare_base_model.update_base_model()


    
if __name__ == '__main__':
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Instantiate and run the pipeline
        pipeline_base_model = PrepareBaseModelTrainingPipeline()
        pipeline_base_model.main()
        
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log error details if the pipeline fails
        logging.exception(e)
        raise e
