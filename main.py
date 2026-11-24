import os

# The One-Line Laugh — entry line (<=200 chars), written to /output/entry.txt.
ENTRY = "I bought a phone charger for every room, so now there's never one in the room I'm in."


def build_line():
    """Return the single entry line the judge reads."""
    return ENTRY


def write_entry(path="/output/entry.txt"):
    line = build_line()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path, len(line)


if __name__ == "__main__":
    path, n = write_entry()
    print(f"wrote {n} chars to {path}")