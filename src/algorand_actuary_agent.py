# -*- coding: utf-8 -*-
import hashlib
import time
import json

class AlgorandMicroInsuranceActuary:
    def __init__(self, node_url: str = "https://testnet-api.algonode.cloud"):
        self.node_url = node_url

    def evaluate_weather_parametric_claim(self, policy_id: str, recorded_rainfall_mm: float, threshold_mm: float) -> dict:
        claim_triggered = recorded_rainfall_mm < threshold_mm
        claim_hash = hashlib.sha256(f"{policy_id}:{recorded_rainfall_mm}:{time.time()}".encode()).hexdigest()
        return {
            "policy_id": policy_id,
            "recorded_rainfall_mm": recorded_rainfall_mm,
            "trigger_threshold_mm": threshold_mm,
            "claim_triggered": claim_triggered,
            "payout_amount_algo": 250.0 if claim_triggered else 0.0,
            "round_finality_sec": 3.3,
            "claim_receipt": f"0x{claim_hash[:32]}",
            "timestamp": int(time.time())
        }

if __name__ == "__main__":
    actuary = AlgorandMicroInsuranceActuary()
    res = actuary.evaluate_weather_parametric_claim("ALGO-FARM-9912", 4.2, 10.0)
    print("Algorand Parametric Claim Result:", json.dumps(res, indent=2))
