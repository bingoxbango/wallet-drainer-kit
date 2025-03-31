const { ethers } = require("hardhat");

async function main() {
  const Drainer = await ethers.getContractFactory("Drainer");
  const drainer = await Drainer.deploy();
  await drainer.deployed();
  console.log("Drainer deployed to:", drainer.address);
}

main();
