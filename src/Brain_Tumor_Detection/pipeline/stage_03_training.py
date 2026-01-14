import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.Brain_Tumor_Detection.config.configuration import ConfigurationManager
from src.Brain_Tumor_Detection.components.model_training import Training
from src.Brain_Tumor_Detection.logger import logging


STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Step 1: Manage and fetch training configuration (paths, hyperparameters)
        config = ConfigurationManager()
        training_config = config.get_training_config()
        
        # Step 2: Initialize the Training component with the fetched config
        training = Training(config=training_config)
        
        # Step 3: Run the training workflow:
        training.get_base_model()         # 1. Load the customized VGG16 model from artifacts
        training.train_valid_generator()  # 2. Prepare the images (normalization & augmentation)
        training.train()                  # 3. Start training and save the final result

if __name__ == '__main__':
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Instantiate and run the pipeline stage
        modeltraining = ModelTrainingPipeline()
        modeltraining.main()
        
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any errors encountered during the training pipeline
        logging.exception(e)
        raise e
