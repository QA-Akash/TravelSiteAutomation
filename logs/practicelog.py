import logging


class LoggerDemoPractice:
    def logging_practice(self):
        # 1
        new_logger = logging.getLogger(LoggerDemoPractice.__name__)
        # 2
        new_logger.setLevel(logging.WARNING)
        # 3
        file_handler = logging.FileHandler("../logs/demo_practice1.log", mode="a")
        # 4
        formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                       datefmt='%m/%d/%y %I:%M:%S %p')
        # 5
        file_handler.setFormatter(formatter1)
        # 6
        new_logger.addHandler(file_handler)
        # 7
        new_logger.debug("Debug log statement")
        new_logger.warning("warning log statement")
        new_logger.critical("Critical log statement")
        new_logger.debug("Error log statement")
        new_logger.critical("critiCal log statement")
        new_logger.warning("warning log statement")


new_obj_logger = LoggerDemoPractice()
new_obj_logger.logging_practice()
