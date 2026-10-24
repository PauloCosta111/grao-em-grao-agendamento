def validar_agendamento(dados):
    campos = ["nome_responsavel", "nome_crianca", "data", "horario"]
    for campo in campos:
        if not dados.get(campo):
            return False, f"Campo obrigatório: {campo}"
    return True, ""