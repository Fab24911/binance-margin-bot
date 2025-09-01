import os
from bitget.openapi import bitget

# Charger les clés depuis les variables d’environnement
API_KEY = os.getenv("BITGET_API_KEY")
API_SECRET = os.getenv("BITGET_API_SECRET")
API_PASSPHRASE = os.getenv("BITGET_API_PASSPHRASE")

client = bitget.MixOrderApi(API_KEY, API_SECRET, API_PASSPHRASE)

# Exemple : marché = 'umcbl' pour USDT-M Perpetual
def place_order(symbol, action, price):
    try:
        side = 'open_long' if action.lower() == 'buy' else 'open_short'

        print(f"📤 Envoi d’un ordre {side} pour {symbol} à {price} USDT")

        response = client.place_order(
            symbol=symbol,
            marginCoin='USDT',
            size='0.01',  # Ajuste cette taille selon ton capital
            side=side,
            orderType='market',
            price='',  # Vide pour market
            market='umcbl'  # Perp USDT
        )

        print("✅ Réponse Bitget:", response)
    except Exception as e:
        print("❌ Erreur lors de l’ordre :", e)
