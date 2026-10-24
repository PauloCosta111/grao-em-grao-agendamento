from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Grão em Grão - Agendamento"


if __name__ == "__main__":
    app.run(debug=True)