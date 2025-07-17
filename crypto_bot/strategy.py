# crypto_bot/strategy.py

def generate_signal(df):
    """
    Prend un DataFrame contenant les indicateurs (RSI, MACD, EMA).
    Retourne un signal : 'buy', 'sell' ou None.
    """

    # On prend la dernière ligne avec les indicateurs
    latest = df.iloc[-1]

    # Conditions RSI
    rsi = latest["rsi"]
    if rsi is None or rsi != rsi:  # NaN check
        return None

    # Conditions MACD
    macd = latest["macd"]
    macd_signal = latest["macd_signal"]

    # Conditions EMA
    ema20 = latest["ema20"]
    ema50 = latest["ema50"]
    price = latest["close"]

    # Stratégie BUY :
    if (
        rsi < 30 and                      # RSI en survente
        macd > macd_signal and            # MACD croise au-dessus du signal
        ema20 > ema50 and                 # EMA court terme > EMA long terme
        price > ema20                     # Le prix est au-dessus de l'EMA20
    ):
        return "buy"

    # Stratégie SELL :
    if (
        rsi > 70 and                      # RSI en surachat
        macd < macd_signal and            # MACD croise en dessous du signal
        ema20 < ema50 and                 # EMA court terme < EMA long terme
        price < ema20                     # Le prix est en-dessous de l'EMA20
    ):
        return "sell"

    return None
