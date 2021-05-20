from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QGraphicsDropShadowEffect, QTextEdit
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import sys


class TelaRevisao(QWidget):
    def __init__(self, parent=None):
        super(TelaRevisao, self).__init__(parent)
        self.titulo = None
        self.settings()
        self.create_widgets()
        self.set_layout()
        self.set_style()

    def settings(self):
        self.resize(800, 400)
        self.setWindowTitle("Revisão")
 
    def create_widgets(self):
        self.ver_resposta_botao = QPushButton("ver resposta")
        self.ver_pergunta_botao = QPushButton("ver pergunta")
        self.acertei_botao = QPushButton("acertei")
        self.errei_botao = QPushButton("errei")
        self.cancelar_botao = QPushButton("cancelar")

        self.ver_resposta_shadow = QGraphicsDropShadowEffect()
        self.ver_pergunta_shadow = QGraphicsDropShadowEffect()
        self.acertei_shadow = QGraphicsDropShadowEffect()
        self.errei_shadow = QGraphicsDropShadowEffect()
        self.cancelar_shadow = QGraphicsDropShadowEffect()

        self.texto = QTextEdit()

    def set_layout(self):
        self.gridLayout = QGridLayout()
        
        self.gridLayout.addWidget(self.texto, 2, 1)
        self.gridLayout.addWidget(self.ver_pergunta_botao, 0, 0)
        self.gridLayout.addWidget(self.ver_resposta_botao, 1, 0)
        self.gridLayout.addWidget(self.acertei_botao, 0, 1)
        self.gridLayout.addWidget(self.errei_botao, 1, 1)
        self.gridLayout.addWidget(self.cancelar_botao, 0, 2)

        self.setLayout(self.gridLayout)

    def set_style(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        def style_button(button, shadow):
            button.setStyleSheet('''
                                        QPushButton{ 
                                            font: 10pt;
                                            height: 50px;
                                            width: 80px;
                                            background-color: rgb(235, 235, 235);
                                            color: rgb(50, 50, 50);
                                            border-radius: 10px;
                                            border-color: rgb(56, 56, 56)
                                        }

                                        QPushButton:hover{
                                            background-color: rgb(107, 107, 107);
                                            color: rgb(245, 245, 245);;
                                        }

                                        QPushButton:pressed{
                                            background-color: rgb(75, 75, 75);
                                            color: rgb(210, 210, 210);
                                        }
                                        ''')

            shadow.setXOffset(0)
            shadow.setYOffset(2)
            shadow.setBlurRadius(25)
            shadow.setColor(QColor (200, 200, 200))

            button.setGraphicsEffect(shadow) 

        style_button(self.ver_resposta_botao, self.ver_resposta_shadow)
        style_button(self.ver_pergunta_botao, self.ver_pergunta_shadow)
        style_button(self.acertei_botao, self.acertei_shadow)
        style_button(self.errei_botao, self.errei_shadow)
        style_button(self.cancelar_botao, self.cancelar_shadow)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaRevisao()
    app.show()
    sys.exit(root.exec_())
