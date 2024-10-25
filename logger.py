import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger('cbz-unzipper-logger')
logger.setLevel(logging.DEBUG)

log_file_name = 'logs/cbz_unzipper_debug.log'
with open(log_file_name, 'a'):
    pass

handler = RotatingFileHandler('logs/cbz_unzipper_debug.log', maxBytes=5000000, backupCount=5)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
