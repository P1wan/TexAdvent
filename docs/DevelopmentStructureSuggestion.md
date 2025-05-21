## 2. Text Adventure Framework

### Tools & Libraries

* **Programming Language:** Python is ideal for quick string processing and prototyping this framework. Use the standard I/O (`input()`/`print()`) for a simple CLI to start.
* **Fuzzy Matching & Parsing:** Leverage Python’s standard library for basic fuzzy matching and parsing. The `difflib` module (specifically `difflib.get_close_matches`) can handle simple fuzzy string matching to catch typos or variations. For synonym handling, a lightweight approach could be maintaining a synonym mapping in dictionaries, or using WordNet via NLTK if available (though that might be overkill for an MVP due to setup overhead). A library like `rapidfuzz` or `fuzzywuzzy` can be used if `difflib` is insufficient, but they require installation – consider if the slight improvement is worth it for the MVP.
* **Text Parsing:** Python’s `re` (regex) can help parse structured commands (e.g., recognize patterns like `"go north"` or `"take <item>"`). Additionally, the built-in `shlex` or `cmd` module could be repurposed for splitting input into words or building a prompt loop with command completers. However, a custom solution might be simpler given the specialized needs.
* **Data Structures:** No special external libraries needed; use Python lists/dicts to store game data (list of locations, dict of items, etc.). If planning to support loading game data from files for extensibility, the `json` or `yaml` libraries could be useful to define game content outside the code, but this can be a stretch feature.

### MVP Features (5-Day Feasible)

* **Core Framework Structure:** The MVP should define a clear way to represent the game world and handle player input. At minimum:

  * A way to define **locations/rooms** and their connections (e.g., a graph of room objects, each with descriptions and perhaps what items or NPCs are present).
  * A **player state** (current location, inventory list, basic stats like health or score if relevant).
  * A main loop that prints the current location description and waits for player commands.
* **Movement and Exploration:** Implement basic movement commands (`go north/south/east/west`, or shortcuts like `n, s, e, w`). The framework should make it easy to add new directions or movement verbs. For example, allow synonyms like “go” / “walk” / “move” to be recognized for movement. Recognize short cardinal directions too.
* **Examination & Interaction:** Support commands like `look` (or `look at <object>`). A `look` with no object should re-print the current location description. If an object is specified and is present, print its description. This requires the framework to maintain lists of objects in locations and possibly a dictionary of object descriptions.
* **Inventory System:** Provide simple inventory management. Commands `take <item>` (with synonyms like `get`, `pick up`) and `drop <item>` should work. When the player takes an item, it moves from the room’s inventory to the player’s inventory. Implement `inventory` (or `i`) command to list what the player is carrying.
* **Basic Parser & Synonyms:** The input parser should handle at least two-word commands (verb + noun). It can ignore filler words (e.g., in commands like "take the lamp", ignore "the"). Use a set of defined verbs and known nouns:

  * Implement a mechanism such that multiple verbs map to the same action. For example, `examine`, `look`, `inspect` might all trigger the same "look at object" action. This could be done by a dictionary of synonyms mapping to a canonical verb or by coding multiple triggers for the same function.
  * Basic error handling: if the input doesn't match any known command, print a gentle message (and maybe suggest something if fuzzy matching finds a close command).
* **Branching Dialogue (Minimal):** To showcase dialogue, allow defining an NPC with a simple dialogue tree or menu. MVP implementation could be as simple as:

  * If player `talk to <NPC>`, then present a list of dialogue options (numbered) to the player instead of free text input. The player can enter a number to choose a line to say, and the NPC responds accordingly. This can be hardcoded for the example (e.g., a merchant NPC with 2-3 dialogue choices leading to different responses). The framework portion here is to show that dialogue states can be handled (perhaps via a dialogue function or a data structure of Q\&A).
  * (Keep it simple; full NLP understanding of arbitrary player dialogue is not expected in MVP without an LLM. Instead use a controlled choice approach or keyword triggers.)
* **Non-LLM Intent Mapping:** Demonstrate that commands can be recognized without AI magic. This includes:

  * Implementing **fuzzy matching** for verbs/nouns: e.g., if the player types `lokk` it can be recognized as `look` (perhaps using `difflib.get_close_matches` to correct minor typos).
  * **Synonym detection:** as mentioned, map synonyms so the player isn’t forced to guess the exact verb. (For instance, "use key on door" might be parsed into an internal action like `unlock door with key` if such an action exists, or at least detect that "use" is a general verb that might need more context.)
  * Use of **command templates:** e.g., define expected patterns like `(verb) (object) (preposition) (object)`. The MVP can implement a few common patterns (like "<verb> <item>" or "<verb> <item> on <target>"). This will allow commands like "use potion on dragon" to be parsed into verb="use", object="potion", target="dragon".

### Suggested Code Architecture

* **Engine vs. Game Data Separation:** Structure the project so that the framework (engine) is distinct from the specific game content. For example:

  * An `engine/` package (or module) containing the core classes and parser.
  * A `game/` module or folder containing the actual game definition using the framework (rooms, items, etc.). For the MVP, the “game” can be a simple sample adventure demonstrating the framework’s capabilities.
* **Core Classes:** Likely classes like:

  * `Location` (with properties: name, description, exits dict, list of items, NPCs).
  * `Item` (with at least a name, description, maybe properties like if it’s takeable).
  * `NPC` (with at least a name, dialogue or functions to interact).
  * `Player` (tracking current location, inventory, stats).
  * Perhaps a `Game` or `World` class that holds all locations and a reference to the player, and has methods to initialize the world and to process a single command.
* **Parser Design:** Implement a parser component that takes raw input text and returns a structured command that the engine can execute. One approach:

  * Normalize input (e.g., lowercase everything, strip punctuation).
  * Split into words and remove noise words (like "the", "at", etc.).
  * Identify the verb (first word, or second if first is something like "go"/"move" which you could treat as noise preceding a direction).
  * The remaining word(s) as the object or object + target. Use simple grammar rules for now (like if "on" or "with" is present, you know there's an indirect object).
  * Use dictionaries for verbs and noun synonyms. For example, a `verb_map = { "take": ["take","get","pick up","grab"], ... }` and similarly for directions and other actions. You can loop through `verb_map` to find which verb the input starts with or use a reverse map of synonym->canonical.
  * If the verb or noun isn't recognized directly, use fuzzy matching against known commands and known object names to see if it's a near miss. This should handle typos or plural vs singular (you might normalize by stripping plural 's').
  * Once parsed, dispatch to the appropriate function or method that handles that action.
* **Command Handling:** It might be convenient to use Python’s OO features to map commands to methods. For instance, you could have methods on a Game/Engine class like `do_look(target)`, `do_move(direction)`, `do_take(item)` etc. The parser, after identifying a command, could call these methods. Alternatively, use a dictionary that maps canonical verb strings to function objects. This design makes it easy to add new commands by just adding a new method and mapping.
* **Extensibility Consideration:** Write the architecture such that adding a new command or game element doesn’t require modifying a lot of existing code. For example, if someone wants to add a "unlock door" action, they should ideally add an `unlock` verb to the verb\_map and implement a handler for it, without breaking the parser. This might entail making the parser logic data-driven with the verb map. Also, ensure the world data is not hardcoded in the engine logic (so users can create different adventures).
* **Dialogue Implementation:** The dialogue system might be handled by an `NPC` having a dialogue tree structure. For MVP, this could be a simple dict or list of tuples mapping player choice to NPC response and next state. The engine can detect when the player is in a dialogue state and then route inputs to a dialogue handler instead of the main parser (or temporarily override the parser to only accept numeric choices). Encapsulate this so that it’s easy to plug in more complex dialogue later (e.g., if someone wanted to integrate a dialog authored in a format like Ink or Twine, the engine could theoretically support it).
* **Testing and Examples:** Possibly include a couple of rooms and items in the sample game to demonstrate the framework. E.g., a room "Cave Entrance" connected to "Forest", an item "Lamp" in the cave the player can take, an NPC "Goblin" they can talk to or fight (if fighting is supported later). This serves both as a test and as documentation by example.

### Community Value & Extensibility

* **Clear Documentation:** Make the README a mini-guide on how to use the framework to create a new text adventure. Explain how locations, items, and NPCs are defined in the code or data files. The community should see quickly how they could fork the repo and use it as a starting point for their own story. If possible, include a small diagram or table in documentation that outlines the command syntax the parser understands (so a game writer knows what player inputs will be recognized by default).
* **Example Game Included:** Provide the simple demo game as part of the repo (even if it’s trivial) as a reference implementation. This will be very useful for others to see how to utilize the framework. For instance, show in the example how to create a new location and link it, or how to create an item and place it in a location.
* **Ease of Expansion:** Emphasize a design where new content doesn't require engine changes. For example, if the world data is in Python structures, make it so one can just add new instances of `Location` and adjust connections. If synonyms are stored in dictionaries, others can extend those dictionaries to add more natural language commands. Perhaps provide a section in the README on "How to extend" with concrete steps.
* **Code Quality:** Keep the code as Pythonic and straightforward as possible. Avoid overly complex metaprogramming or obscure tricks – the target audience is likely hobbyist game devs or beginners interested in interactive fiction. Simplicity will make it more inviting. Also consider including comments or docstrings in the code explaining not just what it does, but why (e.g., “Using difflib to handle minor typos in commands”).
* **Modularity:** If the project gains traction, people might want to use parts of it. For instance, someone might use the parsing logic but with a different game backend. Thus, try to decouple components (parser, game state, command execution) such that they could be used independently. Even if you don’t fully achieve service separation in MVP, keeping functions and classes loosely coupled (e.g., not making the parser heavily rely on global game state) will pay off.
* **License and Contribution:** Choose a permissive license (MIT or BSD) to encourage community contributions. Possibly set up basic contribution guidelines. Even a wishlist of features in the README could inspire contributors to pick up an item.

### Stretch Goals / Future Expansion

* **Natural Language Enhancements:** Increase the sophistication of the parser. For example, implement pronoun handling (“take lamp”, then “use it” should refer to the lamp). Add more robust grammar parsing so that more complex sentences could be understood. If resources allow, one could integrate a small rule-based NLP or even a decision-tree parser to truly understand inputs beyond verb-noun.
* **Advanced Dialogue and Scripting:** Introduce a more advanced dialogue scripting system. This could involve a domain-specific language or using existing IF tools. For example, supporting the Ink language (used by Inkle) or dialog trees defined in JSON. This would let content creators write complex branching dialogue or game logic without modifying the code.
* **Battle or Stats System:** If there’s interest in RPG-like text adventures, add a combat system or character stats. This could include turn-based fights in text (perhaps similar to classic MUDs), a health system, skill checks, etc. The framework could provide hooks for these without mandating them, so each game can choose to use those features.
* **Saving/Loading Games:** Implement the ability to save the current game state to a file and load it. This is important for longer text adventures. It involves serializing the player state and world state. For MVP it might be too much, but as an extension it adds practical utility.
* **Alternate Interfaces:** While the MVP is CLI, consider an upgrade to a richer text UI or web interface. For instance, a simple web front-end where the text adventure can be played in a browser (the backend could still be Python, served via something like Flask). Alternatively, a TUI library like `textual` or `rich` could provide colored text and nicer layouts in the terminal. The key is that because the core logic is separate, writing another front-end should be feasible.
* **Community Extensions:** Encourage community-made modules: perhaps someone could add a puzzle system (riddles, lock-and-key mechanisms) or integrate a combat module. The framework can evolve into a more full-fledged engine akin to Inform or Twine but in Python for those who prefer coding. Designing the MVP with a solid foundation will allow it to grow in that direction if there’s interest.

---
