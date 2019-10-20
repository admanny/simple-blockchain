import time

from blockchain.block import Block, Transaction


class Blockchain:
    pow_difficulty = 1


    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.create_genesis_block()


    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "-1")
        genesis_block.hash = genesis_block.compute_hash()

        self.chain.append(genesis_block)
    

    def add_block(self, block: Block, proof: str) -> bool:
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_block_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        
        block.hash = proof
        self.chain.append(block)

        return True


    @property
    def last_block(self) -> Block:
        return self.chain[-1]


    def proof_of_work(self, block: Block) -> str:
        block.nonce = 0
        computed_hash = block.compute_hash()

        while not computed_hash.startswith('0' * Blockchain.pow_difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash


    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        return (block_hash.startswith('0' * Blockchain.pow_difficulty) 
            and block_hash == block.compute_hash())


    def add_new_transaction(self, transaction: Transaction):
        self.unconfirmed_transactions.append(transaction)


    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index+1, transactions=self.unconfirmed_transactions,
                            timestamp=time.time(), previous_block_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []

        return new_block.index
