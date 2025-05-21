"""Launcher for TexAdvent games."""

import importlib
import os
import sys

GAME_DIR = os.path.join(os.path.dirname(__file__), "game")


def list_games():
    games = []
    for d in os.listdir(GAME_DIR):
        if d.startswith("__"):
            continue
        path = os.path.join(GAME_DIR, d)
        if os.path.isdir(path):
            games.append(d)
    return games


def run_game(name: str):
    try:
        module = importlib.import_module(f"game.{name}.main")
    except ModuleNotFoundError:
        print(f"Game '{name}' not found.")
        return

    if hasattr(module, "main"):
        module.main()
    else:
        print(f"Game '{name}' does not define a main() function.")


def main(argv: list[str] | None = None):
    argv = argv or sys.argv[1:]
    games = list_games()
    if not games:
        print("No games available.")
        return

    if argv:
        game = argv[0]
    else:
        print("Available games:")
        for i, g in enumerate(games, start=1):
            print(f"  {i}. {g}")
        choice = input("Select a game by name or number: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(games):
                game = games[idx]
            else:
                print("Invalid selection.")
                return
        else:
            game = choice

    run_game(game)


if __name__ == "__main__":
    main()
