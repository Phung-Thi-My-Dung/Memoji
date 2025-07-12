import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

class Logger:
    def __init__(self, name='vocab_logger', log_dir='logs_data', max_bytes=1_000_000, backup_count=5, console_output=True):
        """
        name: Tên logger
        log_dir: Thư mục lưu log
        max_bytes: Kích thước file log tối đa (mặc định: 1MB)
        backup_count: Số file backup giữ lại
        console_output: Có in ra console không
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Ghi cả DEBUG trở lên

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count, encoding='utf-8')
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        if console_output:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def exception(self, msg):
        self.logger.exception(msg)
