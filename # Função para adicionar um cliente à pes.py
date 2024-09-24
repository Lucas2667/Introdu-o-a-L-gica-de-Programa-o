# Função para adicionar um cliente à pesquisa diária
def adicionar_cliente(idade, sistema):
    cliente = {
        'idade': idade,
        'sistema': sistema
    }
    pesquisa_dia.append(cliente)
