
## MongoDB Connection and Data export
DATABASE_NAME = "us_visa"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "MONGODB_URL"

## Training Pipeline Config
ARTIFACT_DIR: str = "artifact"
PIPELINE_NAME: str = "usvisa"


FILE_NAME: str = "usdata.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

## Data Ingestion constants
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
