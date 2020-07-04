from datetime import datetime
import json

class Block:
    def __init__(self, index, transactions, nonce, hash, prevHash):
        self.index = index
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.nonce = nonce
        self.hash = hash
        self.previousBlockHash = prevHash

    def get(self):
        transactions = []
        for i in self.transactions:
            transactions.append(i.get())
        ret = {"index": self.index, "timestamp": str(self.timestamp), "transactions": transactions,
            "nonce": self.nonce, "hash": self.hash}
        return ret