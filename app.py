from flask import Flask, render_template, request 
from datetime import datetime
import json
from web3 import Web3, HTTPProvider
import os
import datetime

app = Flask(__name__)


global details, user


def readDetails(contract_type):
    global details
    details = ""
    blockchain_address = 'http://127.0.0.1:9545' #Blokchain connection IP
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'Sharing.json' #counter feit contract code
    deployed_contract_address = '0x5682CF04494D4528c5A86f03f762bb02FB902473' #hash address to access counter feit contract
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    file.close()
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi) #now calling contract to access data
    if contract_type == 'adduser':
        details = contract.functions.getUsers().call()
    if contract_type == 'information':
        details = contract.functions.getinformation().call()
    if len(details) > 0:
        if 'empty' in details:
            details = details[5:len(details)]

    

def saveDataBlockChain(currentData, contract_type):
    global details
    global contract
    details = ""
    blockchain_address = 'http://127.0.0.1:9545'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'Sharing.json' #Counter feit contract file
    deployed_contract_address = '0x5682CF04494D4528c5A86f03f762bb02FB902473' #contract address
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    file.close()
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    readDetails(contract_type)
    if contract_type == 'adduser':
        details+=currentData
        msg = contract.functions.addUsers(details).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
    if contract_type == 'information':
        details+=currentData
        msg = contract.functions.addinformation(details).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)



@app.route('/AddUser', methods=['POST'])
def AddUser():
    if request.method == 'POST':
        
        username = request.form['t1']
        password = request.form['t2']
        number = request.form['t3']
        email = request.form['t4']
        address = request.form['t5']

        status = "none"
        readDetails('adduser')
        arr = details.split("\n")

        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[1] == username:
                status = username + " Already Exists."
                context = status  
                return render_template('AddUser.html', msg=context)
                break

        if status == "none":
            data = username+"#"+password+"#"+number+"#"+email+"#"+address+"\n"
            saveDataBlockChain(data, "adduser")
            context = "SignUp Completed and details are saved to blockchain"  
            return render_template('AddUser.html', msg=context)
        else:
            context = 'Error in signup process'  
            return render_template('AddUser.html', msg=context)


@app.route('/UserLoginAction', methods=['POST'])
def UserLoginAction():
    if request.method == 'POST':
        global user
        username = request.form['t1']
        password = request.form['t2']
        user = username
        status = "none"
        readDetails('adduser')
        arr = details.split("\n")

        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == username and array[1] == password:
                status = 'success'
                break

        if status == 'success':
            context = username + ' Welcome.'
            return render_template('UserScreen.html', msg=context)
        else:
            context = 'Invalid Details'
            return render_template('Login.html', msg=context)


def getusernames(current_user_name):
    readDetails('adduser')
    arr = details.split("\n")
    user_names = []

    for i in range(len(arr) - 1):
        array = arr[i].split("#")
        username = array[0]
        if username != current_user_name:
            user_names.append(username)

    return user_names


@app.route('/AddInformation', methods=['GET'])
def AddInformations():
    global user
    username = getusernames(user)
    return render_template('AddInformation.html', username_all=username)


@app.route('/AddInformation', methods=['POST'])
def AddInformation():
    global user
    status = "none"
    name = request.form['username']
    file = request.files['t1']
    
    filename = file.filename
    print("@@ Input posted = ", filename)
    file_path = os.path.join('static/files/', filename)
    file.save(file_path)
    
    readDetails('information')
    arr = details.split("\n")

    for i in range(len(arr)-1):
        array = arr[i].split("#")
        if array[1] == filename:
            context = "Details Already Exists"
            return render_template('AddInformation.html', msg=context)
    
    if status == "none":
        data = user+"#"+name+"#"+filename+"\n"
        saveDataBlockChain(data, "information")
        context = 'Information Added Successfully to Blockchain.'
        return render_template('AddInformation.html', msg=context)
    else:
        context = "Error in the process."
        return render_template('AddInformation.html', msg=context)




@app.route('/CheckInformation', methods=['GET', 'POST'])
def CheckInformation():

    if request.method == 'GET':
        global user
        
        output = '<table border=1 align=center width=100%>'
        font = '<font size=3 color=black>'
        headers = ['Sent By','File Name', 'Download the file']

        output += "<tr>"
        for header in headers:
            output += "<th>" + font + header + "</th>"
        output += "</tr>"

        
        readDetails('information')

        arr = details.split("\n")
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[1] == user:
                output += "<tr><td>" + font + array[0] + "</td>"
                output += "<td>" + font + array[2] + "</td>"
                output += f'<td><a href="/static/files/{array[2]}" download="{array[2]}">Download</a></td>'

        output += "</table><br/><br/><br/>"

        return render_template('CheckInformation.html', msg=output)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
       return render_template('index.html', msg='')

@app.route('/AddInformation', methods=['GET', 'POST'])
def AddInformationss():
    if request.method == 'GET':
       return render_template('AddInformation.html', msg='')

@app.route('/AddUser', methods=['GET', 'POST'])
def AddUsers():
    if request.method == 'GET':
       return render_template('AddUser.html', msg='')

@app.route('/CheckInformation', methods=['GET', 'POST'])
def CheckInformations():
    if request.method == 'GET':
       return render_template('CheckInformation.html', msg='')

@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
       return render_template('Login.html', msg='')

@app.route('/UserScreen', methods=['GET', 'POST'])
def UserScreen():
    if request.method == 'GET':
       return render_template('UserScreen.html', msg='')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
       return render_template('index.html', msg='')

    
if __name__ == '__main__':
    app.run()       
