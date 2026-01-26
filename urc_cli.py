# urc_cli.py
import requests

import argparse
from urc_chain import Chain, mine_block, genesis_block
from urc_storage import load_chain, save_chain

def broadcast_block(block):
    r = requests.post("http://127.0.0.1:8333/block", json=block, timeout=5)
    print("Broadcast:", r.status_code, r.text)


def cmd_mine(address):
    print("ENTERED MINE COMMAND")
    print("Mining to address:", address)

    # load existing chain or create new
    chain = load_chain()

    # mine exactly one block
    b = mine_block(chain, address)
    print("Mined block", chain.height)
    broadcast_block(b)

    # persist to disk
    save_chain(chain)


def main():
    print("LOADED urc_cli.py")

    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("address")
    args = parser.parse_args()

    print("ARGS:", args)

    if args.command == "mine":
        cmd_mine(args.address)
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()

