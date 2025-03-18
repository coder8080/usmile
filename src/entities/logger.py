import logging

logger = logging.getLogger("usmile")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
debug_file = logging.FileHandler("logs/debug.log")
error_file = logging.FileHandler("logs/error.log")

console_handler.setLevel(logging.DEBUG)
debug_file.setLevel(logging.DEBUG)
error_file.setLevel(logging.ERROR)

logger.addHandler(console_handler)
logger.addHandler(debug_file)
logger.addHandler(error_file)
