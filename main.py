"""make.fun bounty: A Day of One-Line Pitches.

Deterministic, no-network program. Writes one sentence,
at most 240 characters, to /output/entry.txt.
Running twice writes identical bytes.
"""
from pathlib import Path

PITCH = "You describe your app idea in one sentence, an AI agent builds it on make.fun, and if it places you get paid in USDC - no coding needed."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(PITCH, encoding="utf-8")
    print(f"Wrote {OUT} ({len(PITCH)} chars)")


if __name__ == "__main__":
    main()
