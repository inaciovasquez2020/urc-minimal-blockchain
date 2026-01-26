# urc_node.py

import os
import requests
from flask import Flask, request, jsonify

from urc_storage import load_chain, save_chain
from urc_chain import verify_chain, Chain, genesis_block

app = Flask(__name__)
chain = load_chain()

PORT = int(os.environ.get("URC_PORT", "8333"))
PEER = os.environ.get("URC_PEER", "")  # e.g. http://127.0.0.1:8334


def chain_work(blocks):
    w = 0
    for b in blocks[1:]:
        if (
            isinstance(b.get("hash"), str)
            and b["hash"].startswith("0" * 4)
        ):
            w += 1
    return w


def adopt_if_better(remote_blocks):
    global chain

    candidate = Chain(genesis_block())
    candidate.blocks = remote_blocks
    if not verify_chain(candidate):
        return False

    if chain_work(remote_blocks) > chain_work(chain.blocks):
        chain.blocks = remote_blocks
        save_chain(chain)
        return True

    return False


@app.route("/block", methods=["POST"])
def receive_block():
    block = request.json
    chain.blocks.append(block)
    if not verify_chain(chain):
        chain.blocks.pop()
        return jsonify({"status": "rejected"}), 400
    save_chain(chain)
    return jsonify({"status": "accepted"})


@app.route("/chain")
def get_chain():
    return jsonify(chain.blocks)


@app.route("/sync")
def sync():
    if not PEER:
        return jsonify({"status": "no_peer_configured"}), 400
    r = requests.get(f"{PEER}/chain", timeout=5)
    ok = adopt_if_better(r.json())
    return jsonify({"status": "adopted" if ok else "kept"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=PORT)

