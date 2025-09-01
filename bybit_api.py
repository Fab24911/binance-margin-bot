import os
from pybit.unified_trading import HTTP

# Charger les clés API depuis les variables d'environnement
API_KEY = os.getenv("BYBIT_API_KEY")
API_SECRET = os.getenv("BYBIT_API_SECRET")

# Initialiser le client Bybit (Unified Trading)
session = HTTP(
    api_key=API_KEY,
    api_secret=API_SECRET,
)

def place_order(symbol, action, price):
    try:
        side = "Buy" if action.lower() == "buy" else "Sell"

        print(f"📤 Envoi ordre {side} sur {symbol} à {price}")

        response = session.place_order(
            category="linear",          # Pour USDT Perpetual
            symbol=symbol,
            side=side,
            order_type="Market",
            qty=0.01,                   # ⚠️ À adapter selon ton capital
            time_in_force="GoodTillCancel"
        )

        print("✅ Réponse Bybit:", response)
    except Exception as e:
        print("❌ Erreur Bybit:", e)
