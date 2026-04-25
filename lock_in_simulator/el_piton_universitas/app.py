from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

URL = "https://elif.cz/LA_2526"

def fetch_grades():
    """Scrape grade table from the given webpage."""
    try:
        r = requests.get(URL)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("table")
        if table:
            df = pd.read_html(str(table))[0]
            return df.to_html(classes="table table-striped", index=False)
        else:
            return "<p>No table found on the website.</p>"
    except Exception as e:
        return f"<p>Error fetching grades: {e}</p>"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        username = request.form["username"]
        bet = float(request.form["bet"])
        actual = float(request.form["actual"])
        diff = actual - bet

        if diff >= 0:
            result = f"🎉 {username}, you met or beat your bet by {diff:.1f} points!"
        else:
            result = f"😞 {username}, you missed your bet by {-diff:.1f} points."

        return render_template("result.html", result=result)

    table_html = fetch_grades()
    return render_template("index.html", table_html=table_html)

if __name__ == "__main__":
    app.run(debug=True)
