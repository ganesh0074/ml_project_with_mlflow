from mlproject.components.data_transformation import DataTransformation
from mlproject.config.configuration import ConfigurationManager
from mlproject import logger


STAGE_NAME = "Data Transformation Stage"

class dataTransformationPipeline:

    def __init__(self) -> None:
        pass

    def main(self):
        config= ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation= DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()


if __name__=="__main__":
    try:

        logger.info(f">>>> stage {STAGE_NAME} started   <<<<")  
        obj = dataTransformationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<") 
    except Exception as e:
        logger.exception(e)
        raise e 