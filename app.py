from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Takenlijst en huidige taakindex
tasks = [
    "Wasbox bij halve tank",
    "CarPro bij lege tank",
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
    app.run(debug=True)