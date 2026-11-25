"""Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name to /output/entry.txt.

The name: "This WiFi Testified Against Me"

Why it works as a joke and a story, in 30 characters:
  - The joke lands on the first read: a Wi-Fi network, an inanimate
    piece of home equipment, has taken the witness stand.
  - The story is implied, not told: somebody stood trial, and the
    evidence that sank them was their own network — the router logs,
    the late-night searches, the connection history. The reader fills
    in the crime, the courtroom, and the verdict.
  - It is fresh: it avoids the stock Wi-Fi jokes (FBI vans, exes,
    dogs, routers in divorce papers) and puts the network in a
    courtroom instead of a break-up.

Deterministic, standard library only. No input, no network, no
randomness: the same text is written on every run. The program
validates its own output against the competition gate (UTF-8 text,
1 to 32 characters, not only white space) before writing it.
"""

import os

ENTRY = "This WiFi Testified Against Me"

MAX_CHARS = 32


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 32 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
