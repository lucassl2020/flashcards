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
        self.adicione_datas = label(self, "Adicione datas para revisão", 0, 20, 800, 20) 
        self.adicione_datas.setAlignment(Qt.AlignCenter)

        self.criar_datas_padrao_botao = button(self, "Criar data padrão", 280, 80, 100, 30)

        self.carregar_datas_padrao_botao = button(self, "Carregar data padrão", 400, 80, 120, 30)

        self.calendario_widget = calendar(self, 90, 200, 320, 191)
        ano, mes, dia = hojeSplit()
        self.calendario_widget.setMinimumDate(QDate(ano, mes, dia))

        self.datas_listwidget = listWidget(self, 450, 200, 260, 192)

        self.adicionar_botao = button(self, "Adicionar", 90, 392, 320, 41)

        self.remover_botao = button(self, "Remover", 450, 392, 260, 41)

        self.finalizar_botao = button(self, "Finalizar", 325, 500, 150, 41)


    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.adicione_datas.setStyleSheet("color: rgb(210, 210, 210); font: 14pt;")

        self.calendario_widget.setStyleSheet("color: rgb(210, 210, 210);")
        self.datas_listwidget.setStyleSheet('''color: rgb(210, 210, 210); 
                                            border: 1px solid; 
                                            border-top-left-radius: 4px; 
                                            border-top-right-radius: 4px; 
                                            border-color: rgb(84, 84, 84);''')
        
        style_button(button=self.adicionar_botao, cor="verde", tam_fonte="12", border_radius=(0, 0, 5, 5), border_color="(123, 205, 126)")
        style_button(button=self.remover_botao, cor="vermelho", tam_fonte="12", border_radius=(0, 0, 5, 5), border_color="(205, 123, 123)")
        style_button(button=self.finalizar_botao, cor="azul", tam_fonte="12", border_radius=(5, 5, 5, 5), border_color="(123, 166, 205)")
        style_button(button=self.criar_datas_padrao_botao, cor="cinza_escuro", tam_fonte="8", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.carregar_datas_padrao_botao, cor="cinza_escuro", tam_fonte="8", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.adicionar_botao.clicked.connect(self.botaoAdicionar)
        self.remover_botao.clicked.connect(self.botaoRemover)
        self.finalizar_botao.clicked.connect(self.botaoFinalizar)


    def clear(self):
        self.datas_listwidget.clear()


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
