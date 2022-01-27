def perguntar():
    return   input("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuário\n" +
            "<P> - Para Pesquisar um usuário\n" +
            "<E> - Para Excluir um usuário\n" +
             "<L> - Para Listar um usuário\n"
).upper()

def inserir(dicionario):
            chave =  input("Digite o Login: ").upper()
            nome =  input("Digite o Nome: ").upper()
            data =  input("Digite o última data de acesso: ").upper()
            estacao =  input("Última estação acessada: ").upper()
            dicionario[chave] = [nome, data, estacao] 