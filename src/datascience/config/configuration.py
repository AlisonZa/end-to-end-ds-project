from src.datascience.constants import CONFIG_FILEPATH, PARAMS_FILEPATH, SCHEMA_FILEPATH
from src.datascience.utils.commons import read_yaml, create_directories
from src.datascience.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig

class ConfigurationManager():
    def __init__(self, # recebe os parâmetros que seram usados para instanciar as propriedades p/leitura
                 config_filepath = CONFIG_FILEPATH,
                 params_filepath = PARAMS_FILEPATH,
                 schema_filepath = SCHEMA_FILEPATH,):
        
        # instância as propriedades com base nas leituras dos parâmetros passados acima
        self.config = read_yaml(config_filepath) # lê as configurações
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir)
        
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        
        config = self.config.data_validation # change the "section" of the config file
        schema = self.schema.FEATURE_COLUMNS
        
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            STATUS_FILE = config.STATUS_FILE,
            schema = schema)
        
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        
        config = self.config.data_transformation # change the "section" of the config file
        
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            )
        
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        
        config = self.config.model_trainer # change the "section" of the config file
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMNS


        create_directories([config.root_dir]) # cria o /artifacts/model_trainer

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            X_train_data_path= config.X_train_data_path,
            X_test_data_path= config.X_test_data_path,
            y_train_data_path= config.y_train_data_path,
            y_test_data_path= config.y_test_data_path,
            model_name = config.model_name,

            alpha= params.alpha,
            l1_ratio= params.l1_ratio,
            
            target_column= schema.name,

            )
        
        return model_trainer_config