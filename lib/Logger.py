import inspect
import logging

from config.TestConstants import TestConstants

class Logger:
        def file_log(self):
                loggerName = inspect.stack()[1][3]
                logger = logging.getLogger(loggerName)
                fileHandler = logging.FileHandler("logs/{}".format(TestConstants.LOG_FILENAME))
                formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(module)s: %(message)s")
                fileHandler.setFormatter(formatter)
                logger.addHandler(fileHandler)
                logger.setLevel(logging.DEBUG)
                return logger

log_to_file = Logger().file_log()
