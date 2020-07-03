from datetime import datetime

class Block:
    def __init__(self, index, transactions, nonce, hash, prevHash):
        self.index = index
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.nonce = nonce
        self.hash = hash
        self.previousBlockHash = prevHash

    def __repr__(self):
        return (
        "\n{\n" +
        f"index: {self.index}\n" +
        f"timestamp: {self.timestamp}\n" +
        f"transactions: {self.transactions}\n" +
        f"nonce: {self.nonce}\n" +
        f"hash: {self.hash}\n" +
        f"previous hash: {self.previousBlockHash}\n" +
        "}"
        )