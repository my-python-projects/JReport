import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # Configuração do logger
    logger = logging.getLogger('jreport')
    logger.setLevel(logging.DEBUG)

    # Formato do log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Handler para o console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Handler para o arquivo de log (com rotação)
    file_handler = RotatingFileHandler('./logs/jreport.log', maxBytes=10000000, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Adicionar handlers ao logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
