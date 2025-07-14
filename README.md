# Crypto Bot Starter

A beginner-friendly Python crypto trading bot powered by real-time Binance data, technical indicators (RSI, MACD, EMA), and clean modular design. Perfect for learning algorithmic trading and proving DevOps/Linux automation skills.

## Features

- Live OHLCV data from Binance (via CCXT)
- Built-in indicators: RSI, MACD, EMA20/50 (pandas + ta-lib)
- Entry/exit logic with stop loss & take profit
- Logs all trades and strategy events
- .env for API key safety

## Tech Stack

- Python 3.10+
- CCXT
- TA-Lib
- dotenv
- systemd-ready for deployment

## Project Structure

crypto-bot-starter/
├── README.md
├── .env.example
├── requirements.txt
├── crypto_bot/
│   ├── __init__.py
│   ├── indicators.py
│   ├── strategy.py
│   ├── binance_api.py
│   └── main.py
└── logs/
    └── trades.log

## Setup

cp .env.example .env
# Add your Binance API keys in the new .env file

pip install -r requirements.txt

python3 crypto_bot/main.py

## Disclaimer

This project is educational and not financial advice. Use testnet or small funds.

Maintained by Victor L. Callewaert – aspiring Linux Engineer & Crypto DevOps specialist.
