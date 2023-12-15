// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.21 <= 0.9;

contract Sharing {
    string public users;
    string public information;
   

    function addUsers(string memory u) public {
        users = u;	
    }

    function getUsers() public view returns (string memory) {
        return users;
    }


    function addinformation(string memory ca) public {
        information = ca;
    }

    function getinformation() public view returns (string memory) {
        return information;
    }

   

    constructor() public {
        users = "empty";
    information = "empty";
    
    
    }
}