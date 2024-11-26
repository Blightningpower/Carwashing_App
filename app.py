import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Takenlijst en huidige taakindex
tasks = [
    "Wasbox bij halve tank",
    "CarPro bij lege tank",
    "Wasbox bij halve tank",
    "Washin7 bij lege tank"
]
current_task_index = 0

@app.route("/")
def index():
    """Toon de huidige taak."""
    current_task = tasks[current_task_index]
    return render_template("index.html", task=current_task)

@app.route("/complete", methods=["POST"])
def complete_task():
    """Markeer de huidige taak als voltooid en ga naar de volgende."""
    global current_task_index
    current_task_index = (current_task_index + 1) % len(tasks)  # Ga naar de volgende taak
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Gebruik de dynamische poort die Heroku toewijst
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)