from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def schedule_planner():
    return render_template("schedule_planner.html")

@app.route("/plan", methods=["POST"])
def plan_schedule():
    start_time = request.form["start_time"]
    end_time = request.form["end_time"]
    activities = request.form["activities"].split(",")

    return render_template("planned_schedule.html", start_time=start_time, end_time=end_time, activities=activities)

if __name__ == "__main__":
    app.run()