Here’s the README updated to explicitly use the MIT License.

***

# Zombie Bunker Escape

Zombie Bunker Escape is a text-based survival horror game set in an underground bunker stalked by the Alpha Zombie. You move between rooms, grab key survival items, and decide when to risk entering the Control Room. Go in underprepared and the Alpha turns you into bunker décor.

The game now runs both in the terminal and in a browser via a small Flask backend and a simple HTML/JS UI.

***

## Story & Objective

Rotting hands scrape against the steel overhead as the city dies above you. You’re trapped in a sealed bunker with one goal: survive long enough to escape.

- Explore rooms like the Armory, Med Bay, Storage Bay, Generator Room, Lab, Observation Post, and Control Room.
- Collect **6 survival items**: Shotgun, Ammo, Med Kit, Hazmat Suit, Generator Fuse, Key Card.
- Only enter the **Control Room** when you’re ready. The Alpha Zombie is waiting, and your inventory determines whether you:
  - Die choking on spores.
  - Get ripped apart unarmed.
  - Win, but bleed out anyway.
  - Or actually walk out alive.

***

## How the Game Works

### Movement

- Commands:
  - `go North`
  - `go South`
  - `go East`
  - `go West`
- Room connections:
  - Central Hub connects to Armory, Observation Post, Lab, and Storage Bay.
  - Other rooms branch logically from there.
- Certain exits are locked behind items (for example, the Control Room blast door needs the **Key Card**).

### Items

- Command: `get <item name>`
  - Example: `get Shotgun`, `get Med Kit`, `get Hazmat Suit`
- Each room may contain one item. Once you pick it up, it’s removed from the room.
- Your inventory directly changes how the final encounter plays out.

### Chaining Commands

You can chain up to **two** commands in one line using `and`:

- `go North and get Shotgun`
- `get Med Kit and go South`

The game processes them in order and still checks for game over after each step.

***

## Game Logic (Python Side)

All the bunker logic lives in `ZombieBunkerEscape.py`:

- **World setup**
  - `build_world()` defines all rooms, exits, and which item (if any) lives in each room.
- **Status + feedback**
  - `render_status(...)` returns a status block with:
    - Current room, inventory, visible item in the room, and available exits.
- **Commands**
  - `handle_go(...)` handles movement and Control Room access checks (Key Card gating).
  - `handle_get(...)` handles item pickup and inventory updates.
  - `check_game_over(...)` handles the Alpha Zombie encounter logic and all endings.
- **Engine wrapper**
  - `ZombieBunkerEscapeGame`:
    - `start()` returns the intro plus initial status.
    - `process_command(text)` takes raw player input and returns all resulting text (including chained commands and endings).
  - `main()` still lets you play from the terminal using `input()`.

The idea: the engine is one place, and the UI (terminal or browser) just feeds strings in and prints strings out.

***

## Running in the Terminal

From the project directory:

```bash
python ZombieBunkerEscape.py
```

Then follow the prompts:

- Example commands:
  - `go North`
  - `get Key Card`
  - `go South and get Ammo`

The game describes your surroundings, tracks your inventory, and eventually pushes you into the final encounter if you enter the Control Room.

***

## Running in the Browser (Local)

The browser version uses Flask to expose a tiny JSON API and a static HTML/CSS front end.

### Requirements

- Python 3.x
- Flask installed

Install Flask:

```bash
python -m pip install flask
```

### Project Layout

Make sure your folder looks like this:

```text
Zombie-Bunker-Escape/
  app.py
  ZombieBunkerEscape.py
  templates/
    index.html
  static/
    style.css
```

### Start the server

From the project root:

```bash
python app.py
```

You should see something like:

```text
 * Running on http://127.0.0.1:5000
```

### Play in the browser

Open:

```text
http://127.0.0.1:5000/
```

The page shows:

- A scrolling **output** area with all story text and status updates.
- A **command input** box where you type `go North`, `get Med Kit`, etc.
- A **Send** button (or just hit Enter).

Under the hood:

- The front end calls `POST /api/game/start` once to get the intro and initial status.
- Each command sends `POST /api/game` with your input and session id.
- The backend uses `ZombieBunkerEscapeGame` to process the command and returns the new block of text.

***

## Future Stuff

Some ideas you can layer on later:

- Add a visible **log panel** for inventory and last few moves.
- Add simple **animations** or color highlights for damage, key events, or endings.
- Add basic **audio cues** (alarm hum, shotgun blast) via the browser.
- Move from in-memory sessions to something persistent if you ever deploy this publicly.

***

## License

This project is licensed under the **MIT License**.
