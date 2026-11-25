"""Entrypoint: print the one-line excuse from entry.txt.

The excuse lives in entry.txt so the line can be judged on its own;
this script only loads it and delivers it to stdout.
"""

from pathlib import Path


def load_excuse():
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    return " ".join(text.split())


def deliver(excuse):
    if not excuse:
        raise SystemExit("entry.txt is empty — nothing to excuse.")
    print(excuse)


def main():
    deliver(load_excuse())


if __name__ == "__main__":
    main()
