from flask import Flask, render_template, request

app = Flask(__name__)

subjects = []

@app.route("/", methods=["GET", "POST"])
def index():
    global subjects
    result = None

    if request.method == "POST":

        # ถ้ากดเพิ่มวิชา
        if "add" in request.form:
            name = request.form["name"]
            difficulty = int(request.form["difficulty"])
            subjects.append({"name": name, "difficulty": difficulty})

        # ถ้ากดคำนวณ
        elif "calculate" in request.form:
            days = int(request.form["days"])
            hours_per_day = float(request.form["hours"])

            result = []
            total_weight = sum(sub["difficulty"] for sub in subjects)

            for day in range(1, days + 1):
                daily_plan = []
                for sub in subjects:
                    hours = (sub["difficulty"] / total_weight) * hours_per_day
                    daily_plan.append(
                        f"{sub['name']} {hours:.2f} ชั่วโมง"
                    )
                result.append((day, daily_plan))

    return render_template("index.html", result=result, subjects=subjects)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
