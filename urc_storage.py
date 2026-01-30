import pickle
import os
from urc_chain import Blockchain

def _filename(address):
    safe = address.replace(":", "_")
    return f"chain_{safe}.dat"

def load_chain(address):
    fname = _filename(address)
    if os.path.exists(fname):
        with open(fname, "rb") as f:
            return pickle.load(f)
    else:
        return Blockchain()

def save_chain(address, chain):
    fname = _filename(address)
    with open(fname, "wb") as f:
        pickle.dump(chain, f)

