from flask import Flask, render_template, request, redirect

app = Flask(__name__)

NOTES_FILE = "notes.txt"

def read_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

@app.route("/")
def index():
    notes = read_notes()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    note = request.form.get("note")
    if note:
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")
    return redirect("/")

@app.route("/health")
def health():
    return "App is healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

