# Função para calcular a idade média
def calcular_idade_media(pesquisa):
    if not pesquisa:
        return 0  # Evitar divisão por zero
    total_idade = sum([cliente['idade'] for cliente in pesquisa])
    return total_idade / len(pesquisa)
