from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command

def create_database():
    conexao, cursor = abrir_banco_de_dados()

    sql_command = """CREATE TABLE IF NOT EXISTS Grupos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL
            );"""
    apply_sql_command(cursor, sql_command)

    sql_command = """CREATE TABLE IF NOT EXISTS Flashcards(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                pergunta TEXT NOT NULL, 
                resposta TEXT NOT NULL,
                id_grupo INTEGER NOT NULL,
                CONSTRAINT fk_grupo FOREIGN KEY (id_grupo) REFERENCES Grupos (id)
            );"""
    apply_sql_command(cursor, sql_command)

    sql_command = """CREATE TABLE IF NOT EXISTS Datas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data INTEGER NOT NULL, 
                id_grupo INTEGER NOT NULL,
                CONSTRAINT fk_grupo FOREIGN KEY (id_grupo) REFERENCES Grupos (id)
            );"""
    apply_sql_command(cursor, sql_command)


    sql_command = """CREATE TABLE IF NOT EXISTS Dias(
                dia TEXT PRIMARY KEY UNIQUE NOT NULL
            );"""
    apply_sql_command(cursor, sql_command)

    try:
        apply_sql_command(cursor, "INSERT INTO Dias (dia) VALUES ('segunda'), ('terça'), ('quarta'), ('quinta'), ('sexta'), ('sabado'), ('domingo')")
    except:
        pass

    sql_command = """CREATE TABLE IF NOT EXISTS Atividades(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                atividade TEXT NOT NULL,
                dia TEXT NOT NULL,
                CONSTRAINT fk_dia FOREIGN KEY (dia) REFERENCES Dias (dia)
            );"""
    apply_sql_command(cursor, sql_command)

    sql_command = """CREATE TABLE IF NOT EXISTS Historicos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                atividade TEXT NOT NULL,
                data DATE NOT NULL,
                state BOOL NOT NULL
            );"""
    apply_sql_command(cursor, sql_command)

    fechar_banco_de_dados(conexao)

