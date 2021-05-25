from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect, QTextEdit, QLabel
from PyQt5.QtCore import Qt, QRect
import sys
from Suporte import style_button, SetInterface


class TelaRevisao(QWidget, SetInterface):
    def __init__(self, parent=None):
        super(TelaRevisao, self).__init__(parent)
        self.titulo = None
        self._texts = {}

        self._settings()
        self._createWidgets()
        self._setStyle()
        self._setTexts()
        self._setConnects()

    def _settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Revisão")
 
    def _createWidgets(self):
        self.pergunta_ou_resposta = QLabel("pergunta", self)
        self.pergunta_ou_resposta.setGeometry(QRect(350, 85, 100, 30))
        self.pergunta_ou_resposta.setAlignment(Qt.AlignCenter)

        self.anterior_botao = QPushButton("<", self)
        self.anterior_botao.setGeometry(QRect(100, 300, 40, 40))

        self.proximo_botao = QPushButton(">", self)
        self.proximo_botao.setGeometry(QRect(660, 300, 40, 40))

        self.acertei_botao = QPushButton("acertei", self)
        self.acertei_botao.setGeometry(QRect(150, 470, 250, 50))

        self.errei_botao = QPushButton("errei", self)
        self.errei_botao.setGeometry(QRect(400, 470, 250, 50))

        self.voltar_botao = QPushButton("voltar", self)
        self.voltar_botao.setGeometry(QRect(20, 20, 90, 40))

        self.anterior_shadow = QGraphicsDropShadowEffect()
        self.proximo_shadow = QGraphicsDropShadowEffect()
        self.acertei_shadow = QGraphicsDropShadowEffect()
        self.errei_shadow = QGraphicsDropShadowEffect()
        self.voltar_shadow = QGraphicsDropShadowEffect()

        self.texto = QTextEdit(self)
        self.texto.setGeometry(QRect(150, 120, 500, 350))

    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.pergunta_ou_resposta.setStyleSheet("font: 14pt;")

        self.texto.setStyleSheet("font: 12pt;")

        style_button(button=self.anterior_botao, shadow=self.anterior_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_borda="20")
        style_button(button=self.proximo_botao, shadow=self.proximo_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_borda="20")
        style_button(button=self.acertei_botao, shadow=self.acertei_shadow, cor="(156, 255, 176)", tam_fonte="10", tam_borda="5")
        style_button(button=self.errei_botao, shadow=self.errei_shadow, cor="(255, 135, 135)", tam_fonte="10", tam_borda="5")
        style_button(button=self.voltar_botao, shadow=self.voltar_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_borda="10")

    def _setTexts(self):
        self._texts["pergunta_ou_resposta"] = self.pergunta_ou_resposta.setText
        self._texts["texto"] = self.setText_texto

    def _setConnects(self):
        self._connects["anterior_botao"] = self.anterior_botao.clicked.connect
        self._connects["proximo_botao"] = self.proximo_botao.clicked.connect
        self._connects["acertei_botao"] = self.acertei_botao.clicked.connect
        self._connects["errei_botao"] = self.errei_botao.clicked.connect
        self._connects["voltar_botao"] = self.voltar_botao.clicked.connect

    def setText_texto(self, texto):
        self.texto.setText(texto)
        self.texto.setAlignment(Qt.AlignJustify)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaRevisao()
    app.show()
    sys.exit(root.exec_())
