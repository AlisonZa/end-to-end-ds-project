from src.datascience.constants import CONFIG_FILEPATH, PARAMS_FILEPATH, SCHEMA_FILEPATH
from src.datascience.utils.commons import read_yaml, create_directories
from src.datascience.entity.config_entity import DataIngestionConfig

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