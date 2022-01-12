from PyQt5.QtWidgets import QApplication, QWidget

import sys

from view.Widgets import button, label, listWidget
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaRevisoes(QWidget):
    def __init__(self, parent=None):
        super(TelaRevisoes, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("Revisões")


    def _create_widgets(self):
        self.voltar_botao = button(self, "Voltar", 20, 20, 90, 40)

        self.revisoes_atrasadas_label = label(self, "Revisões atrasadas", 100, 158, 160, 50)

        self.revisoes_do_dia_label = label(self, "Revisões do dia", 405, 158, 140, 50)

        self.revisoes_atrasadas_lista = listWidget(self, 95, 200, 300, 240)

        self.revisoes_do_dia_lista = listWidget(self, 400, 200, 300, 240)

        self.revisar_atrasado_botao = button(self, "Revisar atrasado", 95, 440, 300, 41)

        self.revisar_atual_botao = button(self, "Revisar do dia", 400, 440, 300, 41)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.revisoes_atrasadas_label.setStyleSheet("color: rgb(210, 210, 210); font: 14pt;")
        self.revisoes_do_dia_label.setStyleSheet("color: rgb(210, 210, 210); font: 14pt;")
        self.revisoes_atrasadas_lista.setStyleSheet('''color: rgb(210, 210, 210); 
                                    border: 1px solid; 
                                    border-top-left-radius: 4px; 
                                    border-top-right-radius: 4px; 
                                    border-color: rgb(84, 84, 84);
                                    font: 14px;''')
        self.revisoes_do_dia_lista.setStyleSheet('''color: rgb(210, 210, 210); 
                                    border: 1px solid; 
                                    border-top-left-radius: 4px; 
                                    border-top-right-radius: 4px; 
                                    border-color: rgb(84, 84, 84);
                                    font: 14px;''')
                                
        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.revisar_atrasado_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(0, 0, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.revisar_atual_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(0, 0, 5, 5), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.voltar_botao.clicked.connect(self.botaoVoltar)
        self.revisar_atrasado_botao.clicked.connect(self.botaoRevisarAtrasado)
        self.revisar_atual_botao.clicked.connect(self.botaoRevisarAtual)


    def clear(self):
        self.revisoes_atrasadas_lista.clear()
        self.revisoes_do_dia_lista.clear()


    def botaoVoltar(self):
        event = {"codigo": 3, "descricao": "Botão VOLTAR da tela REVISOES"}
        self.subject.notify(event)


    def botaoRevisarAtrasado(self):
        if self.revisoes_atrasadas_lista.currentItem():
            event = {"codigo": 4, "descricao": "Botão REVISAR ATRASADO da tela REVISOES"}
            self.subject.notify(event)


    def botaoRevisarAtual(self):
        if self.revisoes_do_dia_lista.currentItem():
            event = {"codigo": 5, "descricao": "Botão REVISAR ATUAL da tela REVISOES"}
            self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaRevisoes()
    app.show()
    sys.exit(root.exec_())
