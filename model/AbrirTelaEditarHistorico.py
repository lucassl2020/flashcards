from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command
from model.Datas import diaDaSemanaData

class AbrirTelaEditarHistorico(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 34:
            self._stack_telas.screens[10].clear()
            self._stack_telas.open_screen(10)

            indice = self._stack_telas.screens[9].tabela_historico.currentRow()
            data = self._stack_telas.screens[9].tabela_historico.item(indice, 0).text()

            self._stack_telas.screens[10].data_label.setText(data)
            self._stack_telas.screens[10].dia_label.setText(diaDaSemanaData(data).upper())

            data = data.split('/')
            data = data[2] + '-' + data[1] + '-' + data[0]

            conexao, cursor = abrir_banco_de_dados()


            lista_historico = apply_sql_command(cursor, "SELECT atividade, state FROM Historicos WHERE data='%s'" % (data), retorno="fetchall")


            fechar_banco_de_dados(conexao)


            lista_state = [value[1] for value in lista_historico]
            porcentagem = int(100 * (sum(lista_state) / len(lista_state)))
            self._stack_telas.screens[10].porcentagem_barra_progresso.setValue(porcentagem)


            self._stack_telas.screens[10].tabela_editar.setRowCount(len(lista_historico)) 
            self._stack_telas.screens[10].tabela_editar.setHorizontalHeaderLabels(["Atividade", "Estado"])

            indice_linha = 0
            for tupla_valores in lista_historico:
                self._stack_telas.screens[10].adicionarItemTabela(indice_linha, tupla_valores)

                indice_linha += 1
