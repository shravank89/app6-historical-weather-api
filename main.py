from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("weather.html")


@app.route("/api/v1/<station_id>/<date>")
def api(station_id, date):
    temperature = 23
    return {"station_id": station_id,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)