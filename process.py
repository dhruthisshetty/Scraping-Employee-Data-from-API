import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def process_employee_data(data):
    if not data:
        logging.error("No valid data to process.")
        return None
    
    logging.info("Processing employee data...")

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Debug: Print available columns
    logging.info(f"Available Columns: {df.columns.tolist()}")

    # Ensure required columns exist
    required_columns = ["id", "first_name", "last_name", "email", "job_title", "phone", "years_of_experience"]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        logging.error(f"Missing required columns: {missing_columns}")
        return None
    
    # Rename columns to match schema
    df.rename(columns={
        "id": "employee_id",
        "first_name": "First Name",
        "last_name": "Last Name",
        "email": "Email",
        "job_title": "Job Title",
        "phone": "Phone"
    }, inplace=True)

    # Create "Full Name" column
    df["Full Name"] = df["First Name"] + " " + df["Last Name"]

    # Normalize phone numbers
    df["Phone"] = df["Phone"].apply(lambda x: "Invalid Number" if isinstance(x, str) and "x" in x else 
                                      str(x) if isinstance(x, (int, float)) else x)


    # Create "designation" column based on years_of_experience
    df["designation"] = df["years_of_experience"].apply(lambda x: "System Engineer" if x < 3 else 
                                                         "Data Engineer" if 3 <= x <= 5 else 
                                                         "Senior Data Engineer" if 5 < x <= 10 else 
                                                         "Lead")

    # Ensure correct data types
    df["Full Name"] = df["Full Name"].astype(str)
    df["Email"] = df["Email"].astype(str)
    df["Job Title"] = df["Job Title"].astype(str)
    df["years_of_experience"] = df["years_of_experience"].astype(int)
    df["salary"] = df["salary"].astype(int) if "salary" in df.columns else pd.NA  # Ensure salary is handled
    df["gender"] = df["gender"].astype(str) if "gender" in df.columns else pd.NA
    df["age"] = df["age"].astype(int) if "age" in df.columns else pd.NA
    df["department"] = df["department"].astype(str) if "department" in df.columns else pd.NA

    logging.info("Data processing complete!")
    return df
