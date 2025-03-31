from web3 import Web3
import os

INFURA_URL = os.getenv("INFURA_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
MY_WALLET = os.getenv("DRAINER_WALLET")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def trigger_drain(victim_wallet):
    # Pretend to send a malicious approve() or permit()
    print(f"Draining wallet: {victim_wallet}")
    # In a real attack, it would send a contract call here
