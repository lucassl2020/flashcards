from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton
from PyQt5.QtCore import Qt

import sys

from view.Widgets import button, label, spinBox, groupBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaOpcoesRevisao(QWidget):
    def __init__(self, parent=None):
        super(TelaOpcoesRevisao, self).__init__(parent)
        
        self.subject = ISubject()

        self._settings()
        self._createWidgets()
        self._setStyle()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(400, 300)
        self.setWindowTitle("Opções")

 
    def _createWidgets(self):
        self.qtd_ciclos_label = label(self, "Quantos ciclos (repetições dos flashcards)?", 0, 30, 400, 30)
        self.qtd_ciclos_label.setAlignment(Qt.AlignCenter)

        self.qtd_ciclos_spinbox = spinBox(self, 145, 60, 110, 20)

        self.modo_do_ciclo_groupbox = groupBox(self, "Modo do ciclo", 10, 120, 380, 80)

        self.revisar_botao = button(self, "Revisar", 80, 230, 100, 30)

        self.voltar_botao = button(self, "Voltar", 220, 230, 100, 30)
        
        self.ordenar_flashcards_radiobutton = QRadioButton("Ordenar flashcards com base nos acertos e erros")
        self.ordenar_flashcards_radiobutton.setChecked(True)
        
        self.retirar_flashcard_radiobutton = QRadioButton("Retirar flashcard ao acertar")


        vlayout = QVBoxLayout()

        vlayout.addWidget(self.ordenar_flashcards_radiobutton)
        vlayout.addWidget(self.retirar_flashcard_radiobutton)

        self.modo_do_ciclo_groupbox.setLayout(vlayout)


    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.qtd_ciclos_label.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")
        self.ordenar_flashcards_radiobutton.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")
        self.retirar_flashcard_radiobutton.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")
        self.modo_do_ciclo_groupbox.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")
        self.qtd_ciclos_spinbox.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")

        style_button(button=self.revisar_botao, cor="azul", tam_fonte="12", border_radius=(5, 5, 5, 5), border_color="(123, 166, 205)")
        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.revisar_botao.clicked.connect(self.botaoRevisar)
        self.voltar_botao.clicked.connect(self.botaoVoltar)


    def clear(self):
        self.qtd_ciclos_spinbox.clear()


    def botaoRevisar(self):
        event = {"codigo": 13, "descricao": "Botão REVISAR da tela OPCOES REVISAO"}
        self.subject.notify(event)


    def botaoVoltar(self):
        event = {"codigo": 14, "descricao": "Botão VOLTAR da tela OPCOES REVISAO"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaOpcoesRevisao()
    app.show()
    sys.exit(root.exec_())
