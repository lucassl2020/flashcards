from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class CriarESalvarRotina(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 27:
            dia = self._stack_telas.screens[7].dias_box.currentText().lower()
            atividades = self._stack_telas.screens[7].atividade_line.text()

            lista_atividades = atividades.split(',')

            conexao, cursor = abrir_banco_de_dados()


            for atividade in lista_atividades:
                self._stack_telas.screens[7].atividades_listwidget.addItem(atividade)

                apply_sql_command(cursor, "INSERT INTO Atividades (atividade, dia) VALUES ('%s', '%s')" % (atividade, dia))
            

            fechar_banco_de_dados(conexao)


        if event["codigo"] == 28:
            dia = self._stack_telas.screens[7].dias_box.currentText().lower()
            atividade = self._stack_telas.screens[7].atividades_listwidget.takeItem(self._stack_telas.screens[7].atividades_listwidget.currentRow()).text()
            

            conexao, cursor = abrir_banco_de_dados()


            apply_sql_command(cursor, "DELETE FROM Atividades WHERE atividade='%s' AND dia='%s'" % (atividade, dia))
            print("DELETE FROM Atividades WHERE atividade='%s' AND dia='%s'" % (atividade, dia))

            fechar_banco_de_dados(conexao)


        if event["codigo"] == 29:
            dia = self._stack_telas.screens[7].dias_box.currentText().lower()
            self._stack_telas.screens[7].atividades_listwidget.clear()

            conexao, cursor = abrir_banco_de_dados()

            listas_atividades = apply_sql_command(cursor, "SELECT a.atividade FROM Atividades as a INNER JOIN Dias as d ON a.dia=d.dia WHERE d.dia='%s'" % (dia), retorno="fetchall")
            for lista_atividade in listas_atividades: 
                atividade = lista_atividade[0]
                self._stack_telas.screens[7].atividades_listwidget.addItem(atividade)


            fechar_banco_de_dados(conexao)
