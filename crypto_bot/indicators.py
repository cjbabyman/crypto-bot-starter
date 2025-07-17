# crypto_bot/indicators.py

import pandas as pd
import ta  # Assure-toi que c'est bien installé avec : pip install ta

def calculate_indicators(ohlcv):
    """
    Calcule RSI, MACD, EMA20 et EMA50 à partir des données OHLCV (listes de listes).
    Retourne un DataFrame pandas avec les indicateurs.
    """

    # Transformer les données OHLCV en DataFrame
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)

    # Convertir les colonnes nécessaires en float
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    # ➤ Ajouter RSI
    rsi_indicator = ta.momentum.RSIIndicator(close=df["close"], window=14)
    df["rsi"] = rsi_indicator.rsi()

    # ➤ Ajouter MACD
    macd_indicator = ta.trend.MACD(close=df["close"])
    df["macd"] = macd_indicator.macd()
    df["macd_signal"] = macd_indicator.macd_signal()

    # ➤ Ajouter EMA
    ema20 = ta.trend.EMAIndicator(close=df["close"], window=20)
    ema50 = ta.trend.EMAIndicator(close=df["close"], window=50)
    df["ema20"] = ema20.ema_indicator()
    df["ema50"] = ema50.ema_indicator()

    return df
