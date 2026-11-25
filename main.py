#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line to /output/entry.txt: the excuse a dog gives after
being caught eating the homework, in the dog's own voice.

The line: the homework itself told the dog to "show your work", so the
dog did exactly that -- with its teeth. No guilt, no apology, just a
dog that believes it followed instructions perfectly.
"""

import os

ENTRY = "It said 'show your work,' so I did. I showed it my teeth."


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
