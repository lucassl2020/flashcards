from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect, QLabel, QSpinBox, QGroupBox, QRadioButton, QVBoxLayout 
from PyQt5.QtCore import Qt, QRect
import sys
from Suporte import style_button, SetInterface


class TelaOpcoesRevisao(QWidget, SetInterface):
    def __init__(self, parent=None):
        super(TelaOpcoesRevisao, self).__init__(parent)
        self._settings()
        self._createWidgets()
        self._setStyle()
        self._createSetTexts()
        self._createGetTexts()
        self._createConnects()
        self._createSetClears()

    def _settings(self):
        self.resize(400, 300)
        self.setWindowTitle("Opções")
 
    def _createWidgets(self):
        self.qtd_ciclos_label = QLabel("Quantos ciclos (repetições dos flashcards)?", self)
        self.qtd_ciclos_label.setGeometry(QRect(95, 40, 210, 20))
        self.qtd_ciclos_label.setAlignment(Qt.AlignCenter)

        self.qtd_ciclos_spinbox = QSpinBox(self)
        self.qtd_ciclos_spinbox.setGeometry(QRect(145, 60, 110, 20))

        self.modo_do_ciclo_groupbox = QGroupBox("Modo do ciclo", self)
        self.modo_do_ciclo_groupbox.setGeometry(QRect(60, 120, 280, 80))

        self.ordenar_flashcards_radiobutton = QRadioButton("ordenar flashcards com base nos acertos e erros")
        self.ordenar_flashcards_radiobutton.setChecked(True)
        
        self.retirar_flashcard_radiobutton = QRadioButton("retirar flashcard ao acertar")

        self.iniciar_botao = QPushButton("iniciar", self)
        self.iniciar_botao.setGeometry(QRect(80, 230, 100, 30))

        self.voltar_botao = QPushButton("voltar", self)
        self.voltar_botao.setGeometry(QRect(220, 230, 100, 30))

        self.iniciar_shadow = QGraphicsDropShadowEffect()
        self.voltar_shadow = QGraphicsDropShadowEffect()
        
        vlayout = QVBoxLayout()

        vlayout.addWidget(self.ordenar_flashcards_radiobutton)
        vlayout.addWidget(self.retirar_flashcard_radiobutton)

        self.modo_do_ciclo_groupbox.setLayout(vlayout)

    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        style_button(button=self.iniciar_botao, shadow=self.iniciar_shadow, cor="azul", tam_fonte="10", tam_border_radius="5")
        style_button(button=self.voltar_botao, shadow=self.voltar_shadow, cor="cinza", tam_fonte="10", tam_border_radius="5")

    def _createSetTexts(self):
        pass

    def _createGetTexts(self):
        pass

    def _createConnects(self):
        self._connects["iniciar_botao"] = self.iniciar_botao.clicked.connect
        self._connects["voltar_botao"] = self.voltar_botao.clicked.connect

    def _createSetClears(self):
        self._clears["qtd_ciclos_spinbox"] = self.qtd_ciclos_spinbox.clear

    def setText_texto(self, texto):
        pass


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaOpcoesRevisao()
    app.show()
    sys.exit(root.exec_())
