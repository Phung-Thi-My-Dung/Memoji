import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from words import Word
from session import Session

__all__ = [
    "Word", "Session"]