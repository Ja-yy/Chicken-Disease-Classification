import os
import urllib.request as request
import zipfile
from pathlib import Path

from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.get_logger import logger
from cnnClassifier.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Download data in zip format

        PARAMS:
            local_data_file: str
            source_URL: str(URL)
        RETURNS: None
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory

        PARAMS:
            zip_file_path: str
        RETURN: None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
