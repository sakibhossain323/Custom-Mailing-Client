import logging


def email_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s: %(message)s')
    file_handler = logging.FileHandler('Logs/emails_sent.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def error_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s:%(funcName)s: %(message)s')
    file_handler = logging.FileHandler('Logs/errors.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
