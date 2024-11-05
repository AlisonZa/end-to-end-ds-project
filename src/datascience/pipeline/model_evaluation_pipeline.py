from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.utils import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self, stage_name):
        self.stage_name = STAGE_NAME

    def initiate_model_evaluation(self):
        try:
            logger.info(f"{">"*10} Stage: {self.stage_name} started {"<"*10}")

            # Get the variables from needed for the process
            model_evaluation_config = ConfigurationManager().get_model_evaluation_config()
            
            # Instantiate the object for performing the Model Training:
            model_evaluation_object = ModelEvaluation(model_evaluation_config)

            X_test, y_test = model_evaluation_object.load_test_data()
            model = model_evaluation_object.load_model()
            predictions = model_evaluation_object.predict(model, X_test)
            model_evaluation_object.log_to_mlflow(model, y_test, predictions)

            logger.info(f"{">"*10} Stage: {self.stage_name} completed {"<"*10}")

        except Exception as e:
            logger.error(f"Error during model_evaluation. Error {e}")
            raise e