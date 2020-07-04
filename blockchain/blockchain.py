from .transaction import Transaction
from hashlib import sha256
from .block import Block
from sys import argv
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.currentNodeUrl = "http://" + argv[2] + ":" + argv[1]
        self.networkNodes = []
        self.createNewBlock(100, "0", "0")
    
    def get(self):
        chain = []
        pendingTransactions = []
        for i in self.chain:
            chain.append(i.get())
        for i in self.pendingTransactions:
            pendingTransactions.append(i.get())
        ret = {
            "URL": self.currentNodeUrl,
            "attached nodes": self.networkNodes,
            "chain": chain,
            "pendingTransactions": pendingTransactions
            }
        return ret

    def createNewBlock(self, nonce, previousBlockHash, hash):
        """Generates a new block for the chain that contains the new transactions

        Args:
            nonce (int): Proof of work
            previousBlockHash (string): Hash of previous block
            hash (string): Data for new block
        """
        newBlock = Block(len(self.chain), self.pendingTransactions, nonce, hash, previousBlockHash)
        self.pendingTransactions = []
        self.chain.append(newBlock)
        return newBlock

    def getLastBlock(self):
        """Gets the latest block in the chain

        Returns:
            Block: the latest block
        """
        if (len(self.chain) == 0):
            return -1
        else:
            return self.chain[len(self.chain)-1]

    def createNewTransaction(self, amount, sender, recipient):
        """Creates a new transaction

        Args:
            amount (int): amount to be sent
            sender (string): address of the sender
            recipient (string): address of the recipient
        """
        newTransaction = Transaction(amount, sender, recipient)
        self.pendingTransactions.append(newTransaction)
        return self.getLastBlock().index + 1

    def hashBlock(self, previousBlockHash, nonce):
        dataString = previousBlockHash + str(nonce) + str(self.pendingTransactions)
        hash = sha256()
        hash.update(dataString.encode("utf-8"))
        hash = hash.hexdigest()
        return hash
        
    def proofOfWork(self, previousBlockHash):
        nonce = 0
        while True:
            hash = self.hashBlock(previousBlockHash, nonce)
            if hash[0:4] == "0000":
                break
            nonce += 1
        return nonce