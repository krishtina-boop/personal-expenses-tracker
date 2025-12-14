from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

expenses = []

@app.route("/", methods=["GET", "POST"])
def index():
    show_total = False
    today = date.today().isoformat() 

    if request.method == "POST":
        action = request.form.get("action")

        if action == "add":
            expense_date = request.form["date"] 
            category = request.form["category"]
            amount = float(request.form["amount"])
            note = request.form["note"]

            expenses.append({
                "date": expense_date,
                "category": category,
                "amount": amount,
                "note": note
            })

        elif action == "total":
            show_total = True

        elif action == "delete":
            index = int(request.form["index"])
            expenses.pop(index)

    total = sum(exp["amount"] for exp in expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        show_total=show_total,
        today=today
    )

if __name__ == "__main__":
    app.run(debug=True)
