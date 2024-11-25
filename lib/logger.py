import logging

class Logger:
    def __init__(self, log_file="engine.log", level=logging.INFO):
        self.logger = logging.getLogger("BitoshiBlockamoto")
        self.logger.setLevel(level)
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - 
%(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

