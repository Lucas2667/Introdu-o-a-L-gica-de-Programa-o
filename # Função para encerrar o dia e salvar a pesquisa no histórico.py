# Função para encerrar o dia e salvar a pesquisa no histórico
def encerrar_dia():
    if pesquisa_dia:
        historico_pesquisas.append({
            'data': 'data_atual',  # Exemplo: data atual
            'dados': pesquisa_dia.copy()
        })
        pesquisa_dia.clear()  # Limpa a pesquisa para o próximo dia
