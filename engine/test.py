"""Manual test area for engine components."""

# Allow running this file directly or via ``python -m engine.test``
if __package__ is None:
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from engine import GameEngine, Parser
from engine import engine as engine_mod


def simple_test():
    loc = engine_mod.Location("Test Room", "A room used for testing.")
    game = GameEngine(loc)
    game.run()
    parser = Parser()
    print(parser.parse("look around"))

if __name__ == "__main__":
    # Running this file will execute the simple test
    simple_test()
