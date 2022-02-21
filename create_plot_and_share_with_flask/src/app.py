from fileinput import filename
from flask import Flask, render_template, send_from_directory
import src.create_plots as create_plots

import os

# Constants

BASE_DIRECTORY = "src"
PLOTS_DIRECTORY = "plots"
PLOTS_PATH = os.path.join(BASE_DIRECTORY, PLOTS_DIRECTORY)

# Plot creation

create_plots.create_barplot(os.path.join(PLOTS_PATH, "barplot.png"))
create_plots.create_scatterplot(os.path.join(PLOTS_PATH, "scatterplot.png"))

plots: list[dict[str, str]] = [
    {
        "name": "Awesome Bars",
        "filename": "barplot.png"
    },
    {
        "name": "Cool scatterplot",
        "filename": "scatterplot.png"
    },
]

# App

app = Flask(__name__)
app.secret_key = "super secret password"

# Routes

@app.route("/")
def home_template():
    return render_template("index.html", plots=plots)

@app.route("/plots/<path:name>")
def show_plot(name):
    return send_from_directory("plots", name)



if __name__ == "__main__":
    app.run()
