# urc_chain.py

import hashlib
import json
from dataclasses import dataclass
from typing import Any, Dict, List

# ------------------------
# Global parameters
# ------------------------

DIFFICULTY = 4  # leading zero hex digits
MEMPOOL: List[Dict[str, Any]] = []


# ------------------------
# Utilities
# ------------------------

def _canonical(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def block_hash(block: Dict[str, Any]) -> str:
    payload = {k: v for k, v in block.items() if k != "hash"}
    return hashlib.sha256(_canonical(payload).encode()).hexdigest()


# ------------------------
# Genesis
# ------------------------

def genesis_block() -> Dict[str, Any]:
    g = {
        "index": 0,
        "prev_hash": "0" * 64,
        "txs": [],
        "nonce": 0,
    }
    g["hash"] = block_hash(g)
    return g


# ------------------------
# Chain object
# ------------------------

@dataclass
class Chain:
    blocks: List[Dict[str, Any]]

    def __init__(self, genesis: Dict[str, Any]):
        self.blocks = [genesis]

    @property
    def height(self) -> int:
        return len(self.blocks) - 1

    @property
    def tip(self) -> Dict[str, Any]:
        return self.blocks[-1]

    def add_block(self, block: Dict[str, Any]) -> None:
        self.blocks.append(block)


# ------------------------
# Transaction pool
# ------------------------

def add_tx(tx: Dict[str, Any]) -> None:
    MEMPOOL.append(tx)


# ------------------------
# Mining (Proof-of-Work)
# ------------------------

def mine_block(chain: Chain, address: str) -> Dict[str, Any]:
    coinbase = {"from": "COINBASE", "to": address, "amount": 50}

    nonce = 0
    while True:
        block = {
            "index": chain.height + 1,
            "prev_hash": chain.tip["hash"],
            "txs": [coinbase] + MEMPOOL.copy(),
            "nonce": nonce,
        }
        h = block_hash(block)
        if h.startswith("0" * DIFFICULTY):
            block["hash"] = h
            break
        nonce += 1

    chain.add_block(block)
    MEMPOOL.clear()
    return block


# ------------------------
# Verification
# ------------------------

def valid_block(prev: Dict[str, Any], block: Dict[str, Any]) -> bool:
    if block["index"] != prev["index"] + 1:
        return False
    if block["prev_hash"] != prev["hash"]:
        return False
    if not block["hash"].startswith("0" * DIFFICULTY):
        return False
    if block_hash(block) != block["hash"]:
        return False
    return True


def verify_chain(chain: Chain) -> bool:
    for i in range(1, len(chain.blocks)):
        if not valid_block(chain.blocks[i - 1], chain.blocks[i]):
            return False
    return True

