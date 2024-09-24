# Função para visualizar o histórico
def consultar_historico():
    for dia in historico_pesquisas:
        data = dia['data']
        dados = dia['dados']
        total, ios, android = calcular_estatisticas(dados)
        idade_media = calcular_idade_media(dados)
        print(f"Data: {data}")
        print(f"Total entrevistados: {total}")
        print(f"Usuários iOS: {ios}, Usuários Android: {android}")
        print(f"Idade média: {idade_media}")
