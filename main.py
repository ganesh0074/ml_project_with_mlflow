from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import dataingestiontrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:

    logger.info(f">>>> stage {STAGE_NAME} started   <<<<")  
    data_ingestion = dataingestiontrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage  {STAGE_NAME} completed <<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise e 