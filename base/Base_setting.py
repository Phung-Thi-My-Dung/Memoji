
class BaseSetting:
    """
    Base class for settings.
    This class can be extended to create specific settings classes.
    """
    def __init__(self):
        """
        Initializes the BaseSetting instance.
        This method can be overridden in subclasses to set specific attributes.
        """
        self.key = None
        self.value = None
        pass

    def apply(self):
        """
        Apply the settings.
        This method should be implemented in subclasses to define how settings are applied.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    
