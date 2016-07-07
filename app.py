from flask import Flask

from ciphersolver import solve


app = Flask(__name__)


@app.route("/")
def main():
  return "Hello World!"


@app.route("/words/<w>")
def words(w):
  solved, suspected = solve(w)

  return str(suspected)


if __name__ == "__main__":
  app.run(debug=True)
