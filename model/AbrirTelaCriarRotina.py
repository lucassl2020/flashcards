from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command
from model.Datas import dia_da_semana_indice


class AbrirTelaCriarRotina(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 25:
            self._stack_telas.screens[7].clear()
            self._stack_telas.open_screen(7)


            conexao, cursor = abrir_banco_de_dados()


            listas_dias = apply_sql_command(cursor, "SELECT dia FROM Dias", retorno="fetchall")


            fechar_banco_de_dados(conexao)


            for lista_dia in listas_dias: 
                dia = lista_dia[0]
                self._stack_telas.screens[7].dias_box.addItem(dia.title())

            self._stack_telas.screens[7].dias_box.setCurrentIndex(dia_da_semana_indice())
            


