from mlproject.components.model_training import ModelTrainer, ModelTrainerConfig
from mlproject.config.configuration import ConfigurationManager
from mlproject import logger


STAGE_NAME = "Model Training Stage"

class modelTrainingPipeline:

    def __init__(self) -> None:
        pass

    def main(self):         
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
       

if __name__=="__main__":
    try:

        logger.info(f">>>> stage {STAGE_NAME} started   <<<<")  
        obj = modelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<") 
    except Exception as e:
        logger.exception(e)
        raise e 