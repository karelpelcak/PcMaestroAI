import logging

# Konfigurace logování
logging.basicConfig(filename='utils/app.log', level=logging.INFO)

def log(message):
    logging.info(message)
