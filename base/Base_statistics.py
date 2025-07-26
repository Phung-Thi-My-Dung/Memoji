
class BaseStatistic:
    def __init__(self):

        """
            Initializes the BaseStatistic instance with data.
        """
        self.data = None
        self.method = {}

    def set_data(self, data):
        """
        Set the data for the statistics.
        
        Args:
            data (any): The data to be set.
        """
        self.data = data    
    
    def get_data(self):
        """
        Get the data for the statistics.
        
        Returns:
            any: The data set for the statistics.
        """
        return self.data    
    
    def add_method(self, name, method):
        """         
        Add a method to the statistics. 
        Args:
            name (str): The name of the method.
            method (callable): The method to be added.
        """
        self.method[name] = method  

    def get_method(self, name):
        """ 
        Get a method by its name.           
        Args:
            name (str): The name of the method. 

        Returns:
            callable: The method associated with the name.
        """
        return self.method.get(name, None)
        

