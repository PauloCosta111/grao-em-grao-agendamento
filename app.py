from flask import Flask, jsonify, request, render_template
from validacao import validar_agendamento

app = Flask(__name__)
agendamentos = []


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/agendamentos", methods=["GET"])
def listar():
    return jsonify(agendamentos)


@app.route("/agendamentos", methods=["POST"])
def criar():
    dados = request.get_json() or {}
    valido, erro = validar_agendamento(dados)
    if not valido:
        return jsonify({"erro": erro}), 400
    agendamentos.append(dados)
    return jsonify(dados), 201


if __name__ == "__main__":
    app.run(debug=True)