import inspect
import logging


class CustomLoggerDemo:
    def custom_logger(self, loglevel=logging.DEBUG):
        # 1 set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # new_logger = logging.getLogger(CustomLoggerDemo.__name__)
        new_logger = logging.getLogger(logger_name)
        # 2
        new_logger.setLevel(logging.DEBUG)
        # 3
        file_handler = logging.FileHandler("automation_logs.log", mode="a")
        # 4
        formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                       datefmt='%m/%d/%y %I:%M:%S %p')
        # 5
        file_handler.setFormatter(formatter1)
        # 6
        new_logger.addHandler(file_handler)
        # # 7
        return new_logger

        # new_logger.debug("Debug log statement")
        # new_logger.warning("warning log statement")
        # new_logger.critical("Critical log statement")
        # new_logger.debug("Error log statement")
        # new_logger.critical("critcial log statement")
        # new_logger.warning("warning log statement")

