from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Bot Binance OK"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Alerte reçue:", data)
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
