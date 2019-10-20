from fastapi import APIRouter, Body
from blockchain.blockchain import Blockchain
from blockchain.block import Transaction

import json


route = APIRouter()
blockchain = Blockchain()


@route.get('/chain/blocks')
async def get_chain_blocks():
    chain_data = []

    for block in blockchain.chain:
        chain_data.append(block.__dict__)

    response = {
        "blockchain_length": len(chain_data),
        "blockchain_data": chain_data
    }

    return response


@route.get('/chain/mine')
async def mine():
    blockchain.mine()

    last_block = blockchain.last_block

    response = {
        "message": "New Block has been created!",
        "block_index": last_block.index,
        "block_hash": last_block.hash,
        "block_transactions": last_block.transactions,
        "previous_block_hash": last_block.previous_block_hash
    }

    return response


@route.post('/transaction/add', status_code=201)
async def add_transaction(payload = Body(...)):
    transaction = Transaction(**payload)
    blockchain.add_new_transaction(transaction)
