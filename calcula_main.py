from calcula_conexao import criar_conexao, fechar_conexao


    


def insere_entradas(con, valor, data, nome, recorrente):

    valor_entradas = float(input('Valor da conta:'))
    data_entradas = str(input('Digite a data: '))
    nome_entradas = str(input('Nome da conta: '))
    recorrente_entradas = str(input('Recorrente: ')).strip().upper()
    if recorrente_entradas in 'Ss':
        recorrente_entradas = 1
    else:
        recorrente_entradas = 0
    cursor = con.cursor()
    entradas_sql = "INSERT INTO ENTRADAS (valor, data, nome, recorrente) values (%s, %s, %s, %s)"
    input_entradas = (valor_entradas, data_entradas, nome_entradas, recorrente_entradas)
    cursor.execute(entradas_sql, input_entradas)
    con.commit()
    print('valores de entradas inseridos com sucesso!')
    cursor.close()


def insere_saidas(con, valor, vencimento, nome, recorrente):

    valor_saida = float(input('Valor da saida: '))
    data_saida = str(input('Data da saida: '))
    nome_saida = str(input('Descrição da saida: '))
    recorrente_saida = str(input('recorrente: ')).strip().upper()
    if recorrente_saida in 'sS':
        recorrente_saida = 1
    else:
        recorrente_saida = 0
    cursor = con.cursor()
    saida_sql = 'INSERT INTO SAIDAS (valor, vencimento, nome, recorrente) values (%s, %s, %s, %s)'
    input_saida = (valor_saida, data_saida, nome_saida, recorrente_saida)
    cursor.execute(saida_sql, input_saida)
    con.commit()
    print('valores de saídas inseridos com sucesso!')
    cursor.close()



def main():
    con = criar_conexao("localhost", "root", "", "calcula_python")
    print('''Digite a opção desejada:
    [1] entradas
    [2] saidas''')
    opcao = int(input('Qual opção você deseja? '))
    if opcao == 1:
        insere_entradas(con, "", "", "", "")
    elif opcao == 2:
        insere_saidas(con, '', '', '', '')
    

    
    fechar_conexao(con)


if __name__ == "__main__":
    main()


