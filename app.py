from flask import Flask, jsonify, request

app = Flask(__name__)
agendamentos = []


@app.route("/")
def inicio():
    return "Grão em Grão - Agendamento"


@app.route("/agendamentos", methods=["GET"])
def listar():
    return jsonify(agendamentos)


@app.route("/agendamentos", methods=["POST"])
def criar():
    dados = request.get_json() or {}
    agendamentos.append(dados)
    return jsonify(dados), 201


if __name__ == "__main__":
    app.run(debug=True)