from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>/")  # < > brackets are used in Flask for user-entered values
def define(word):
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    return {"word": word,
            "definition": definition}


if __name__ == "__main__":
    app.run(debug=True, port=5001)
