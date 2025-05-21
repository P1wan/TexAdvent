# TexAdvent

A simple framework to structure text-based adventure games in Python.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Features](#features)
- [Project Structure](#project-structure)
- [Extending the Framework](#extending-the-framework)
- [Example Game](#example-game)
- [Contributing](#contributing)
- [License](#license)
- [Roadmap](#roadmap)

## Overview

TexAdvent aims to provide a lightweight set of classes and utilities for creating interactive fiction. The documentation in [`docs/DevelopmentStructureSuggestion.md`](docs/DevelopmentStructureSuggestion.md) outlines a minimal parser, objects for rooms, items and NPCs, and tips for clean separation between the engine and game data. [`docs/BasicIdeas.md`](docs/BasicIdeas.md) contains early brainstorming notes. Those notes are not finalized but serve as inspiration for future expansion.

## Getting Started

1. **Requirements**
   - Python 3.11 or later
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Demo**
   ```bash
   python -m game.demo
   ```
   *(Demo game not yet implemented)*

## Features

- Rooms and connections to represent the game world
- Player state with location and inventory
- Movement commands with optional synonyms
- Basic `look` and item interaction
- Simple inventory management (`take`, `drop`, `inventory`)
- Minimal dialogue system for NPCs
- Parser with synonym and fuzzy matching support

## Project Structure

```
engine/   # core classes and parser
game/     # example adventure using the engine
```

## Extending the Framework

1. Create new `Location` objects and link them via exits.
2. Define `Item` and `NPC` instances with descriptions.
3. Add synonyms to the parser maps to expand understood vocabulary.

## Example Game

A small demo adventure will be included to showcase usage.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests. The project uses the permissive MIT license to encourage community participation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Roadmap

Ideas for future development are tracked in the documentation. See the "Stretch Goals / Future Expansion" section in [`docs/DevelopmentStructureSuggestion.md`](docs/DevelopmentStructureSuggestion.md).

