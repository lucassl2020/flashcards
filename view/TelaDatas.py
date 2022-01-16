from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QDate

import sys

from view.Widgets import button, label, listWidget, calendar
from view.StyleButton import style_button

from model.Datas import hojeSplit

from model.Observer import ISubject


class TelaDatas(QWidget):
    def __init__(self, parent=None):
        super(TelaDatas, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._createWidgets()
        self._setStyle()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("Datas")


    def _createWidgets(self):
        self.voltar_botao = button(self, "Voltar", 20, 20, 90, 40)

        self.calendario_widget = calendar(self, 90, 200, 320, 191)

        self.datas_listwidget = listWidget(self, 450, 200, 260, 192)

        self.adicionar_botao = button(self, "Adicionar", 90, 392, 320, 41)

        self.remover_botao = button(self, "Remover", 450, 392, 260, 41)

        self.finalizar_botao = button(self, "Finalizar", 325, 500, 150, 41)


    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.calendario_widget.setStyleSheet("color: rgb(210, 210, 210);")
        self.datas_listwidget.setStyleSheet('''color: rgb(210, 210, 210); 
                                            border: 1px solid; 
                                            border-top-left-radius: 4px; 
                                            border-top-right-radius: 4px; 
                                            border-color: rgb(84, 84, 84);''')
        
        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.adicionar_botao, cor="verde", tam_fonte="12", border_radius=(0, 0, 5, 5), border_color="(123, 205, 126)")
        style_button(button=self.remover_botao, cor="vermelho", tam_fonte="12", border_radius=(0, 0, 5, 5), border_color="(205, 123, 123)")
        style_button(button=self.finalizar_botao, cor="azul", tam_fonte="12", border_radius=(5, 5, 5, 5), border_color="(123, 166, 205)")


    def _setConnects(self):
        self.voltar_botao.clicked.connect(self.botaoVoltar)
        self.adicionar_botao.clicked.connect(self.botaoAdicionar)
        self.remover_botao.clicked.connect(self.botaoRemover)
        self.finalizar_botao.clicked.connect(self.botaoFinalizar)


    def clear(self):
        self.datas_listwidget.clear()
        ano, mes, dia = hojeSplit()
        self.calendario_widget.setMinimumDate(QDate(ano, mes, dia))
        self.calendario_widget.setSelectedDate(QDate(ano, mes, dia))


    def botaoVoltar(self):
        event = {"codigo": 37, "descricao": "Botão VOLTAR da tela EDITAR DATAS"}
        self.subject.notify(event)


    def botaoAdicionar(self):
        event = {"codigo": 21, "descricao": "Botão ADICIONAR da tela DATAS"}
        self.subject.notify(event)


    def botaoRemover(self):
        event = {"codigo": 22, "descricao": "Botão REMOVER da tela DATAS"}
        self.subject.notify(event)


    def botaoFinalizar(self):
        event = {"codigo": 23, "descricao": "Botão FINALIZAR da tela DATAS"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaDatas()
    app.show()
    sys.exit(root.exec_())
