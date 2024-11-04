import pandas as pd
from src.datascience.utils import logger
from src.datascience.config.configuration import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        # config should be an instance of DataValidationConfig
        self.config = config

    def validate_column_names(self) -> bool:
        """Validate if all columns match the schema names."""
        try:
            validation_status_names = True
            log_messages = []

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            schema_columns = set(self.config.schema.keys())

            for col in all_cols:
                if col not in schema_columns:
                    validation_status_names = False
                    log_messages.append(f"Name Validation Status for {col}: False")
                else:
                    log_messages.append(f"Name Validation Status for {col}: True")

            # Write all messages to the status file at once
            with open(self.config.STATUS_FILE, "a") as f:
                f.write("\n".join(log_messages) + "\n")

            return validation_status_names

        except Exception as e:
            logger.exception(f"Error during column name validation: {e}")
            raise e

    def validate_column_types(self) -> bool:
        """Validate if all column types match the schema types."""
        try:
            validation_status_types = True
            log_messages = []

            data = pd.read_csv(self.config.unzip_data_dir)
            column_types = data.dtypes.to_dict()
            schema_types = self.config.schema

            for col, dtype in column_types.items():
                if col not in schema_types or schema_types[col] != str(dtype):
                    validation_status_types = False
                    log_messages.append(f"Dtype Validation Status for {col}: False")
                else:
                    log_messages.append(f"Dtype Validation Status for {col}: True")

            # Write all messages to the status file at once
            with open(self.config.STATUS_FILE, "a") as f:
                f.write("\n".join(log_messages) + "\n")

            return validation_status_types

        except Exception as e:
            logger.exception(f"Error during column type validation: {e}")
            raise e
