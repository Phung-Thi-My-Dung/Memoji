import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

class _ColorState:
    """
    A helper class to determine if the terminal supports color.
    It's a singleton to avoid re-checking the environment every time.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(_ColorState, cls).__new__(cls)
            cls._instance.enabled = cls._instance._check_color_support()
        return cls._instance

    def _check_color_support(self):
        """
        Checks if the environment supports ANSI color codes.
        Returns True if colors should be enabled, False otherwise.
        """
        # 1. The `NO_COLOR` environment variable should be respected.
        if os.getenv('NO_COLOR'):
            return False

        # 2. If output is redirected to a file, disable colors.
        # `isatty()` returns True if the file descriptor is connected to a TTY(-like) device.
        if not sys.stdout.isatty():
            return False

        # 3. On Windows, modern terminals (like Windows Terminal) support ANSI.
        # Older cmd.exe does not without special handling (like colorama).
        # This check is a good heuristic for modern environments.
        return True

class ColorCodes:
    """ANSI color codes"""
    GREY = "\x1b[38;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"

class ColoredFormatter(logging.Formatter):
    """
    A custom log formatter that adds colors to log levels for terminal output.
    """
    def __init__(self, fmt, datefmt=None, style='%'):
        super().__init__()
        self.color_state = _ColorState()
        self.base_format = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey(fmt),
            logging.INFO: self.grey(fmt),
            logging.WARNING: self.yellow(fmt),
            logging.ERROR: self.red(fmt),
            logging.CRITICAL: self.bold_red(fmt)
        }

    def grey(self, text): return f"{ColorCodes.GREY}{text}{ColorCodes.RESET}"
    def yellow(self, text): return f"{ColorCodes.YELLOW}{text}{ColorCodes.RESET}"
    def red(self, text): return f"{ColorCodes.RED}{text}{ColorCodes.RESET}"
    def bold_red(self, text): return f"{ColorCodes.BOLD_RED}{text}{ColorCodes.RESET}"

    def format(self, record):
        if self.color_state.enabled:
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)
        else:
            # If colors are disabled, use the base formatter
            formatter = logging.Formatter(self.base_format)
            return formatter.format(record)

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
        self.logger.setLevel(logging.DEBUG)
        # Prevent log messages from being propagated to the root logger
        self.logger.propagate = False

        # Avoid adding handlers if they already exist
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # --- File Handler (no colors) ---
        log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")
        file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count, encoding='utf-8')
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

        # --- Console Handler (with colors) ---
        if console_output:
            console_handler = logging.StreamHandler(sys.stdout)
            # Use the ColoredFormatter for the console
            console_formatter = ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(console_formatter)
            self.logger.addHandler(console_handler)

    def log_info(self, msg):
        self.logger.info(msg)

    def log_warning(self, msg):
        self.logger.warning(msg)

    def log_error(self, msg):
        self.logger.error(msg)

    def log_debug(self, msg):
        self.logger.debug(msg)

    def log_exception(self, msg):
        self.logger.exception(msg)
