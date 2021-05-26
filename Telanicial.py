from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QRect
import sys
from Suporte import style_button, SetInterface


class TelaInicial(QWidget, SetInterface):
    def __init__(self, parent=None):
        super(TelaInicial, self).__init__(parent)
        self._settings()
        self._create_widgets()
        self._set_style()
        self._createSetTexts()
        self._createGetTexts()
        self._createConnects()
        self._createSetClears()

    def _settings(self):
        self.resize(350, 300)
        self.setWindowTitle("Inicio")
 
    def _create_widgets(self):
        self.ver_dia_botao = QPushButton("ver dia", self)
        self.ver_dia_botao.setGeometry(QRect(20, 70, 310, 60))

        self.criar_flashcards_botao = QPushButton("criar flashcards", self)
        self.criar_flashcards_botao.setGeometry(QRect(20, 170, 310, 60))

        self.ver_dia_shadow = QGraphicsDropShadowEffect() 
        self.criar_flashcards_shadow = QGraphicsDropShadowEffect() 

    def _set_style(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        style_button(button=self.ver_dia_botao, shadow=self.ver_dia_shadow, cor="(235, 235, 235)", tam_fonte="14", tam_border_radius="5")
        style_button(button=self.criar_flashcards_botao, shadow=self.criar_flashcards_shadow, cor="(235, 235, 235)", tam_fonte="14", tam_border_radius="5")

    def _createSetTexts(self):
        pass

    def _createGetTexts(self):
        pass

    def _createConnects(self):
        self._connects["ver_dia_botao"] = self.ver_dia_botao.clicked.connect
        self._connects["criar_flashcards_botao"] = self.criar_flashcards_botao.clicked.connect

    def _createSetClears(self):
        pass
        

if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaInicial()
    app.show()
    sys.exit(root.exec_())