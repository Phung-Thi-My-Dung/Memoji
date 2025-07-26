
class BaseFile:
    
    def __init__(self, file_path, file_name, file_type):
        """
        Initialize a BaseFile object with the required fields.
        
        Args:
            file_path (str): The path to the file.
            file_name (str): The name of the file.
            file_type (str): The type of the file (e.g., 'txt', 'csv', 'xlsx').
        """
        self.file_path = file_path
        self.file_name = file_name
        self.file_type = file_type

    def read_file(self):
        return
    
    def write_file(self, data):
        return 
    
    def delete_file(self):
        return  
    
