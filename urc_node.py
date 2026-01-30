from urc_chain import Blockchain
from urc_storage import load_chain, save_chain

class Node:
    def __init__(self, address):
        self.address = address
        self.chain = load_chain(address)

    def start(self):
        print(f"Node running at {self.address}")

    def mine(self):
        block = self.chain.add_block("dummy transaction")
        save_chain(self.address, self.chain)
        print("New block added:", block)

    def show_chain(self):
        for block in self.chain.chain:
            print(block)

