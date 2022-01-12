from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command
from model.Datas import dia_da_semana, hojeFormatado


class AbrirTelaRotina(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 24:
            self._stack_telas.screens[8].clear()
            self._stack_telas.open_screen(8)

            hoje_formatado = hojeFormatado()
            dia = dia_da_semana()
            self._stack_telas.screens[8].atividades.setText(dia.upper())


            conexao, cursor = abrir_banco_de_dados()


            listas_atividades = apply_sql_command(cursor, "SELECT atividade FROM Atividades WHERE dia='%s'" % (dia), retorno="fetchall")
            for lista_atividade in listas_atividades: 
                atividade = lista_atividade[0]
                estado = 0 # False

                lista_historicos = apply_sql_command(cursor, "SELECT state FROM Historicos WHERE atividade='%s' AND data='%s'" % (atividade, hoje_formatado), retorno="fetchall")

                if not lista_historicos:
                    apply_sql_command(cursor, "INSERT INTO Historicos (atividade, data, state) VALUES ('%s', '%s', 0)" % (atividade, hoje_formatado))
                else:
                    estado = lista_historicos[0][0]
                
                self._stack_telas.screens[8].adicionarCheckBox(atividade, estado)


            fechar_banco_de_dados(conexao)
