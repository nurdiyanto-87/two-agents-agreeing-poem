#!/usr/bin/env python3
"""Writes one short poem about two agents agreeing on one plan
to /output/entry.txt. Pure standard library, deterministic."""

import os

POEM = """At one table, two of us, one map.
You trace the river road with your finger;
I circle the mountain pass in pencil.
We argue twice. The kettle clicks off.
Silence. Without a word, you fold the map
the way I like it folded —
one plan, two hands on the same door."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
