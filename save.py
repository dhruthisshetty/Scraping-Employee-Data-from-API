import pyarrow.parquet as pq
import pyarrow as pa
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

OUTPUT_FILE = "processed_employees.parquet"

def save_to_parquet(df, file_path=OUTPUT_FILE):
    try:
        logging.info(f"Saving data to {file_path}...")
        table = pa.Table.from_pandas(df)
        pq.write_table(table, file_path)
        logging.info("Parquet file successfully saved!")
    except Exception as e:
        logging.error(f"Error saving Parquet file: {e}")