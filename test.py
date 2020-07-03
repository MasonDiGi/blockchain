from blockchain import Blockchain

bitcoin = Blockchain()

prevHash = bitcoin.getLastBlock().hash
nonce = bitcoin.proofOfWork(prevHash)
hash = bitcoin.hashBlock(prevHash, nonce)
print(bitcoin.createNewBlock(nonce, prevHash, hash))