from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class AbrirTelaFlashcards(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 2:
            self._stack_telas.screens[6].clear()
            self._stack_telas.open_screen(6)

            conexao, cursor = abrir_banco_de_dados()

            lista_grupos_flashcards = apply_sql_command(cursor, "SELECT titulo FROM Grupos", retorno="fetchall")

            fechar_banco_de_dados(conexao)
        
            for tupla in lista_grupos_flashcards:
                titulo = tupla[0]

                self._stack_telas.screens[6].flashcards_lista.addItem(titulo)
            