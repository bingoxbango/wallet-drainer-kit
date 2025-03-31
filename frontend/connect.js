document.getElementById("connectButton").addEventListener("click", async () => {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
  
    // Send wallet info to backend
    fetch("http://localhost:5000/connect", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ wallet: accounts[0] })
    });
  
    alert("Wallet connected! Please approve to mint.");
  });
  