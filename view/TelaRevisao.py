from PyQt5.QtWidgets import QApplication, QWidget, QStatusBar
from PyQt5.QtCore import Qt

import sys

from view.Widgets import button, label, textEdit, lineEdit
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaRevisao(QWidget):
    def __init__(self, parent=None):
        super(TelaRevisao, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._createWidgets()
        self._setStyle()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 610)
        self.setWindowTitle("Revisão")
 

    def _createWidgets(self):
        self.ciclo_label = label(self, "Ciclo:", 635, 20, 90, 40)
        self.ciclo_label.setAlignment(Qt.AlignCenter)

        self.ciclo_line = lineEdit(self, 700, 25, 60, 30)
        self.ciclo_line.setEnabled(False)
        self.ciclo_line.setAlignment(Qt.AlignCenter)

        self.pergunta_ou_resposta = label(self, "Pergunta", 350, 65, 100, 30)
        self.pergunta_ou_resposta.setAlignment(Qt.AlignCenter)

        self.anterior_botao = button(self, "<", 100, 280, 40, 40)

        self.proximo_botao = button(self, ">", 660, 280, 40, 40)

        self.acertei_botao = button(self, "Acertei", 150, 450, 250, 50)

        self.errei_botao = button(self, "Errei", 400, 450, 250, 50)

        self.voltar_botao = button(self, "Voltar", 20, 20, 90, 40)

        self.salvar_botao = button(self, "Salvar", 150, 510, 500, 50)

        self.texto = textEdit(self, 150, 100, 500, 350)


    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.pergunta_ou_resposta.setStyleSheet("color: rgb(210, 210, 210); font: 14pt;")
        self.ciclo_label.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")
        self.texto.setStyleSheet('''font: 12pt;
                                    color: rgb(210, 210, 210); 
                                    border: 1px solid; 
                                    border-top-left-radius: 4px; 
                                    border-top-right-radius: 4px; 
                                    border-color: rgb(84, 84, 84);''')
        self.ciclo_line.setStyleSheet("color: rgb(210, 210, 210); border-radius: 4px; border: 1px solid; border-color: rgb(84, 84, 84);")

        style_button(button=self.anterior_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(20, 20, 20, 20), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.proximo_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(20, 20, 20, 20), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.acertei_botao, cor="verde", tam_fonte="12", border_radius=(0, 0, 5, 0), border_color="(123, 205, 126)")
        style_button(button=self.errei_botao, cor="vermelho", tam_fonte="12", border_radius=(0, 0, 0, 5), border_color="(205, 123, 123)")
        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.salvar_botao, cor="azul", tam_fonte="12", border_radius=(5, 5, 5, 5), border_color="(123, 166, 205)")


    def _setConnects(self):
        self.anterior_botao.clicked.connect(self.botaoAnterior)
        self.proximo_botao.clicked.connect(self.botaoProximo)
        self.acertei_botao.clicked.connect(self.botaoAcertei)
        self.errei_botao.clicked.connect(self.botaoErrei)
        self.voltar_botao.clicked.connect(self.botaoVoltar)
        self.salvar_botao.clicked.connect(self.botaoSalvar)


    def clear(self):
        self.texto.clear()
        #self.ciclo_line.clear()


    def botaoAnterior(self):
        event = {"codigo": 15, "descricao": "Botão ANTERIOR da tela REVISAO"}
        self.subject.notify(event)


    def botaoProximo(self):
        event = {"codigo": 16, "descricao": "Botão PROXIMO da tela REVISAO"}
        self.subject.notify(event)


    def botaoAcertei(self):
        event = {"codigo": 17, "descricao": "Botão ACERTEI da tela REVISAO"}
        self.subject.notify(event)


    def botaoErrei(self):
        event = {"codigo": 18, "descricao": "Botão ERREI da tela REVISAO"}
        self.subject.notify(event)


    def botaoVoltar(self):
        event = {"codigo": 19, "descricao": "Botão VOLTAR da tela REVISAO"}
        self.subject.notify(event)


    def botaoSalvar(self):
        event = {"codigo": 20, "descricao": "Botão SALVAR da tela REVISAO"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaRevisao()
    app.show()
    sys.exit(root.exec_())
