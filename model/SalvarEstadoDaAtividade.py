from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command
from model.Datas import hojeFormatado, dataFormatada


class SalvarEstadoDaAtividade(Observer):
    def __init__(self, stack_telas, AbrirTelaEditarHistorico):
        self._stack_telas = stack_telas
        self._abrir_tela_editar_historico = AbrirTelaEditarHistorico


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

        if event["codigo"] == 36:
            conexao, cursor = abrir_banco_de_dados()


            for i in range(0, self._stack_telas.screens[10].tabela_editar.rowCount()):
                atividade = self._stack_telas.screens[10].tabela_editar.item(i, 0).text()
                estado = self._stack_telas.screens[10].tabela_editar.item(i, 1).text()
                data = dataFormatada(self._stack_telas.screens[10].data_label.text())

                apply_sql_command(cursor, "UPDATE Historicos SET state=%s WHERE atividade='%s' AND data='%s'" % (estado, atividade, data), retorno="fetchall")


            fechar_banco_de_dados(conexao)


            self._abrir_tela_editar_historico.update({"codigo": 34, "descricao": "Atualizar porcentagem da tela EDITAR HISTÓRICO"}) # FORÇANDO ABERTURA DA TELA VER DIA