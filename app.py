from flask import Flask, request, jsonify
from binance_api import place_order

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Bot Binance OK ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Alerte reçue:", data)

    action = data.get("action")  # "buy" ou "sell"
    symbol = data.get("symbol")  # Ex: "BTCUSDT"
    price = data.get("price")    # Prix limite

    if not all([action, symbol, price]):
        return jsonify({"error": "Champs manquants"}), 400

    result = place_order(symbol, action, price)

    if result:
        return jsonify({"status": "ordre envoyé"}), 200
    else:
        return jsonify({"error": "échec de l'ordre"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

