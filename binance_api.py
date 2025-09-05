import os
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

def place_order(symbol, side, price, quantity=0.001):  # Ajuste la quantité selon ton besoin
    try:
        side = SIDE_BUY if side.lower() == "buy" else SIDE_SELL
        order = client.create_order(
            symbol=symbol.upper(),
            side=side,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=str(price)
        )
        print("✅ Ordre passé :", order)
        return order
    except Exception as e:
        print("❌ Erreur lors du passage de l'ordre :", e)
        return None
