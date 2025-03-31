# wallet-drainer-kit
   🎣 Phishing Site (frontend/)
       └── index.html
             ↓
   👤 Victim visits fake "Claim Wallet" or "Mint NFT" page
             ↓
   🦊 MetaMask Triggered (connect.js)
             ↓
   📩 Wallet sent to Backend API (/connect route in routes.py)
             ↓
   🔧 Backend (app.py + wallet_logic.py)
         - Builds approve() or permit() TX
         - Signs using attacker's private key (.env)
             ↓
   🧱 Smart Contract (Drainer.sol)
         - transferFrom(victim, attacker, tokens)
             ↓
   💰 Tokens stolen (ETH, USDC, NFTs)
             ↓
   🖥️ Admin Panel (dashboard.html + monitor.js)
         - Shows: Wallet, Status, Tokens, TX Hash
