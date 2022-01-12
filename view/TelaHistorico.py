from PyQt5.QtWidgets import QApplication, QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel

import sys

from view.Widgets import button, label, table
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaHistorico(QWidget):
    def __init__(self, parent=None):
        super(TelaHistorico, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("Histórico")
 

    def _create_widgets(self):
        self.voltar_botao = button(self, "Voltar", 20, 20, 90, 40)

        self.historico_label = label(self, "Histórico", 350, 80, 100, 30)

        self.tabela_historico = table(self, 110, 110, 580, 400)
        #Table will fit the screen horizontally
        self.tabela_historico.horizontalHeader().setStretchLastSection(True)
        self.tabela_historico.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabela_historico.horizontalHeader().setDefaultSectionSize(280)
        self.tabela_historico.setColumnCount(2)  


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.historico_label.setStyleSheet("color: rgb(210, 210, 210);font: 16pt;")
        self.tabela_historico.setStyleSheet('''QTableWidget{
                                                color: rgb(210, 210, 210); 
                                                border: 1px solid; 
                                                border-top-left-radius: 4px; 
                                                border-top-right-radius: 4px; 
                                                border-color: rgb(84, 84, 84);
                                                font: 14px
                                            }''')

        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.voltar_botao.clicked.connect(self.botaoVoltar)


    def clear(self):
        self.tabela_historico.clear()


    def botaoVoltar(self):
        event = {"codigo": 32, "descricao": "Botão VOLTAR da tela HISTÓRICO"}
        self.subject.notify(event)


    def adicionarItemTabela(self, linha, valores):
        lista_data = valores[0].split("-")
        data = QTableWidgetItem(lista_data[2] + "/" + lista_data[1]  + "/" + lista_data[0])
        porcentagem_de_conclusao = QTableWidgetItem(str(valores[1]) + "%")
       
        data.setTextAlignment(Qt.AlignCenter)
        porcentagem_de_conclusao.setTextAlignment(Qt.AlignCenter)
        
        self.tabela_historico.setItem(linha, 0, data)
        self.tabela_historico.setItem(linha, 1, porcentagem_de_conclusao)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaHistorico()
    app.show()
    sys.exit(root.exec_())
