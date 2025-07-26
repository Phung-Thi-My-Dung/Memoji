
class BaseSession:
    """
    File này chứa định nghĩa chung cho session trong hệ thống,
    bao gồm các phương thức cơ bản để quản lý session.
    Các lớp con sẽ kế thừa và mở rộng các phương thức này.
    Attributes:
        - session_id (str): ID duy nhất của session 

    """
    def __init__(self, session_id: str):
        self.session_id = session_id

    def get_session_id(self) -> str:
        return self.session_id

    def set_session_id(self, session_id: str):
        self.session_id = session_id

    def is_valid(self) -> bool:
        # Placeholder for actual validation logic
        return True