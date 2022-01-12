import sqlite3


def abrir_banco_de_dados():
    conexao = sqlite3.connect("model\\banco de dados.db")

    return conexao, conexao.cursor()


def fechar_banco_de_dados(conexao):
    conexao.commit()

    conexao.close()


def apply_sql_command(cursor, sql_command, retorno=None):
    cursor.execute(sql_command)

    if retorno == "fetchall":
        valor = cursor.fetchall()
    elif retorno == "lastrowid":
        valor = cursor.lastrowid 
    else:
        valor = None

    return valor
