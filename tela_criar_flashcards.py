from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect, QTextEdit, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import Qt, QRect
import sys
from Suporte import style_button, SetInterface


class TelaCriarFlashcards(QWidget, SetInterface):
    def __init__(self, parent=None):
        super(TelaCriarFlashcards, self).__init__(parent)
        self._settings()
        self._create_widgets()
        self._set_style()
        self._createSetTexts()
        self._createGetTexts()
        self._createConnects()
        self._createSetClears()

    def _settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Criar flashcards")
 
    def _create_widgets(self):
        self.titulo_label = QLabel("titulo", self)
        self.titulo_label.setGeometry(QRect(150, 20, 60, 25))

        self.titulo_line = QLineEdit(self)
        self.titulo_line.setGeometry(QRect(190, 20, 440, 25))

        self.pergunta_label = QLabel("pergunta", self)
        self.pergunta_label.setGeometry(QRect(102, 90, 60, 25))

        self.resposta_label = QLabel("resposta", self)
        self.resposta_label.setGeometry(QRect(407, 90, 60, 25))

        self.pergunta_texto = QTextEdit(self)
        self.pergunta_texto.setGeometry(QRect(97, 115, 300, 240))

        self.resposta_texto = QTextEdit(self)
        self.resposta_texto.setGeometry(QRect(402, 115, 300, 240))

        self.adicionar_botao = QPushButton("adicionar", self)
        self.adicionar_botao.setGeometry(QRect(97, 355, 605, 50))

        self.flashcards_label = QLabel("flashcards", self)
        self.flashcards_label.setGeometry(QRect(100, 440, 60, 25))

        self.flashcards_box = QComboBox(self)
        self.flashcards_box.setDuplicatesEnabled(False)
        self.flashcards_box.setMaxCount(40)
        self.flashcards_box.setGeometry(QRect(160, 440, 350, 25))

        self.deletar_botao = QPushButton("deletar", self)
        self.deletar_botao.setGeometry(QRect(520, 430, 177, 40))

        self.salvar_botao = QPushButton("salvar", self)
        self.salvar_botao.setGeometry(QRect(97, 510, 302, 50))

        self.cancelar_botao = QPushButton("cancelar", self)
        self.cancelar_botao.setGeometry(QRect(400, 510, 302, 50))

        self.adicionar_shadow = QGraphicsDropShadowEffect() 
        self.deletar_shadow = QGraphicsDropShadowEffect()
        self.salvar_shadow = QGraphicsDropShadowEffect()  
        self.cancelar_shadow = QGraphicsDropShadowEffect() 

    def _set_style(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.titulo_label.setStyleSheet("font: 11pt;")

        style_button(button=self.adicionar_botao, shadow=self.adicionar_shadow, cor="(120, 180, 255)", tam_fonte="10", tam_border_radius="5")
        style_button(button=self.deletar_botao, shadow=self.deletar_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_border_radius="5")
        style_button(button=self.salvar_botao, shadow=self.salvar_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_border_radius="5")
        style_button(button=self.cancelar_botao, shadow=self.cancelar_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_border_radius="5")

    def _createSetTexts(self):
        pass

    def _createGetTexts(self):
        self._getTexts["titulo_line"] = self.titulo_line.text
        self._getTexts["pergunta_texto"] = self.pergunta_texto.toPlainText
        self._getTexts["resposta_texto"] = self.resposta_texto.toPlainText
        self._getTexts["flashcards_box"] = self.flashcards_box.currentText
        
    def _createConnects(self):
        self._connects["adicionar_botao"] = self.adicionar_botao.clicked.connect
        self._connects["deletar_botao"] = self.deletar_botao.clicked.connect
        self._connects["salvar_botao"] = self.salvar_botao.clicked.connect
        self._connects["cancelar_botao"] = self.cancelar_botao.clicked.connect

    def _createSetClears(self):
        self._clears["flashcards_box"] = self.flashcards_box.clear
        self._clears["pergunta_texto"] = self.pergunta_texto.clear
        self._clears["resposta_texto"] = self.resposta_texto.clear
        self._clears["titulo_line"] = self.titulo_line.clear


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaCriarFlashcards()
    app.show()
    sys.exit(root.exec_())
