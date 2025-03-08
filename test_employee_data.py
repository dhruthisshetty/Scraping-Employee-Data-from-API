import unittest
from fetch import fetch_employee_data
from process import process_employee_data

class TestEmployeeData(unittest.TestCase):

    def setUp(self):
        """Set up shared test data before each test"""
        self.data = fetch_employee_data()

    def test_fetch_employee_data(self):
        """Test Case 1: Verify JSON File Download"""
        self.assertIsInstance(self.data, list, "Expected data to be a list.")
        self.assertGreater(len(self.data), 0, "Expected data list to be non-empty.")

    def test_json_file_extraction(self):
        """Test Case 2: Verify JSON File Extraction"""
        if isinstance(self.data, dict):
            self.assertIn("employees", self.data, "Missing 'employees' key in response.")
        elif isinstance(self.data, list):
            self.assertTrue(self.data, "Expected non-empty list of employees.")

    def test_validate_file_type_and_format(self):
        """Test Case 3: Validate File Type and Format"""
        self.assertIsInstance(self.data, (list, dict), "Data should be a list or dictionary.")

    def test_validate_data_structure(self):
        """Test Case 4: Validate Data Structure"""
        processed_df = process_employee_data(self.data)
        self.assertIsNotNone(processed_df, "Processed DataFrame should not be None.")
        required_columns = [
            "employee_id", "First Name", "Last Name", "Email", "Job Title", "Phone", "Full Name", "designation"
        ]
        for col in required_columns:
            self.assertIn(col, processed_df.columns, f"Missing expected column: {col}.")

    def test_handle_missing_or_invalid_data(self):
        """Test Case 5: Handle Missing or Invalid Data"""
        invalid_data = [{"id": 1, "first_name": "John", "last_name": "Doe"}]  # Missing essential fields
        processed_df = process_employee_data(invalid_data)
        
        # Ensure that the function returns either None or an empty DataFrame
        self.assertTrue(processed_df is None or processed_df.empty, "Processed DataFrame should be None or empty for invalid data.")

if __name__ == "__main__":
    unittest.main()
