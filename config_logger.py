from loguru import logger
import sys


def configure_logger(logging_level='WARNING'):
    logging_format = '<green>{time:DD MMM YYYY | HH:mm:ss}</green> | ' \
                     '<level>{level}</level> | ' \
                     '<bold>{message}</bold>'

    logger.remove()
    logger.add(sys.stderr,
               colorize=True,
               level=logging_level,
               format=logging_format)

    logger.debug('Loguru is configured!')


if __name__ == '__main__':
    configure_logger()
    logger.warning('This module is intended to be imported into main.py.')

