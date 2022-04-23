from xmlrpc.client import boolean
from calcula_conexao import criar_conexao, fechar_conexao


    


def insere_entradas(con, valor, data, nome, recorrente):

    valor_entradas = float(input('Valor da conta:'))
    data_entradas = str(input('Digite a data: '))
    nome_entradas = str(input('Nome da conta: '))
    recorrente_entradas = str(input('Recorrente ou não recorrente:'))
    cursor = con.cursor()
    entradas_sql = "INSERT INTO ENTRADAS (valor, data, nome, recorrente) values (%s, %s, %s, %s)"
    input_entradas = (valor_entradas, data_entradas, nome_entradas, recorrente_entradas)
    cursor.execute(entradas_sql, input_entradas)
    con.commit()
    print('valores de entradas inseirdos com sucesso!')
    cursor.close()


def insere_saidas(con, valor, vencimento, nome, recorrente):

    valor_saida = float(input('Valor da saida: '))
    data_saida = str(input('Data da saida: '))
    nome_saida = str(input('Descrição da saida: '))
    recorrente_saida = str(input('Recorrente ou não recorrente:'))
    cursor = con.cursor()
    saida_sql = 'INSERT INTO SAIDAS (valor, vencimento, nome, recorrente) values (%s, %s, %s, %s)'
    input_saida = (valor_saida, data_saida, nome_saida, recorrente_saida)
    cursor.execute(saida_sql, input_saida)
    con.commit()
    print('valores de saídas inseirdos com sucesso!')
    cursor.close()

def insere_ganhos(con, entrada_ganhos, descricao_ganhos):
    valor_ganhos = float(input('Digite o valor do ganho: '))
    descricao_ganho = str(input('Descrição da entrada do ganho: '))
    cursor = con.cursor()
    ganhos_sql = 'INSERT INTO GANHOS (entrada_ganhos, descricao_ganhos) values (%s, %s)'
    input_ganhos = (valor_ganhos, descricao_ganho)
    cursor.execute(ganhos_sql, input_ganhos)
    con.commit()
    print('Ganhos adicionados com sucesso!')
    cursor.close()



def main():
    con = criar_conexao("localhost", "root", "", "calcula_python")
    print(''' Digite a opção desejada:
    [1] entradas
    [2] saidas
    [3] ganhos''')
    opcao = int(input('Qual opção você deseja? '))
    if opcao == 1:
        insere_entradas(con, "", "", "", "")
    elif opcao == 2:
        insere_saidas(con, '', '', '', '')
    elif opcao == 3:
        insere_ganhos(con, '', '')

    
    fechar_conexao(con)


if __name__ == "__main__":
    main()

