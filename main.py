import pandas as pd
from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word):
    df = pd.read_csv("dictionary.csv")
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    result_dictionary = {"word": word, "definition": definition}
    return result_dictionary


if __name__ == "__main__":
    app.run(debug=True, port=5001)
