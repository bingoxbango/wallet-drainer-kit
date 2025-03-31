# wallet-drainer-kit
docker-compose.yml
Orchestrates how the app runs.

Starts all containers: backend server, phishing site (frontend), and admin panel.

Each part is isolated but networked internally.

.env
Stores secrets/config like:

Wallet private keys

Web3 provider URLs (e.g., Infura, Alchemy)

Wallet address to send stolen funds to

backend/ — The Command Center
File	Description
app.py (or index.js)	Entry point of the backend server (Flask or Express). Handles HTTP requests from the frontend.
routes.py	Defines all the backend routes like /connect, /drain, /log, etc.
wallet_logic.py	Contains Web3 logic for interacting with the Ethereum blockchain: crafting token approvals, sending drain transactions.
phishing_db.sqlite	Stores victim logs: IPs, wallets, drain status, timestamps. (Sometimes replaced with MongoDB or Firebase in advanced kits.)
requirements.txt	Python dependencies (Flask, web3, SQLAlchemy, etc.) for Docker to install.

frontend/ — The Fake Website
File	Description
index.html	Main phishing webpage — typically mimics OpenSea, Uniswap, airdrop pages, etc.
connect.js	JavaScript to trigger MetaMask or WalletConnect — asks victim to “connect wallet” and sign a transaction or approval.
web3.js	The Web3 interface (ethers.js or web3.js library) used to talk to MetaMask or mobile wallets.
styles.css	CSS styling to make the site look convincing.
phishing_logic.js	Main logic that executes malicious wallet interactions (e.g., token approvals, fake transactions).

smart-contract/ — The Actual Drainer
File	Description
Drainer.sol	Malicious Solidity smart contract that does the draining — typically uses transferFrom() or permit() to steal tokens.
deploy.js	JavaScript script (Node + Hardhat or Web3) that deploys Drainer.sol to the blockchain.
compiled/Drainer.json	ABI and bytecode for the compiled contract — needed by the backend to call contract functions.

admin-panel/ — Real-Time Monitoring UI
File	Description
dashboard.html	Web UI for the scammer — shows live wallet connections, ETH/NFT values, “Drain Now” buttons.
monitor.js	JavaScript that fetches backend data via API and renders victim info in the dashboard.
config.json	Configuration settings: auto-drain rules, token filters, blacklists, developer cut %, etc.

logs/ — Stolen Data Storage
File	Description
victims.log	Text or JSON log of wallet addresses, connected IPs, time of drain, asset values.
(Optional) tx_hashes.log	Track drain transaction hashes to monitor movement of funds.

