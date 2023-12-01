from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel, Field
from yaml import safe_load

from cnnClassifier.constant import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassifier.utils.common import create_directories

__all__ = {
    "DataIngestionConfig",
    "PrepareBaseModelConfig",
    "PrepareCallbacksConfig",
    "TrainingConfig",
    "EvaluationConfig",
}


class BaseConfig(BaseModel):
    @classmethod
    def load_yaml(cls, file_path: Path) -> Dict[str, Any]:
        with file_path.open("r") as f:
            config = safe_load(f)
            if not isinstance(config, dict):
                raise TypeError(f"Config file has no top-level mapping: {file_path}")
            return config

    @classmethod
    def get_config(cls, sub_config_name: str, is_parm: bool = False) -> "BaseConfig":
        main_config = cls.load_yaml(CONFIG_FILE_PATH)
        return_config = main_config.get(sub_config_name, {})
        try:
            create_directories([return_config.get("root_dir")])
        except Exception:
            pass
        if is_parm:
            params_config = cls.load_yaml(PARAMS_FILE_PATH)
            print(params_config)
            return_config.update(params_config)

        return cls(**return_config)


class DataIngestionConfig(BaseConfig):
    root_dir: Path = Field(description="Data ingestion root folder")
    source_URL: str = Field(description="URL to download data")
    local_data_file: Path = Field(description="Savas file name")
    unzip_dir: Path = Field(description="Path to unzip data")


class PrepareBaseModelConfig(BaseConfig):
    root_dir: Path = Field(description="Base model root folder")
    base_model_path: Path = Field(description="Path to save base model")
    updated_base_model_path: Path = Field(description="Updated model path")
    params_image_size: list = Field(description="Image size", alias="IMAGE_SIZE")
    params_learning_rate: float = Field(
        description="learning rate", alias="LEARNING_RATE"
    )
    params_include_top: bool = Field(
        description="Boolean value to include top", alias="INCLUDE_TOP"
    )
    params_weights: str = Field(description="Params weights", alias="WEIGHTS")
    params_classes: int = Field(description="Number of classes", alias="CLASSES")

    class config:
        populate_by_name = True


class PrepareCallbacksConfig(BaseConfig):
    root_dir: Path = Field(description="Callbacks root folder")
    tensorboard_root_log_dir: Path = Field(description="Path for log dir")
    checkpoint_model_filepath: str = Field(description="Path to save checkpoint models")


class TrainingConfig(BaseConfig):
    root_dir: Path = Field(description="Training Root folder")
    trained_model_path: Path = Field(description="Path to trained model")
    updated_base_model_path: Path = Field(description="Path to updated base model")
    training_data: Path = Field(description="Path to training data")
    params_epochs: int = Field(description="Number of epochs", alias="EPOCHS")
    params_batch_size: int = Field(description="Batch size", alias="BATCH_SIZE")
    params_is_augmentation: bool = Field(
        description="Boolean value fot augmentation", alias="AUGMENTATION"
    )
    params_image_size: list = Field(description="Image size", alias="IMAGE_SIZE")

    class config:
        populate_by_name = True


class EvaluationConfig(BaseConfig):
    path_of_model: Path = Field(description="Path to sabed model")
    training_data: Path = Field(description="Path for training data")
    params_image_size: list = Field(description="Image size",alias="IMAGE_SIZE")
    params_batch_size: int = Field(description="Batch size",alias="BATCH_SIZE")
