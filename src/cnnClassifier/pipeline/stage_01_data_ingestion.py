from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.get_logger import logger

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        data_ingestion_config = DataIngestionConfig.get_config("data_ingestion")
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
