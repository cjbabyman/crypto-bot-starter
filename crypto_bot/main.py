import time
from crypto_bot.binance_api import connect_binance, fetch_ohlcv
from crypto_bot.indicators import calculate_indicators
from crypto_bot.strategy import generate_signal
from crypto_bot.logger import logger

# Initialisation Binance
exchange = connect_binance()

# Paramètres du bot
symbol = "BTC/USDT"
timeframe = "1m"
limit = 100
stop_loss_pct = 0.02        # -2%
take_profit_pct = 0.04      # +4%

# Variables d’état
position = None
entry_price = None

logger.info("🚀 Bot lancé avec succès.")

while True:
    print("🔄 Nouveau cycle...\n")
    logger.info("🔄 Nouveau cycle de trading...")

    # 1. Récupérer données OHLCV
    ohlcv = fetch_ohlcv(exchange, symbol, timeframe, limit)
    if not ohlcv:
        print("⚠️ Aucune donnée récupérée, on attend...")
        logger.warning("⚠️ Données manquantes, cycle ignoré.")
        time.sleep(60)
        continue

    logger.info(f"📊 {len(ohlcv)} bougies récupérées pour {symbol}")

    # 2. Calculer les indicateurs
    df = calculate_indicators(ohlcv)

    # 3. Obtenir le dernier signal
    signal = generate_signal(df)

    # 4. Dernier prix
    price = df.iloc[-1]["close"]
    if isinstance(signal, str):
        print(f"📈 Prix actuel : {price:.2f} | Signal : {signal.upper()}")
        logger.info(f"📈 Prix actuel : {price:.2f} | Signal : {signal}")
    else:
        print(f"📈 Prix actuel : {price:.2f} | Aucun signal")
        logger.info(f"📈 Prix actuel : {price:.2f} | Aucun signal détecté")

    # 5. Logique de trading
    if not position:
        if signal == "buy":
            entry_price = price
            position = "long"
            print(f"✅ Achat à {entry_price:.2f}")
            logger.info(f"✅ Position ouverte à l'achat : {entry_price:.2f}")
    else:
        stop_loss_price = entry_price * (1 - stop_loss_pct)
        take_profit_price = entry_price * (1 + take_profit_pct)

        if price <= stop_loss_price:
            print(f"❌ STOP LOSS déclenché à {price:.2f}")
            logger.warning(f"❌ STOP LOSS déclenché à {price:.2f}")
            position = None
            entry_price = None

        elif price >= take_profit_price:
            print(f"🎯 TAKE PROFIT atteint à {price:.2f}")
            logger.info(f"🎯 TAKE PROFIT atteint à {price:.2f}")
            position = None
            entry_price = None

        elif signal == "sell":
            print(f"🚪 Signal SELL à {price:.2f}, sortie manuelle")
            logger.info(f"🚪 Vente manuelle sur signal SELL à {price:.2f}")
            position = None
            entry_price = None

    print("🕒 Pause 60 secondes...\n")
    time.sleep(60)

