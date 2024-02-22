import logging


# logging module is builtin in the python


class Logging_Demo:
    def sample_logger(self):
        """
        # Create logger
        # create console handler or file handler and set the log level
        # create formatter - how you want your logs to be formatted
        # add formatter to console or file
        # add console handler to the logger
        # application code
       :return:
       """
        # Create logger or utility        #  obj will help to set the level
        # logger = logging.getLogger("demo_log")
        logger = logging.getLogger(Logging_Demo.__name__)
        logger.setLevel(logging.DEBUG)

        # create console handler or file handler and set the log level to display logs on console then have to
        # configure the console handler and to display logs in files then have to configure the file handler
        ch = logging.StreamHandler()
        fh = logging.FileHandler("demo_file_for_logs.log", mode="a")

        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%m/%d/%Y '
                                                                                                      '%I:%M:%S %p')
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        # add formatter to console or file
        ch.setFormatter(formatter)
        fh.setFormatter(file_formatter)

        # add console handler to the logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        # application code
        logger.debug("Debug log statement")
        logger.info("Info log statement")
        logger.warning("Warning log statement")
        logger.error("Error log statement")
        logger.critical("Critical log statement")


logger_obj = Logging_Demo()
logger_obj.sample_logger()

""" 
Output is
02/13/2024 05:41:22 PM - DEBUG - any_demo_log - Debug log statement
02/13/2024 05:41:23 PM - INFO - any_demo_log - Info log statement
02/13/2024 05:41:23 PM - WARNING - any_demo_log - Warning log statement
02/13/2024 05:41:23 PM - ERROR - any_demo_log - Error log statement
02/13/2024 05:41:23 PM - CRITICAL - any_demo_log - Critical log statement
"""
