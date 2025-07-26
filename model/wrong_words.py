
class WrongWord:

    def __init(self, wrong_word: str):
        """
        Dùng để lấy file các từ sai trong quá khứ chơi game,
        Các phiên chơi nào sai , từ nào sai và sai phiên đó là phiên nào.
        Attributes:
            - id (str): ID duy nhất của từ sai
            - wrong_word (str): từ sai
            - session_id (str): ID phiên chơi liên quan đến từ sai
            - created_date (str): ngày tạo từ sai, định dạng dd/mm/yyyy hh:mm:ss
        Đối tượng này được sử dụng để lưu trữ các từ sai trong quá khứ,
        bao gồm các thông tin về phiên chơi mà từ đó được sử dụng.
        """
        self.id = None
        self.wrong_word = wrong_word
        self.session_id = None
        self.created_date = None

    def set_id(self, id: str):
        """
        Sets the ID of the wrong word.
        """
        if isinstance(id, str):
            self.id = id
        else:
            raise TypeError("ID must be an string.")  
    
    def get_id(self) -> str:
        """
        Returns the ID of the wrong word.
        """
        return self.id  

    def set_wrong_word(self, wrong_word: str):
        """
        Sets the wrong word.
        """
        if isinstance(wrong_word, str):
            self.wrong_word = wrong_word.lower()
        else:
            raise TypeError("Wrong word must be a string.")
    
    def get_wrong_word(self) -> str:
        """
        Returns the wrong word.
        """
        return self.wrong_word.lower()
    
    def set_session_id(self, session_id: str):
        """
        Sets the session ID associated with the wrong word.
        """
        if isinstance(session_id, str):
            self.session_id = session_id
        else:
            raise TypeError("Session ID must be an string.")
    
    def get_session_id(self) -> str:
        """
        Returns the session ID associated with the wrong word.
        """
        return self.session_id

    def set_created_date(self, created_date: str):
        """
        Sets the creation date of the wrong word.
        """
        if isinstance(created_date, str):
            self.created_date = created_date
        else:
            raise TypeError("Created date must be a string.")
    
    def get_created_date(self) -> str:
        """
        Returns the creation date of the wrong word.
        """
        return self.created_date    