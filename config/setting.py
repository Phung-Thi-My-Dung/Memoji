from base import BaseSetting

class Setting(BaseSetting):
    def __init__(self):
        """
        Initialize a Setting object with the configuration path.
        
        Args:
            config_path (str): The path to the configuration file.
        """
        super().__init__()

        self.name_game = "Memoji"
        self.version = "1.0.0"
        self.author = "Mỹ Dung and Anh Nhật"
        self.db_path = "db"
        self.max_words = 10
        self.points_per_correct = 10
        self.player_name = "Player"
        self.language = "en"
        self.theme = "default"


    def set_player_name(self, name):
        """
        Set the player's name.
        
        Args:
            name (str): The name of the player.
        """
        self.player_name = name

    def get_player_name(self):
        """
        Get the player's name.
        
        Returns:
            str: The name of the player.
        """
        return self.player_name

