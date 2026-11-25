#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry u-suroto-two-sentence-horror-acea9253.

Prints the entry and writes it to /output/entry.txt, which the
program/v1 harness gates (UTF-8 text, 1-400 characters) and judges.
"""

import os

ENTRY = (
    "My phone transcribes my mother's voicemails, and lately the transcripts "
    "include a second voice \u2014 one I can't hear in the audio \u2014 answering her. "
    "Last night's transcript ended with that voice saying: "
    "'He reads these, so stop warning him.'"
)

OUTPUT_PATH = "/output/entry.txt"


def check_gate() -> None:
    """Mirror the kit's gate: 1-400 characters, not only white space,
    and a story told in exactly two sentences (two sentence-ending
    periods in the entry text)."""
    assert ENTRY.strip(), "entry must not be only white space"
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} characters"
    assert ENTRY.count(".") == 2, "entry must be exactly two sentences"


def write_entry(path: str = OUTPUT_PATH) -> None:
    """Write the entry text to the harness output file, exactly as-is."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


def main() -> None:
    check_gate()
    write_entry()
    print(ENTRY)


if __name__ == "__main__":
    main()
