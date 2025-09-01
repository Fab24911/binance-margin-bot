from flask import Flask, request, jsonify
from bybit_api import place_order

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Bot Bybit OK ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Alerte reçue:", data)

    action = data.get("action")
    symbol = data.get("symbol")
    price = data.get("price")

    if not all([action, symbol, price]):
        return jsonify({"error": "Champs manquants"}), 400

    place_order(symbol, action, price)

    return jsonify({"status": "ordre envoyé"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
