class Emoji:
    def __init__(self, index, emoji_char, unicode, name, image_data=None):
        self.index = index
        self.emoji_char = emoji_char
        self.unicode = unicode
        self.name = name
        self.image_data = image_data

    def display_emoji(self):
        """Hiển thị emoji bằng ký tự Unicode."""
        try:
            # Chuyển đổi mã Unicode (U+1F603) thành ký tự emoji
            unicode_clean = self.unicode.replace("U+", "")
            emoji = chr(int(unicode_clean, 16))
            return emoji
        except ValueError as e:
            return f"Error displaying emoji: {e}"

    def get_details(self):
        """Trả về thông tin chi tiết của emoji."""
        return {
            "index": self.index,
            "emoji": self.display_emoji(),
            "unicode": self.unicode,
            "name": self.name,
            "image_data": self.image_data if self.image_data else "No image data"
        }

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo một instance của Emoji
    emoji = Emoji(
        index=2,
        emoji_char="😃",
        unicode="U+1F603",
        name="grinning face with big eyes",
        image_data="data:image/png"
    )

    # Hiển thị emoji
    print(f"Emoji: {emoji.display_emoji()}")
    
    # Hiển thị thông tin chi tiết
    details = emoji.get_details()
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")