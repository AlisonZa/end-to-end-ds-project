from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.utils import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self, stage_name):
        self.stage_name = STAGE_NAME

    def initiate_model_training(self):
        try:
            logger.info(f"{">"*10} Stage: {self.stage_name} started {"<"*10}")

            # Get the variables from needed for the process
            model_trainer_config = ConfigurationManager().get_model_trainer_config()
            
            # Instantiate the object for performing the Model Training:
            model_trainer_object = ModelTrainer(model_trainer_config)
            X_train, y_train = model_trainer_object.load_training_data()
            trained_model = model_trainer_object.train_model(X_train, y_train)
            model_trainer_object.save_model(trained_model)

            logger.info(f"{">"*10} Stage: {self.stage_name} completed {"<"*10}")

        except Exception as e:
            logger.error(f"Error during model_training. Error {e}")
            raise e