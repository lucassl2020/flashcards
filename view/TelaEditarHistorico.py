from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

import sys

from view.Widgets import button, label, table, progressBar
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaEditarHistorico(QWidget):
    def __init__(self, parent=None):
        super(TelaEditarHistorico, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("Editar histórico")
 

    def _create_widgets(self):
        self.voltar_botao = button(self, "Voltar", 20, 20, 90, 40)

        self.data_label = label(self, "", 115, 80, 193, 30)
        self.data_label.setAlignment(Qt.AlignLeft)

        self.dia_label = label(self, "", 303, 80, 193, 30)
        self.dia_label.setAlignment(Qt.AlignCenter)

        self.porcentagem_barra_progresso = progressBar(self, 500, 80, 193, 25)

        self.tabela_editar = table(self, 110, 110, 580, 400)
        #Table will fit the screen horizontally
        self.tabela_editar.horizontalHeader().setStretchLastSection(True)
        self.tabela_editar.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabela_editar.horizontalHeader().setDefaultSectionSize(275)
        self.tabela_editar.setColumnCount(2)  

        self.salvar_botao = button(self, "Salvar", 110, 510, 580, 50)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.data_label.setStyleSheet("color: rgb(210, 210, 210);font: 16pt;")
        self.dia_label.setStyleSheet("color: rgb(210, 210, 210);font: 16pt;")
        self.porcentagem_barra_progresso.setStyleSheet("color: rgb(210, 210, 210);font: 16pt;")
        self.tabela_editar.setStyleSheet('''QTableWidget{
                                                color: rgb(210, 210, 210); 
                                                border: 1px solid; 
                                                border-top-left-radius: 4px; 
                                                border-top-right-radius: 4px; 
                                                border-color: rgb(84, 84, 84);
                                                font: 14px
                                            }''')

        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.salvar_botao, cor="azul", tam_fonte="12", border_radius=(0, 0, 5, 5), border_color="(123, 166, 205)")


    def _setConnects(self):
        self.voltar_botao.clicked.connect(self.botaoVoltar)
        self.salvar_botao.clicked.connect(self.botaoSalvar)


    def clear(self):
        self.tabela_editar.clear()


    def botaoVoltar(self):
        event = {"codigo": 35, "descricao": "Botão VOLTAR da tela EDITAR HISTÓRICO"}
        self.subject.notify(event)


    def botaoSalvar(self):
        event = {"codigo": 36, "descricao": "Botão SALVAR da tela EDITAR HISTÓRICO"}
        self.subject.notify(event)


    def adicionarItemTabela(self, linha, valores):
        atividade = QTableWidgetItem(valores[0])
        state = QTableWidgetItem(str(valores[1]))

        atividade.setTextAlignment(Qt.AlignCenter)
        state.setTextAlignment(Qt.AlignCenter)
        
        self.tabela_editar.setItem(linha, 0, atividade)
        self.tabela_editar.setItem(linha, 1, state)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaEditarHistorico()
    app.show()
    sys.exit(root.exec_())
