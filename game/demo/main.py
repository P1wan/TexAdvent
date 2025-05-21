"""Entry point for the demo adventure."""

# Allow running directly or via ``python -m``
if __package__ is None:
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from engine import GameEngine, engine


def main():
    start = engine.Location("Demo Room", "This is a placeholder starting room.")
    GameEngine(start).run()


if __name__ == "__main__":
    main()
