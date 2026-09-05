<div align="center">

# Thrust Target · 30 μN/kW

### A **design goal** so scaling talks share one number — not a measured device

[![RESEARCH](https://img.shields.io/badge/design_goal-claim_0-f59e0b?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)

</div>

---

## Why this exists

Without a fixed benchmark, every draft invents a new “interesting” F/P.
This repo freezes the **historical engineering target** used in Coherence Drive scaling discussions:

$$
\frac{F}{P} = 3\times 10^{-8}\,\mathrm{N/W} = 30\,\mu\mathrm{N/kW}
$$

Machine-readable copy: [`constants/target.json`](constants/target.json).

## Why you need it

| Use | Don’t use |
|-----|-----------|
| Compare *predictions* after Stage-2 numerics | Fit coupling so the model “hits” 30 μN/kW |
| Keep papers/scripts on the same yardstick | Claim a thruster was built |

**Parameter provenance rule:** if the coupling is chosen only to reproduce this target, you do **not** have a prediction.

## How it works

There is no solver here. This is a **constants / intent** repository:

1. State the target.
2. Point upstream for math and phenomenology.
3. Stay claim level 0 until experiment says otherwise.
4. CI only checks SI unit identity (`tests/test_unit_identity.py`). Green CI is not physics validation.

See [GOVERNANCE.md](GOVERNANCE.md) and [CLAIM_STATUS.md](CLAIM_STATUS.md).

## Upstream

- [ware-constant-phenomenology](https://github.com/beyond-repair/ware-constant-phenomenology)
- [coherence-drive](https://github.com/beyond-repair/coherence-drive)
- [CFTv3.3-IQG-Unified-Framework](https://github.com/beyond-repair/CFTv3.3-IQG-Unified-Framework)
- [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)
