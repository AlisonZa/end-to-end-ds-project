from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig():
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig():
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str

    schema: dict 

@dataclass
class DataTransformationConfig():
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainerConfig():
  # config.yaml
  root_dir: Path
  X_train_data_path: Path
  X_test_data_path: Path
  y_train_data_path: Path
  y_test_data_path: Path
  model_name: str

  # params.yaml
  alpha: float
  l1_ratio: float
  
  # schema.yaml
  target_column: str 

@dataclass
class ModelEvaluationConfig():
  # config.yaml
  root_dir: Path
  X_test_data_path: Path
  y_test_data_path: Path
  model_path: Path
  metric_file_name: Path

  #params.yaml
  all_params: dict