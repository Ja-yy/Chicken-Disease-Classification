from pydantic import BaseModel
from pathlib import Path


class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


class PrepareBaseModelConfig(BaseModel):
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


class PrepareCallbacksConfig(BaseModel):
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: str
