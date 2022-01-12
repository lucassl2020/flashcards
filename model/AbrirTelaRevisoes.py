from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command
from model.Datas import hoje


class AbrirTelaRevisoes(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] in (0, 14, 19):
            self._stack_telas.screens[1].clear()
            self._stack_telas.open_screen(1)

            today = hoje()

            conexao, cursor = abrir_banco_de_dados()

            lista_grupos_flashcards = apply_sql_command(cursor, "SELECT g.titulo, d.data FROM Grupos AS g INNER JOIN Datas AS d on g.id=d.id_grupo WHERE d.data <= %s" % (today), retorno="fetchall")

            fechar_banco_de_dados(conexao)

            for tupla in lista_grupos_flashcards:
                titulo = tupla[0]
                data_flashcards = tupla[1]

                if today == data_flashcards:
                    self._stack_telas.screens[1].revisoes_do_dia_lista.addItem(titulo)
                else:
                    self._stack_telas.screens[1].revisoes_atrasadas_lista.addItem(titulo)