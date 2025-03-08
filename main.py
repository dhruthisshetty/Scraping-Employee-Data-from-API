from fetch import fetch_employee_data
from process import process_employee_data
from save import save_to_parquet

def main():
    data = fetch_employee_data()
    if data:
        processed_df = process_employee_data(data)
        if processed_df is not None:
            save_to_parquet(processed_df)

if __name__ == "__main__":

    main()
