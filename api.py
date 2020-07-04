from flask import Flask, request, jsonify
from blockchain import Blockchain
import uuid

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