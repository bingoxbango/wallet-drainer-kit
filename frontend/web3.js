// Load the ethers.js library (used for blockchain interaction)
const { ethers } = window;

if (typeof window.ethereum !== 'undefined') {
  window.web3 = new ethers.providers.Web3Provider(window.ethereum);
} else {
  alert("Please install MetaMask to continue.");
}
