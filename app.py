from flask import Flask, request, jsonify, render_template
from ZombieBunkerEscape import ZombieBunkerEscapeGame

app = Flask(__name__)

# super simple in-memory session store
sessions = {}


def get_game(session_id: str) -> ZombieBunkerEscapeGame:
    game = sessions.get(session_id)
    if game is None:
        game = ZombieBunkerEscapeGame()
        sessions[session_id] = game
    return game


@app.route("/")
def index():
    # serve index.html from ./templates
    return render_template("index.html")


@app.route("/api/game/start", methods=["POST"])
def api_start():
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id", "default")

    game = ZombieBunkerEscapeGame()
    sessions[session_id] = game
    text = game.start()

    return jsonify(
        {
            "output": text,
            "session_id": session_id,
        }
    )


@app.route("/api/game", methods=["POST"])
def api_game():
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id", "default")
    command = data.get("command", "")

    game = get_game(session_id)
    text = game.process_command(command)

    return jsonify(
        {
            "output": text,
            "session_id": session_id,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)