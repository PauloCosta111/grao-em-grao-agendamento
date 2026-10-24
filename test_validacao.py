from validacao import validar_agendamento


def test_agendamento_valido():
    dados = {
        "nome_responsavel": "Maria",
        "nome_crianca": "Pedro",
        "data": "30/10/2026",
        "horario": "14:00",
    }
    valido, erro = validar_agendamento(dados)
    assert valido is True


def test_agendamento_sem_horario():
    dados = {
        "nome_responsavel": "Maria",
        "nome_crianca": "Pedro",
        "data": "30/10/2026",
    }
    valido, erro = validar_agendamento(dados)
    assert valido is False