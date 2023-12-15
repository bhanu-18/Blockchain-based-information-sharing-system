Steps to run the code:
1. Download the Code file from github.
2. Make sure you have installed Python 3.7.0, Ganache 2.7.1, Nodejs 18.17.1, Winrar 6.24
in your system / Otherwise install them using the terminal by executing : pip install django = = 2.1.7 urlib3 = = 1. 25.9 jinja2 = = 3. 0. 3 itsdangerous = = 2.0.1 markupsafe = = 2.0.1 werkzeng = = D.16 protobuf = = 3.2.0 web 3 = = 5.12.3 flask = = 1.1.1.1 - - user .
3. This execution is functional only on Windows Operating System.
4. When you install and run ganache,it will generate network details .Copy that .
5. Add metamask extension to chrome.[Metamask acts as a secure wallet and facilitates
seamless interaction with Ethereum-based applications directly from your Chrome].
6. In the metamask,create two accounts:
1-Create a sample account by not attaching any network details.
2-Create a second account and add the network details of ganache [the one that you have copied above].
7. Then install truffle in the terminal by using “npm -g install truffle”
8. Go to the folder and click on “runblockchain.bat”file , then run the command : “truffle
migrate” - to compile the smart contract file and then a contract address would be
generated.
9. Copy this Contract Address and add it in “app.py file” (Replace it here
deployed_contract_address=”----------- ”).
10. Then click on file“run.bat”, it will generate a portal address where the web3 data sharing
website is hosted.
11. Copy paste this portal address in the browser and the Web3 Data Sharing Platform will be
up and running.

All the files/folders in this project:
1. build folder - When smart contract file is compiled, json file is generated - contains the structure of the functions
2. contracts folder - Contains all the smart contract files - Solidity files are in it.
3. migrations folder - contains the details that need to be compiled, we need to
mention the contract name that we want to compile
4. static folder - Contains that CSS and JavaScript files
5. templates folder - Contains the HTML files
6. test folder - Empty folder, created when migrations are done. Contains warnings if
any
7. App.py - Main code file
8. run.bat - Windows batch file to run the server
9. runblockchain.bat - Windows batch file to run the server
10. Sharing.json - To connect to the app file
11. truffle-config.js - To invoke the compiler- npm compiler
