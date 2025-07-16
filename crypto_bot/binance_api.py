# crypto_bot/binance_api.py

import os
import ccxt
from dotenv import load_dotenv

# Charger les variables d'environnement (.env)
load_dotenv("../../.env")

# Récupération des clés API et configs
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
SYMBOL = os.getenv("SYMBOL", "BTC/USDT")
TIMEFRAME = os.getenv("TIMEFRAME", "1m")
TEST_MODE = os.getenv("TEST_MODE", "true").lower() == "true"

# Initialiser l'instance de Binance avec ou sans authentification
def connect_binance():
    if TEST_MODE:
        print("🔁 Mode test : connexion anonyme à Binance")
        return ccxt.binance({
            'options': {
                'defaultType': 'spot'
                }
            })
    else:
        print("🔐 Connexion à Binance avec clés API")
        return ccxt.binance({
            'apiKey': API_KEY,
            'secret': API_SECRET,
            'enableRateLimit': True,
            'options': {
                'defaultType': 'spot'
                }
        })

# Récupérer les données OHLCV depuis Binance
def fetch_ohlcv(exchange, symbol=SYMBOL, timeframe=TIMEFRAME, limit=100):
    try:
        print(f"📊 Récupération OHLCV pour {symbol} - timeframe {timeframe}")
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        return ohlcv
    except Exception as e:
        print(f"❌ Erreur lors de la récupération OHLCV : {e}")
        return []

# Exemple de test en ligne de commande
if __name__ == "__main__":
    exchange = connect_binance()
    candles = fetch_ohlcv(exchange)
    for candle in candles[-5:]:
        print(candle)
