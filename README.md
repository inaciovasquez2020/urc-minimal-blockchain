# URC – Minimal Nakamoto Consensus Implementation

This repository contains a minimal, from-scratch implementation of a
distributed proof-of-work blockchain with:

- cryptographic hash linking
- proof-of-work mining
- persistent chain storage
- HTTP peer-to-peer propagation
- chain verification
- cumulative-work fork resolution

The goal is educational: demonstrate the full Nakamoto consensus
mechanism in a compact, readable Python implementation.

## Running

Start two nodes.

Terminal A:
URC_PORT=8333 URC_PEER=http://127.0.0.1:8334 python3 urc_node.py

Terminal B:
URC_PORT=8334 URC_PEER=http://127.0.0.1:8333 python3 urc_node.py

Mine:
python3 urc_cli.py mine TEST

Sync:
curl http://127.0.0.1:8334/sync

