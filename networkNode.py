from flask import Flask, request, jsonify
from blockchain import Blockchain
from sys import argv
import requests
import uuid

# Make sure argv has defaults
try:
    argv[1]
except:
    argv.append("3000")
try:
    argv[2]
except:
    argv.append("192.168.1.65")

nodeAddress = "".join(str(uuid.uuid1()).split("-"))
myChain = Blockchain()
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello gang, this is my blockchain API. u bad"


@app.route('/blockchain')
def blockchain():
    return jsonify(myChain.get())


@app.route('/transaction', methods=["POST"])
def transaction():
    req = request.json
    index = myChain.createNewTransaction(req["amount"], req["sender"], req["recipient"])
    return f"Transaction Added! When the next block is mined, it will be at index {index}"


@app.route('/mine')
def mine():
    prevHash = myChain.getLastBlock().hash
    nonce = myChain.proofOfWork(prevHash)
    hash = myChain.hashBlock(prevHash, nonce)
    myChain.createNewTransaction(12.5, "00", nodeAddress)
    block = myChain.createNewBlock(nonce, prevHash, hash)
    return jsonify(block.get())


# Register a node and broadcast the node to the network
@app.route('/register-and-broadcast-node', methods=["POST"])
def regAndBroadcast():
    newNodeUrl = request.json["newNodeUrl"]
    try:
        myChain.networkNodes.index(newNodeUrl)
    except:
        myChain.networkNodes.append(newNodeUrl)

    for networkNodeUrl in myChain.networkNodes:
        uri = networkNodeUrl + "/register-node"
        r = requests.post(uri, json={'newNodeUrl': newNodeUrl})
    uri = newNodeUrl + '/register-nodes-bulk'
    requests.post(uri, json={ "allNetworkNodes": [ *myChain.networkNodes, myChain.currentNodeUrl ] })
    return "New node added successsfully!"


# Register a node with the network
@app.route('/register-node', methods=["POST"])
def regNode():
    newNodeUrl = request.json["newNodeUrl"]
    try:
        myChain.networkNodes.index(newNodeUrl)
    except:
        if newNodeUrl != myChain.currentNodeUrl:
            myChain.networkNodes.append(newNodeUrl)
    return "New node added successfully!"


# Register multiple nodes at once
@app.route('/register-nodes-bulk', methods=["POST"])
def regNodesBulk():
    req = request.json
    for node in req["allNetworkNodes"]:
        try:
            myChain.networkNodes.index(newNodeUrl)
        except:
            if node != myChain.currentNodeUrl:
                myChain.networkNodes.append(node)
    return "Nodes added in bulk!"


app.run(port=argv[1], host=argv[2], debug=True)