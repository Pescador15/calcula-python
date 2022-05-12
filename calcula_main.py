import pandas as pd
from datetime import datetime
from calcula_conexao import criar_conexao, fechar_conexao


def insere_entradas(con, valor, data, nome, recorrente):

    valor_entradas = float(input('Valor da conta:'))
    data_entradas = str(input('Digite a data: '))
    data_format = datetime.strptime(data_entradas, '%d-%m-%Y')
    nome_entradas = str(input('Nome da Entrada: '))
    recorrente_entradas = str(input('Recorrente: ')).strip().upper()
    if recorrente_entradas in 'Ss':
        recorrente_entradas = 1
    else:
        recorrente_entradas = 0
    cursor = con.cursor()
    entradas_sql = "INSERT INTO ENTRADAS (valor, data, nome, recorrente) values (%s, %s, %s, %s)"
    input_entradas = (valor_entradas, data_format,
                      nome_entradas, recorrente_entradas)
    cursor.execute(entradas_sql, input_entradas)
    con.commit()
    print('valores de entradas inseridos com sucesso!')
    cursor.close()


def insere_saidas(con, valor, vencimento, nome, recorrente):

    valor_saida = float(input('Valor da saida: '))
    data_saida = str(input('Data da saida: '))
    data_format1 = datetime.strptime(data_saida, '%d-%m-%Y')
    nome_saida = str(input('Descrição da saida: '))
    recorrente_saida = str(input('recorrente: ')).strip().upper()
    if recorrente_saida in 'sS':
        recorrente_saida = 1
    else:
        recorrente_saida = 0
    cursor = con.cursor()
    saida_sql = 'INSERT INTO SAIDAS (valor, vencimento, nome, recorrente) values (%s, %s, %s, %s)'
    input_saida = (valor_saida, data_format1, nome_saida, recorrente_saida)
    cursor.execute(saida_sql, input_saida)
    con.commit()
    print('valores de saídas inseridos com sucesso!')
    cursor.close()


def consulta_entradas(con, valor, data, nome, recorrente):
    cursor = con.cursor()
    input_filtro = str(input('Nome da conta: '))
    cursor.execute("SELECT * FROM entradas WHERE nome='"+input_filtro+"'")
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(valor, 'valor:', coluna[0], 'R$')
        print(data, coluna[1])
        print(nome, 'nome:', coluna[2])
        print(recorrente, coluna[3])


def consulta_saidas(con, valor, vencimento, nome, recorrente):

    input_filtro_saidas = str(input('Nome da conta: '))
    consulta_saidas1 = (
        "SELECT * FROM saidas WHERE nome='"+input_filtro_saidas+"'")
    cursor = con.cursor()
    cursor.execute(consulta_saidas1)
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(valor, 'valor:', coluna[0], 'R$')
        print(vencimento, coluna[1])
        print(nome, 'nome:', coluna[2])
        print(recorrente, coluna[3])


def consulta_pagamento(con, valor, data, descricao, id_saidas, id_entradas,id_pagamento,pago):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pagamento")
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(valor, 'valor:', coluna[0], end='|')
        print(data, 'data:', coluna[1], end='|')
        print(descricao, 'descrição:', coluna[2], end='|')
        print(id_saidas, 'ID saidas:', coluna[3], end='|')
        print(id_entradas, 'ID entradas:', coluna[4], end='|')
        print(id_pagamento, 'ID pagamento:', coluna[5], end='|')
        print(pago, 'pago:', coluna[6])


def main():

    con = criar_conexao("localhost", "root", "", "calcula_python")
    print('''Digite a opção desejada:
    [1] entradas
    [2] saidas
    [3] consulta de dados de entrada
    [4] consulta de dados de saída
    [5] consulta pagamento
    ''')
    opcao = int(input('Qual opção você deseja? '))
    if opcao == 1:
        insere_entradas(con, "", "", "", "")
    elif opcao == 2:
        insere_saidas(con, '', '', '', '')
    elif opcao == 3:
        consulta_entradas(con, '', '', '', '')
    elif opcao == 4:
        consulta_saidas(con, '', '', '', '')
    elif opcao == 5:
        consulta_pagamento(con, '', '', '', '', '', '', '')

    fechar_conexao(con)


if __name__ == "__main__":
    main()



