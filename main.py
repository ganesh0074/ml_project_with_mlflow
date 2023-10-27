from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import dataingestiontrainingPipeline
from mlproject.pipeline.stage_02_data_validation import dataValidationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:

    logger.info(f">>>> stage {STAGE_NAME} started   <<<<")  
    data_ingestion = dataingestiontrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage  {STAGE_NAME} completed <<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Validation Stage"

try:

    logger.info(f">>>> stage {STAGE_NAME} started   <<<<")  
    data_validation = dataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise e 