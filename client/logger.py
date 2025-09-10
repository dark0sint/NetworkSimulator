import logging

def setup_logger(log_file):
    logger = logging.getLogger('client_logger')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
