import json
from hashlib import sha256
from typing import List


class Block:
    hash = None
    
    def __init__(self, index, transactions: List, timestamp, previous_block_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_block_hash = previous_block_hash
        self.nonce = nonce


    def compute_hash(self):
        block_str = json.dumps(self.__dict__, sort_keys=True)
        
        return sha256(block_str.encode()).hexdigest()


class Transaction(dict):
    def __init__(self, sender: str, recipient: str, amount: int):
        dict.__init__(self, 
            sender=sender, 
            recipient=recipient, 
            amount=amount
        )
        