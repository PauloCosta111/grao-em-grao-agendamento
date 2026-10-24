import pytest
from app import app, agendamentos


@pytest.fixture
def client():
    agendamentos.clear()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_pagina_inicial(client):
    resposta = client.get("/")
    assert resposta.status_code == 200


def test_criar_agendamento_valido(client):
    dados = {
        "nome_responsavel": "Maria",
        "nome_crianca": "Pedro",
        "data": "30/10/2026",
        "horario": "14:00",
    }
    resposta = client.post("/agendamentos", json=dados)
    assert resposta.status_code == 201

    lista = client.get("/agendamentos")
    assert len(lista.get_json()) == 1


def test_criar_agendamento_sem_horario(client):
    dados = {
        "nome_responsavel": "Maria",
        "nome_crianca": "Pedro",
        "data": "30/10/2026",
    }
    resposta = client.post("/agendamentos", json=dados)
    assert resposta.status_code == 400
    assert "horario" in resposta.get_json()["erro"]