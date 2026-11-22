#!/usr/bin/env python3
"""Write the plan text to /output/entry.txt.

Stdlib only, no network, deterministic: the same bytes every run.
"""

import os

PLAN = (
    "Day 1: email 300 SaaS founders from Apollo, offering 3 free sales "
    "meetings each. Send via Instantly, book via Calendly. Charge $60 per "
    "meeting held, $1,500 a month per client. One customer is worth "
    "thousands to a founder, so they keep paying. You sell meetings, "
    "not hours."
)


def main() -> None:
    # The gate: 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(PLAN) <= 280 and PLAN.strip(), "plan fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
