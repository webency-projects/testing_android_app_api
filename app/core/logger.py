import logging
import os


class Logger:
    def __init__(self, name, level=logging.INFO, log_file="app.log", log_dir='logs', is_to_file=False):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s ')
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        if is_to_file:
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            file_path = os.path.join(log_dir, log_file)
            file_handler = logging.FileHandler(file_path)
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
