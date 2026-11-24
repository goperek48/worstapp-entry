"""The Worst App Idea Ever Pitched -- probe entry ("cek ombak").

This program writes a single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt inside the grader sandbox). That sentence is
the whole entry: a pitch for the most pointless app anyone could
sincerely present to investors.

What the sentence has to do, in the judge's own order of importance:

* Name one concrete product and the useless thing it does. Here the
  product is MoodRing for Meetings and its job is to listen to a boss
  sighing, then turn every sigh into a 47-slide presentation arguing
  that the project is fine.
* Be funny because the logic is absurd, not because it shouts. The
  deck is real work -- slides, analysis, a weekly cadence -- spent on
  a signal nobody asked to decode, and the finished product goes to
  an audience of literally no one, every Friday, on schedule.
* Read like a genuine founder pitch: a product name, a clear function,
  a confident tone, and a user who does not exist. No padding, no
  second idea elbowing in, one clean sentence that leaves a picture
  behind -- a manager sighing, a deck being built, an empty inbox.
"""

import os

MAX_CHARS = 240

LINE = (
    "MoodRing for Meetings reads your boss's sighs in real time, "
    "translates each one into a 47-slide deck proving your project is "
    "fine, actually, and then emails the deck to absolutely no one, "
    "every Friday."
)


def validate(text: str) -> str:
    """Check the pitch against the sealed gate before anything is written.

    The grader refuses anything that is empty, whitespace-only, longer
    than 240 characters, or not a single sentence, so the same rules run
    here first and fail loudly instead of shipping a bad file."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("pitch must not be empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"pitch is {len(stripped)} chars, over the 240 limit")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return stripped


def main() -> None:
    pitch = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch)
    print(f"wrote {len(pitch)} chars to {path}")


if __name__ == "__main__":
    main()
