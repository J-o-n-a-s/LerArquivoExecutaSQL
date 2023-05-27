# Realiza a leitura de arquivos SQL com o intuito executar os comandos no SQL Server
import sys
import time
import pyodbc


def _conectar_sql(connection_string) -> object:
    ret_erro = False
    try:
        print('\nAguarde a conexão com o banco de dados SQL Server.')
        connection = pyodbc.connect(connection_string)
        print('\nBanco de dados conectado com sucesso.\n')
    except pyodbc.Error as ex:
        ret_erro = True
        connection = 0
        sqlstate = ex.args[1]
        print(f'\nNão foi possível conectar ao banco de dados SQL Server.\n\n{sqlstate}.')
    return connection, ret_erro


def _log_error(exception, p_erro):
    # with open(f'\\log\\' + str(time.strftime("%x")) + '.log', 'w') as arquivo:
    #   arquivo.write(f'{str(time.strftime("%X"))} - {exception} - {p_erro}')
    print(p_erro)


if __name__ == '__main__':
    # Parâmetros de conexão com o banco de dados
    driver = '{SQL Server}'
    server = 'SRVBDDRSUPV\SQLEXPRESS'
    database = 'SCADA'
    trusted_connection = 'yes'
    # Variáveis internas do projeto
    num_linhas = 0
    linhas_inseridas = 0
    linhas_em_branco = 0
    conn = None
    print('+------------------------------------------------------------------------------------------------------+')
    print('| PROGRAMA PARA REALIZAR A LEITURA DE ARQUIVOS SQL COM O INTUITO DE EXECUTAR OS COMANDOS NO SQL SERVER |')
    print('+------------------------------------------------------------------------------------------------------+')
    caminho_arquivo_sql = input('\nDigite o caminho completo, com nome e extensão, do arquivo que deseja ler:\n-> ')
    if not caminho_arquivo_sql:
        caminho_arquivo_sql = r'C:\Users\VETER\Downloads\script-2023-05-23\script-2023-05-23 P2.sql'
        print(f'Usará caminho de arquivo padrão -> {caminho_arquivo_sql}.')
    while True:
        log = input('\nDeseja ver o log de execução?\n'
                    'S - Sim;\n'
                    'N - Não;\n'
                    '-> ')
        if (log.lower() == 's') or (log.lower() == 'n'):
            break
        else:
            print('\nPor gentileza digite uma opção válida.')
    while True:
        info = input('\nPor gentileza digite a opção desejada entre as opções:\n'
                     '1 - Iniciar;\n'
                     '2 - Finalizar;\n'
                     '-> ')
        if info == '2':
            break
        elif info == '1':
            # Captura a hora do início da execução do código para verificar quanto tempo demorou a execução total
            start_t = time.time()
            try:
                print(f'\nTentando ler o arquivo: {caminho_arquivo_sql}.')
                with open(caminho_arquivo_sql, 'r', encoding='utf-16') as file:
                    conn, x_erro = _conectar_sql('Driver=' + driver + ';'
                                                                      'Server=' + server + ';'
                                                                                           'Database=' + database + ';'
                                                                                                                    'Trusted_Connection=' + trusted_connection + ';')
                    if x_erro:
                        break
                    else:
                        cursor = conn.cursor()
                    for linha in file:
                        num_linhas += 1
                        if log.lower() == 's':
                            print(f'Executando a linha -> {num_linhas}.')
                        line_cor = linha.strip()
                        line_cor = line_cor.replace("ÿþ", "")
                        if (line_cor != "") and (line_cor != "GO") and ((line_cor[:6] == "INSERT") and (line_cor[-1:] == ")") or (line_cor[:6] == "SET ID")):
                            cursor.execute(line_cor)
                            conn.commit()
                            linhas_inseridas += 1
                        else:
                            linhas_em_branco += 1
                    conn.close()
                    print(f'\nTotal de linhas do arquivo SQL = {num_linhas}.')
                    print(f'Total de linhas inseridas = {linhas_inseridas}.')
                    print(f'Total de linhas em brancas / não executadas = {linhas_em_branco}.')
                    print(f'Processo finalizado às {time.strftime("%d/%m/%Y %H:%M:%S")}.'
                          f'\nTempo total de execução {(time.time() - start_t):.2f} segundos.')
                    break
            except KeyboardInterrupt as erro:
                _log_error(str(sys.exc_info()[0]), erro)
                print('\nLeitura interrompida.')
                break
            except FileNotFoundError as erro:
                _log_error(str(sys.exc_info()[0]), erro)
                print('\nArquivo não encontrado. Verifique o caminho e o nome do arquivo.')
                break
            except PermissionError as erro:
                _log_error(str(sys.exc_info()[0]), erro)
                print('\nNão foi possível abrir o arquivo. Erro de permissão.')
                break
            except OSError as erro:
                _log_error(str(sys.exc_info()[0]), erro)
                print('\nNão foi possível abrir o arquivo. Verifique o caminho e o nome do arquivo.')
                break
            else:
                print('')
                break
        else:
            print('\nValor digitado é inválido.')
    print('\nAté logo!\n')
