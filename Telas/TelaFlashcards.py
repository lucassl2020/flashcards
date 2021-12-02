from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect, QLabel, QListWidget
from PyQt5.QtCore import Qt, QRect
import sys
from Suporte import style_button, SetInterface


class TelaFlashcards(QWidget, SetInterface):
    def __init__(self, parent=None):
        super(TelaFlashcards, self).__init__(parent)
        self._settings()
        self._create_widgets()
        self._set_style()
        self._createSetTexts()
        self._createGetTexts()
        self._createConnects()
        self._createSetClears()

    def _settings(self):
        self.resize(800, 600)
        self.setWindowTitle("flashcards")
 
    def _create_widgets(self):
        self.voltar_botao = QPushButton("voltar", self)
        self.voltar_botao.setGeometry(QRect(20, 20, 90, 40))

        self.filtros_botao = QPushButton("filtros", self)
        self.filtros_botao.setGeometry(QRect(690, 20, 90, 40))

        self.flashcards_label = QLabel("Flashcards", self)
        self.flashcards_label.setGeometry(QRect(350, 80, 100, 30))

        self.flashcards_lista = QListWidget(self)
        self.flashcards_lista.setGeometry(QRect(110, 110, 580, 400))

        self.editar_botao = QPushButton("editar", self)
        self.editar_botao.setGeometry(QRect(110, 510, 290, 41))

        self.deletar_botao = QPushButton("deletar", self)
        self.deletar_botao.setGeometry(QRect(400, 510, 290, 41))

        self.voltar_shadow = QGraphicsDropShadowEffect()
        self.filtros_shadow = QGraphicsDropShadowEffect()
        self.editar_shadow = QGraphicsDropShadowEffect()
        self.deletar_shadow = QGraphicsDropShadowEffect()

    def _set_style(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.flashcards_label.setStyleSheet("font: 16pt;")

        style_button(button=self.voltar_botao, shadow=self.voltar_shadow, cor="cinza", tam_fonte="12", tam_border_radius="10")
        style_button(button=self.filtros_botao, shadow=self.filtros_shadow, cor="cinza", tam_fonte="12", tam_border_radius="10")
        style_button(button=self.editar_botao, shadow=self.editar_shadow, cor="azul", tam_fonte="13", tam_border_radius="5")
        style_button(button=self.deletar_botao, shadow=self.deletar_shadow, cor="vermelho", tam_fonte="13", tam_border_radius="5")

    def _createSetTexts(self):
        self._setTexts["flashcards_lista"] = self.flashcards_lista.addItem

    def _createGetTexts(self):
        self._getTexts["flashcards_lista"] = self.getText_flashcards

    def _createConnects(self):
        self._connects["voltar_botao"] = self.voltar_botao.clicked.connect
        self._connects["filtros_botao"] = self.filtros_botao.clicked.connect
        self._connects["editar_botao"] = self.editar_botao.clicked.connect
        self._connects["deletar_botao"] = self.deletar_botao.clicked.connect

    def _createSetClears(self):
        self._clears["flashcards_lista"] = self.flashcards_lista.clear

    def getText_flashcards(self):
        current_item = self.flashcards_lista.currentItem()
        if current_item:
            return current_item.text()
        return ""


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaFlashcards()
    app.show()
    sys.exit(root.exec_())
