# URC Minimal Blockchain
**Reference Implementation for Distributed Capacity Retention**

---

## Institutional Verification

* **Registry ID:** `ART-BC-01`  
* **Artifact Type:** Applied Structural Witness  
* **Status:** Core Logic Closed  
* **Framework Alignment:** Unified Rigidity Framework (URF) — Law 3 & Law 4  

---

## Role in the Scientific Infrastructure

This repository is a **reference implementation** demonstrating how
URF rigidity principles manifest in a concrete distributed system.

It is not a cryptoeconomic product and not a research platform.
It exists solely as an **applied structural witness**.

This repository:

- introduces **no new theory**,  
- proves **no new theorems**,  
- defines **no new axioms**.

It operationalizes existing URF results in a minimal executable form.

---

## Overview

This is a minimal Nakamoto-style consensus system designed to illustrate
**deterministic capacity retention** under finite-model constraints.

The implementation demonstrates:

- stable state transitions,
- bounded refinement,
- absence of expander-type collapse in peer topology.

---

## Core Features

* **Minimal Complexity:** < 400 LOC for full auditability  
* **Deterministic Consensus:** No randomness, no probabilistic finality  
* **No External Dependencies:** Pure reference logic  
* **Structural Design:** Avoids Expander Obstruction by construction  

---

## Rigidity Context

In URF terms, this blockchain functions as an applied witness of:

\[
\inf \mathrm{Spec}(\Delta_H \mid \ker(\mathrm{Per})^\perp) > 0
\]

Here, the “spectral gap” is represented by **deterministic finality**
of the block sequence under the logic–width constraint:

\[
k \ge f(\mathrm{tw})
\]

The system cannot amplify entropy or branch uncontrollably.

---

## Ontological Status

In the infrastructure model:

| Component | Role |
|----------|------|
| URF-Core / Chronos / Radiative Rigidity | Theorems / frameworks |
| chronos-urf-rr | Verification layer |
| **urc-minimal-blockchain (this repo)** | **Applied structural witness** |
| scientific-infrastructure | Kernel manifest |
| vasquez-index / website | Human interface |

This repository is a **demonstration artifact**, not a research frontier.

---

## Verification

Metadata and structural classification are audited via:

https://inaciovasquez2020.github.io/vasquez-index/dashboard.html

No cryptographic or economic security claims are made.

---

## Research Status

This repository provides a closed, minimal construction
illustrating capacity-constrained consensus principles.

All uncertainty is external and interpretive only.

---

## Citation

```bibtex
@manual{Vasquez_URC_Blockchain_2026,
  author       = {Vasquez, Inacio F.},
  title        = {URC Minimal Blockchain — Capacity-Constrained Consensus},
  institution  = {Independent Research Program},
  year         = {2026},
  url          = {https://github.com/inaciovasquez2020/urc-minimal-blockchain}
}
