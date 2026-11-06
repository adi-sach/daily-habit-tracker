# This project was developed with assistance from AI tools (ChatGPT)
# for conceptual understanding, debugging, and code structure guidance.
# All final implementation decisions and code integration were done by me.

from flask import Flask, render_template, request, redirect, url_for
from cs50 import SQL
from datetime import date

app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///habits.db")


@app.route("/")
def index():
    today = date.today().isoformat()

    habits = db.execute("""
        SELECT habits.id,
               habits.name,
               COALESCE(habit_logs.completed, 0) AS completed
        FROM habits
        LEFT JOIN habit_logs
            ON habits.id = habit_logs.habit_id
            AND habit_logs.date = ?
        ORDER BY habits.id;
    """, today)

    return render_template("index.html", habits=habits, today=today)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")

        if name:
            db.execute(
                "INSERT INTO habits (name) VALUES (?);",
                name
            )

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/complete/<int:habit_id>", methods=["POST"])
def complete(habit_id):
    today = date.today().isoformat()

    db.execute("""
        INSERT INTO habit_logs (habit_id, date, completed)
        VALUES (?, ?, 1)
        ON CONFLICT(habit_id, date)
        DO UPDATE SET completed = 1;
    """, habit_id, today)

    return redirect(url_for("index"))

@app.route("/history")
def history():
    logs = db.execute("""
        SELECT habit_logs.date,
               habits.name,
               habit_logs.completed
        FROM habit_logs
        JOIN habits
            ON habit_logs.habit_id = habits.id
        ORDER BY habit_logs.date DESC, habits.name;
    """)

    return render_template("history.html", logs=logs)



if __name__ == "__main__":
    app.run(debug=True)
