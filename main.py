import sys
from ulti import Logger
from model.words import Word
from base import BaseWord

word = Word("example")

word.set_pos("noun")

print(word)
print(sys.path)
a = Logger()
a.info("This is an info message.")
a.error("This is an error message.")
a.warning("This is a warning message.")
a.debug("This is a debug message.")
a.exception("This is a critical message.")