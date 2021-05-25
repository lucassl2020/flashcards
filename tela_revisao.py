from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QGraphicsDropShadowEffect, QTextEdit, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QRect
import sys


class TelaRevisao(QWidget):
    def __init__(self, parent=None):
        super(TelaRevisao, self).__init__(parent)
        self.titulo = None
        self.texts = {}
        self.connects = {}

        self.settings()
        self.createWidgets()
        self.setStyle()
        self.setTexts()
        self.setConnects()

    def settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Revisão")
 
    def createWidgets(self):
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

    def setStyle(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.pergunta_ou_resposta.setStyleSheet("font: 14pt;")

        self.texto.setStyleSheet("font: 12pt;")

        def style_button(button, shadow, cor, borda):
            button.setStyleSheet("QPushButton{\n"
                                    "font: 10pt;\n"
                                    "background-color: rgb" + cor + ";\n"
                                    "color: rgb(50, 50, 50);\n"
                                    "border-radius: " + borda + "px;\n"
                                    "border-color: rgb(56, 56, 56)\n"
                                "}\n"

                                "QPushButton:hover{\n"
                                    "background-color: rgb(107, 107, 107);\n"
                                    "color: rgb(245, 245, 245);\n"
                                "}\n"

                                "QPushButton:pressed{\n"
                                    "background-color: rgb(75, 75, 75);\n"
                                    "color: rgb(210, 210, 210);\n"
                                "}")

            shadow.setXOffset(0)
            shadow.setYOffset(2)
            shadow.setBlurRadius(25)
            shadow.setColor(QColor (200, 200, 200))

            button.setGraphicsEffect(shadow) 

        style_button(self.anterior_botao, self.anterior_shadow, "(235, 235, 235)", "20")
        style_button(self.proximo_botao, self.proximo_shadow, "(235, 235, 235)", "20")
        style_button(self.acertei_botao, self.acertei_shadow, "(156, 255, 176)", "5")
        style_button(self.errei_botao, self.errei_shadow, "(255, 135, 135)", "5")
        style_button(self.voltar_botao, self.voltar_shadow, "(235, 235, 235)", "10")

    def setTexts(self):
        self.texts["pergunta_ou_resposta"] = self.pergunta_ou_resposta.setText
        self.texts["texto"] = self.setText_texto

    def setConnects(self):
        self.connects["anterior_botao"] = self.anterior_botao.clicked.connect
        self.connects["proximo_botao"] = self.proximo_botao.clicked.connect
        self.connects["acertei_botao"] = self.acertei_botao.clicked.connect
        self.connects["errei_botao"] = self.errei_botao.clicked.connect
        self.connects["voltar_botao"] = self.voltar_botao.clicked.connect

    def setText(self, widget_name, texto):
        try:
            func = self.texts[widget_name]
            func(texto)
        except:
            print("ERRO: " + widget_name + " nao existe")

    def setConnect(self, widget_name, funcao):
        try:
            func = self.connects[widget_name]
            func(funcao)
        except:
            print("ERRO: " + widget_name + " nao existe")

    def setText_texto(self, texto):
        self.texto.setText(texto)
        self.texto.setAlignment(Qt.AlignJustify)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaRevisao()
    app.show()
    sys.exit(root.exec_())
