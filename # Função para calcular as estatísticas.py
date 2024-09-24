# Função para calcular as estatísticas
def calcular_estatisticas(pesquisa):
    total = len(pesquisa)
    ios = len([cliente for cliente in pesquisa if cliente['sistema'] == 'iOS'])
    android = len([cliente for cliente in pesquisa if cliente['sistema'] == 'Android'])
    return total, ios, android
