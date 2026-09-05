from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONST = json.loads((ROOT / "constants" / "target.json").read_text())

def test_si_identity() -> None:
    n_per_w = CONST["F_over_P"]["value_N_per_W"]
    un_per_kw = CONST["F_over_P"]["value_uN_per_kW"]
    converted = un_per_kw * 1e-9
    assert abs(converted - n_per_w) < 1e-20
    assert CONST["claim_level"] == 0
    assert CONST["experimental_validation"] is False
    assert CONST["kind"] == "design_goal"

if __name__ == "__main__":
    test_si_identity()
    print("ok: 30 uN/kW == 3e-8 N/W; claim_level=0")
