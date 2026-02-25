# Zombie Bunker Escape (Text-Based)

Zombie Bunker Escape is a Python text-based survival-horror adventure set in an underground research facility overrun by zombies.  
You explore interconnected rooms, manage a small inventory, use keycards and codes to unlock critical areas, interact with terminals, and try to reach safety before the bunker becomes your tomb.

This project is designed both as a playable experience and as an example of structured, modular Python game architecture.

***

## Features

- **Text-based exploration**  
  - Navigate a network of bunker rooms using simple text commands.  
  - Each area includes descriptive flavor text and unique interactions.

- **Inventory and items**  
  - Pick up and use items such as keycards and notes.  
  - Inventory is checked at key decision points to unlock or block progress.  

- **Keycard and code-locked doors**  
  - Certain paths and rooms remain inaccessible until you find the correct keycard or discover the required access code.  
  - Encourages exploration and backtracking when new items are found.

- **Terminal interactions**  
  - Access in-game terminals to read logs, uncover story details, and retrieve useful clues like door codes.  
  - Terminals add world-building and light puzzle elements.

- **Branching outcomes and fail states**  
  - Multiple ways to lose (e.g., poor choices, entering unsafe areas unprepared, ignoring clues).  
  - Emphasis on learning from previous runs and making better decisions.

- **Structured game loop**  
  - Clear separation between input handling, game state updates, and output to the player.  
  - Logic organized into functions for rooms, actions, and checks, making the code easier to follow and extend.

***

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/zombie-bunker-escape.git
   cd zombie-bunker-escape
   ```

2. **Ensure Python is installed**  
   - Requires Python 3.x  
   - Check your version with:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```

3. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

There are no external dependencies; the game uses only the Python standard library.

***

## How to Play

1. **Run the game**
   ```bash
   python ZombieBunkerEscape.py
   ```
   or
   ```bash
   python3 ZombieBunkerEscape.py
   ```

2. **Read the opening description**  
   - The game introduces the scenario and your initial location in the bunker.  
   - Pay attention to details; hints for codes and safe routes may appear in the text.

3. **Enter commands**  
   Typical commands (examples, adapt to your actual implementation):
   - Movement: `go north`, `go south`, `go east`, `go west`
   - Interactions: `inspect`, `use terminal`, `read note`
   - Inventory: `inventory`, `use keycard`, `use <item>`
   - Context-specific actions: prompted by the game in certain rooms

4. **Survive and escape**  
   - Explore rooms, collect items, and unlock restricted areas.  
   - Use terminals, notes, and environmental descriptions to deduce door codes and safe paths.  
   - Make careful choices; rushing into the wrong room or ignoring clues can end the run.

***

## Code Structure

- **`ZombieBunkerEscape.py`**  
  Contains:
  - Main game loop  
  - Room functions / handlers  
  - Inventory management logic  
  - Decision branches and fail states  
  - Utility functions for printing text and processing input

Key design ideas:
- **Modular functions** for rooms and events to keep logic localized.
- **Centralized state** (player location, inventory, flags) passed or referenced by these functions.
- **Clear separation** between narrative text and game logic, making it easier to tweak story elements or refactor logic later.

***

## Future Improvements

Planned and potential enhancements:

### Gameplay and Mechanics
- **More complex puzzles**
  - Multi-step puzzles requiring combining clues from different rooms.  
  - Timed sequences where you must complete actions within a limited number of moves.

- **Enhanced inventory system**
  - Item descriptions and examination (`inspect <item>`).  
  - Consumable items (medkits, temporary buffs, etc.).

- **Multiple endings**
  - Different escape outcomes based on choices, items collected, or routes taken.  
  - “Bad”, “neutral”, and “good” endings that encourage replayability.

### World and Narrative
- **Expanded bunker layout**
  - Additional rooms and sectors (labs, armory, ventilation shafts, maintenance levels).  
  - Optional side areas with lore and extra rewards.

- **Deeper story integration**
  - More logs, notes, and terminal messages that reveal what happened in the facility.  
  - Branching narrative nodes that reflect major player decisions.

### Technical Enhancements
- **Better input parsing**
  - More flexible command handling (e.g., supporting synonyms, ignoring minor typos).  
  - Command help system (`help` / `commands`) that lists available actions.

- **Refactored architecture**
  - Move room definitions and data to JSON/YAML or Python data structures for easier content editing.  
  - Introduce a small engine-like framework for reusable text-based games.

- **Save/load system**
  - Ability to save progress to a file and resume later.  
  - Multiple save slots or checkpoints at key story beats.

### Quality of Life
- **Configurable difficulty**
  - Easy/normal/hard modes affecting available hints, number of safe mistakes, or visibility of clues.  

- **Improved text UX**
  - Optional “slow type” effect toggle.  
  - Clearer formatting for important clues and item names.

***

## Contributing

Contributions, suggestions, and bug reports are welcome.  
Possible ways to help:

- Report bugs or confusing sections of the game.
- Propose or implement new rooms, puzzles, and endings.
- Refactor parts of the codebase for clarity, modularity, or testability.

***

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
