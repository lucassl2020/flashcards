from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import sys


class TelaInicial(QWidget):
    def __init__(self, parent=None):
        super(TelaInicial, self).__init__(parent)
        self.settings()
        self.create_widgets()
        self.set_layout()
        self.set_style()

    def settings(self):
        self.resize(350, 300)
        self.setWindowTitle("Inicio")
 
    def create_widgets(self):
        self.ver_dia_botao = QPushButton("ver dia")
        self.criar_flashcards_botao = QPushButton("criar flashcards")

        self.ver_dia_shadow = QGraphicsDropShadowEffect() 
        self.criar_flashcards_shadow = QGraphicsDropShadowEffect() 

    def set_layout(self):
        self.gridLayout = QGridLayout()

        self.gridLayout.addWidget(self.ver_dia_botao, 0, 0)
        self.gridLayout.addWidget(self.criar_flashcards_botao, 1, 0)

        self.setLayout(self.gridLayout)

    def set_style(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        def style_button(button, shadow):
            button.setStyleSheet('''
                                        QPushButton{ 
                                            font: 14pt;
                                            height: 50%;
                                            background-color: rgb(235, 235, 235);
                                            color: rgb(75, 75, 75);
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

        style_button(self.ver_dia_botao, self.ver_dia_shadow)
        style_button(self.criar_flashcards_botao, self.criar_flashcards_shadow)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaInicial()
    app.show()
    sys.exit(root.exec_())
