# urc_storage.py

import json
from urc_chain import Chain, genesis_block, verify_chain

CHAIN_FILE = "chain.json"

def save_chain(chain: Chain):
    with open(CHAIN_FILE, "w") as f:
        json.dump(chain.blocks, f, indent=2)

def load_chain():
    try:
        with open(CHAIN_FILE, "r") as f:
            blocks = json.load(f)
        chain = Chain(genesis_block())
        chain.blocks = blocks
        if not verify_chain(chain):
            raise Exception("Invalid chain on disk")
        return chain
    except FileNotFoundError:
        return Chain(genesis_block())

