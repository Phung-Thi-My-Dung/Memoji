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
    
    def generate_next_id(self, last_id):
        """
        Tạo ID tiếp theo dựa trên ID cuối cùng được cung cấp.

        Args:
            last_id (str): ID cuối cùng trong chuỗi (ví dụ: 'w000020').

        Returns:
            str: ID tiếp theo (ví dụ: 'w000021'), hoặc None nếu định dạng ID không hợp lệ.
        """
        if not isinstance(last_id, str) or len(last_id) < 2 or not last_id[0].isalpha():
            print("Lỗi: ID cuối cùng không hợp lệ. Định dạng phải bắt đầu bằng chữ cái theo sau là số.")
            return None

        # Tách tiền tố chữ cái và phần số
        prefix = last_id[0]
        try:
            current_number = int(last_id[1:])
        except ValueError:
            print("Lỗi: Phần số của ID không hợp lệ.")
            return None

        # Tăng số lên 1
        next_number = current_number + 1

        # Định dạng lại số để giữ nguyên số chữ số 0 đệm
        # Ví dụ: 'w000020' -> 'w' + '000021'
        # Tính toán số lượng số 0 cần đệm
        num_digits_in_current_id = len(last_id) - 1 # Bỏ đi ký tự chữ cái đầu tiên
        next_id = f"{prefix}{next_number:0{num_digits_in_current_id}d}"

        return next_id

