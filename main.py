from src.Brain_Tumor_Detection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Brain_Tumor_Detection.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.Brain_Tumor_Detection.pipeline.stage_03_training import ModelTrainingPipeline
from src.Brain_Tumor_Detection.pipeline.stage_04_model_evaluation import EvaluationTrainingPipeline
from src.Brain_Tumor_Detection.logger import logging


# ----------------- STAGE 1: Data Ingestion -----------------
STAGE_NAME = "Data Ingestion"
try:
        logging.info(f"\n\n ---------- {STAGE_NAME} started ------------------- \n\n")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        logging.info("Data ingestion pipeline initialized")
        data_ingestion_pipeline.main()
        logging.info("Data ingestion process completed")
        logging.info(f"\n\n ---------- {STAGE_NAME} completed ------------------- \n\n")

except Exception as e:
        logging.exception(e)
        raise e


# ----------------- STAGE 2: Prepare Base Model -----------------
STAGE_NAME = "Prepare base model"
try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
        prepare_base_model_pipeline.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logging.exception(e)
        raise e


# ----------------- STAGE 3: Training -----------------
STAGE_NAME = "Training"
try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logging.exception(e)
        raise e


# ----------------- STAGE 4: Evaluation -----------------
STAGE_NAME="Evaluation"
try:
        logging.info("*******************")
        logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        model_evaluation_pipeline = EvaluationTrainingPipeline()
        model_evaluation_pipeline.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")

except Exception as e:
        logging.exception(e)
        raise e



