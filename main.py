"""make.fun entry: The Meeting That Should Have Been an Email.

Running this script produces the one-line entry at /output/entry.txt.
It only uses the Python standard library and reads nothing from disk
or the network; the joke itself lives in the source below.
"""

from pathlib import Path

OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200

JOKE = (
    "This meeting could have been an email, "
    "but then who would have watched me read that email "
    "out loud for 45 minutes?"
)


def describe(line: str) -> str:
    """Short summary of the entry for the run log."""
    return (
        f"{len(line)} chars, {len(line.encode('utf-8'))} bytes, "
        f"{len(line.split())} words, one line"
    )


def check_entry(line: str) -> None:
    """Raise unless the line satisfies the competition's gate."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("entry is blank")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(f"entry is {len(cleaned)} chars, over the {MAX_CHARS} limit")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    check_entry(JOKE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")
    print(f"wrote {describe(JOKE)} to {OUTPUT}")


if __name__ == "__main__":
    main()
