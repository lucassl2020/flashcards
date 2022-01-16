from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command


class AbrirTelaHistorico(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] in (33, 35):
            self._stack_telas.screens[9].clear()
            self._stack_telas.open_screen(9)

            conexao, cursor = abrir_banco_de_dados()

            lista_historico = apply_sql_command(cursor, "SELECT data, (100*SUM(state))/COUNT(data) FROM Historicos GROUP BY data ORDER BY id DESC", retorno="fetchall")

            self._stack_telas.screens[9].tabela_historico.setRowCount(len(lista_historico)) 
            self._stack_telas.screens[9].tabela_historico.setHorizontalHeaderLabels(["Data", "Porcentagem de conclusão"])

            fechar_banco_de_dados(conexao)

            indice_linha = 0
            for tupla_valores in lista_historico:
                self._stack_telas.screens[9].adicionarItemTabela(indice_linha, tupla_valores)

                indice_linha += 1
