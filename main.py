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


@app.route("/api/v1/<station_id>")
def api2(station_id):
    df = pd.read_csv("data_small/TG_STAID" + station_id.zfill(6) + ".txt", skiprows=20, parse_dates=["    DATE"])
    return df.to_dict(orient="records")


@app.route("/api/v1/yearly/<station_id>/<year>")
def api3(station_id, year):
    df = pd.read_csv("data_small/TG_STAID" + station_id.zfill(6) + ".txt", skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    return df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")


if __name__ == "__main__":
    app.run(debug=True)