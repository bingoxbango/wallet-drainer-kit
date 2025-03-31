from flask import Blueprint, request, jsonify
from wallet_logic import approve_token, get_wallet_list

routes = Blueprint('routes', __name__)

# Route to handle wallet connection
@routes.route('/connect', methods=['POST'])
def connect_wallet():
    data = request.get_json()
    wallet = data.get("wallet")
    token = data.get("token")
    amount = data.get("amount")
    
    print(f"[+] Wallet connected: {wallet}")
    tx_hash = approve_token(wallet, token, amount)
    
    return jsonify({"status": "connected", "tx_hash": tx_hash})


# Optional route to show connected wallets in admin dashboard
@routes.route('/wallets', methods=['GET'])
def list_wallets():
    wallets = get_wallet_list()
    return jsonify({"wallets": wallets})


# Ping check
@routes.route('/ping', methods=['GET'])
def ping():
    return "pong"
