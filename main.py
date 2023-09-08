from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


station = pd.read_csv("data_small/stations.txt", skiprows=17)
station = station[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("weather.html", data=station.to_html())


@app.route("/api/v1/<station_id>/<date>")
def api(station_id, date):
    df = pd.read_csv("data_small/TG_STAID" + station_id.zfill(6) + ".txt", skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].item() / 10
    return {"station_id": station_id,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)