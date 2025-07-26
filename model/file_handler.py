from base import BaseFile
import pandas as pd

class FileHandler(BaseFile):
    def __init__(self, file_path, file_name, file_type):
        """
        Initialize a FileHandler object with the required fields.
        
        Args:
            file_path (str): The path to the file.
            file_name (str): The name of the file.
            file_type (str): The type of the file (e.g., 'txt', 'csv', 'xlsx').
        """
        super().__init__(file_path, file_name, file_type)
    
    def read_file_excel(self):
        """
        Read an Excel file and return its content.
        
        Returns:
            content (list): The content of the Excel file.
        """
        # Placeholder for actual reading logic
        file_full_path = f"{self.file_path}/{self.file_name}.{self.file_type}"
        content = pd.read_excel(file_full_path)
        return content