from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command
from model.Datas import hojeFormatado


class SalvarEstadoDaAtividade(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 31:
            conexao, cursor = abrir_banco_de_dados()


            for i in range(0, self._stack_telas.screens[8].atividades_listwidget.count()):
                item = self._stack_telas.screens[8].atividades_listwidget.item(i)

                atividade = item.text()
                estado = item.checkState() > 0
                data = hojeFormatado()

                apply_sql_command(cursor, "UPDATE Historicos SET state=%s WHERE atividade='%s' AND data='%s'" % (estado, atividade, data), retorno="fetchall")


            fechar_banco_de_dados(conexao)
