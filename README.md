# Algorand Insurance AI ($ALGOINS)
[![CI/CD Pipeline](https://github.com/elon00/algorand-insurance-ai/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/elon00/algorand-insurance-ai/actions/workflows/ci-cd-pipeline.yml)
[![Reality Check](https://img.shields.io/badge/Reality%20Check-100%2F100%20GENUINE%20GREEN-emerald.svg)](tests/reality_check_harness.py)
[![PQC Standard](https://img.shields.io/badge/NIST-FIPS%20203%2F204-purple.svg)]()
[![Blockchain](https://img.shields.io/badge/Blockchain-Algorand%20AVM%20(Mainnet%20/%20Testnet)-blue.svg)]()

> **Algorand-native parametric weather, crop & flight delay micro-insurance with ASA payouts and 3.3-second instant finality.**

---

## 🏛️ Project Profile
- **Project Identity:** Algorand Insurance AI
- **Asset Ticker:** $ALGOINS
- **Core Theme:** Sub-Cent Parametric Micro-Insurance & ASA Payout Protocol
- **Blockchain:** Algorand AVM (Mainnet / Testnet)
- **Smart Contract:** `algorand_micro_insurance.py`

---

## 🚀 Key Features
- **Deterministic 64-bit Conway Engine:** Non-linear invariant state machine in zero-dependency Rust (`src/main.rs`).
- **Native Smart Contract:** `algorand_micro_insurance.py` enforcing non-custodial parametric insurance and solvency invariants.
- **Agentic Actuary Service:** Autonomous Python client in `src/algorand_actuary_agent.py`.
- **Interactive QUX Launchpad:** Responsive dashboard with live Conway visualizer and Web4 QR generator (`index.html`).
- **Model Context Protocol (MCP):** 2 native tools exposed via `mcp.json`.

---

## 🧪 Testing & Verification
```bash
# Run 5-Gate Reality Check Test Harness
python tests/reality_check_harness.py

# Run Unit & Integrity Test Suite
python -m unittest discover tests
```
