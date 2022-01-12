from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class DeletarFlashcard(Observer):
    def __init__(self, stack_telas, messager):
        self._stack_telas = stack_telas
        self._messager = messager


    def update(self, event):
        if event["codigo"] == 12:
            resposta = self._messager.question(None, "Salvar", "Deseja realmente DELETAR esse FLASHCARD?", self._messager.Yes, self._messager.No)

            if resposta == self._messager.Yes:
                indice = self._stack_telas.screens[6].flashcards_lista.currentRow()

                if indice > -1:
                    titulo = self._stack_telas.screens[6].flashcards_lista.takeItem(indice).text()

                    conexao, cursor = abrir_banco_de_dados()

                    lista_grupo = apply_sql_command(cursor, "SELECT id FROM Grupos WHERE titulo='%s'" % (titulo), "fetchall")
                    id_grupo = lista_grupo[0][0]

                    apply_sql_command(cursor, "DELETE FROM Flashcards WHERE id_grupo=%s" % (id_grupo))
                    apply_sql_command(cursor, "DELETE FROM Datas WHERE id_grupo=%s" % (id_grupo))
                    apply_sql_command(cursor, "DELETE FROM Grupos WHERE id=%s" % (id_grupo))

                    fechar_banco_de_dados(conexao)
