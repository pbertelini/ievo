# -*- coding: utf-8 -*-

import logging
import configparser
from sys import exit

from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)

config = configparser.RawConfigParser(allow_no_value=True)
config.read('ievo_conv.cfg')

formatter = logging.Formatter(config.get("log", "format"))
filename = config.get("log", "log_path") + config.get("log", "log_file")

file_handler = TimedRotatingFileHandler(filename, when='midnight', interval=1)
file_handler.setFormatter(formatter)
file_handler.suffix = '%Y%m%d'

if config.get("log", "level") == 'DEBUG':
    logger.setLevel(logging.DEBUG)

elif config.get("log", "level") == 'INFO':
    logger.setLevel(logging.INFO)

elif config.get("log", "level") == 'WARNING':
    logger.setLevel(logging.WARNING)

elif config.get("log", "level") == 'ERROR':
    logger.setLevel(logging.ERROR)

elif config.get("log", "level") == 'CRITICAL':
    logger.setLevel(logging.CRITICAL)

else:
    print('[ !! ] invalid log level! quitting...')
    exit(0)

logger.addHandler(file_handler)
