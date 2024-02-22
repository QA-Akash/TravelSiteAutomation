import logging
import logger_demo  # this will return the class name of the logger to know from where the logs are coming from
"""
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future 
(e.g. ‘disk space low’). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running
"""

# print("This is the statement")
# logging.info("This is statement")
# logging.warning("This is statement")  # WARNING:root:This is statement

# logging.basicConfig(level=logging.DEBUG, filename="Demologs.logs", filemode="a")
# Here we have successfully changed the log level to Debug from Warning which is by default

# logging.basicConfig(filename="Demologs.logs", filemode="a")
# here we didn't provide the level so its taken warning as default level

logging.basicConfig(level=logging.DEBUG, filename="../logdemo/demo_logs1.logs", filemode="a", format='%(asctime)s - %('
                                                                                                     'levelname)s :- %('
                                                                                                     'message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


# this is to configure the path of your file into the folder to move the logs to specific folder
# this is to change the directory of the logging file


class LoggingPractice:

    def add_num(self, a, b):
        """
        :param a: first input
        :param b: second input
        :return: addition
        """
        return a + b

    def multiply(self, a, b):
        """
        multiplication of the number
        :param a: first number
        :param b: second number
        :return: multiplication
        """
        return a * b


obj_logging = LoggingPractice()
sum_result = obj_logging.add_num(24, 26)
# print(f"sum of the two number is: {sum_result}")
logging.debug(f"sum of the two number is: {sum_result}")
logging.info(f"sum of the two number is: {sum_result}")
logging.warning(f"sum of the two number is: {sum_result}")
logging.error(f"sum of the two number is: {sum_result}")
logging.critical(f"sum of the two number is: {sum_result}")
# this is the hierarchy
multiply_result = obj_logging.multiply(30, 10)
# print(f"sum of the two number is: {multiply_result}")
logging.info(f"sum of the two number is: {multiply_result}")
logging.debug(f"sum of the two number is: {multiply_result}")
logging.critical(f"sum of the two number is: {multiply_result}")

# Now this both will print in the console and show the logging result with the warning
# only warning, error, critical will be printed in the console
