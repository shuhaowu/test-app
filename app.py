import os

from flask import Flask, render_template, request, redirect, url_for, flash

from ciphersolver import solve


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def main():
  return render_template("index.html")


@app.route("/solve")
def s():
  c = request.args.get("c", "")
  if c == "":
    flash("ERROR: You must provide some cipher text.")
    return redirect(url_for("main"))

  solved, suspected = solve(c)
  return render_template("solved.html", solved=solved, suspected=suspected, c=c)


if __name__ == "__main__":
  app.run(debug=True)
