# crypto_bot/logger.py

import logging
import os
from datetime import datetime

# Créer le dossier de logs s’il n’existe pas
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Nom du fichier de log basé sur la date
log_filename = datetime.now().strftime("trades_%Y-%m-%d.log")
log_filepath = os.path.join(LOG_DIR, log_filename)

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler()  # Affiche aussi dans le terminal
    ]
)

# Exporter un logger réutilisable dans tout le projet
logger = logging.getLogger("crypto_bot_logger")
