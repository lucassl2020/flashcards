from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QGraphicsDropShadowEffect, QLabel, QListWidget
from PyQt5.QtGui import QColor
import sys


class TelaVerDia(QWidget):
    def __init__(self, parent=None):
        super(TelaVerDia, self).__init__(parent)
        self.settings()
        self.create_widgets()
        self.set_layout()
        self.set_style()

    def settings(self):
        self.resize(800, 400)
        self.setWindowTitle("Ver dia")
 
    def create_widgets(self):
        self.voltar_botao = QPushButton("voltar")
        self.revisar_atrasado_botao = QPushButton("revisar atrasado")
        self.revisar_atual_botao = QPushButton("revisar atual")

        self.voltar_shadow = QGraphicsDropShadowEffect()
        self.revisar_atrasado_shadow = QGraphicsDropShadowEffect()
        self.revisar_atual_shadow = QGraphicsDropShadowEffect()

        self.revisoes_atrasadas_label = QLabel("Revisões atrasadas")
        self.revisoes_do_dia_label = QLabel("Revisões do dia")

        self.revisoes_atrasadas_lista = QListWidget()
        self.revisoes_do_dia_lista = QListWidget()

        self.salvar_botao = QPushButton("salvar")

    def set_layout(self):
        self.gridLayout = QGridLayout()
        
        self.gridLayout.addWidget(self.voltar_botao, 0, 0)
        self.gridLayout.addWidget(self.revisoes_atrasadas_label, 1, 0)
        self.gridLayout.addWidget(self.revisoes_do_dia_label, 1, 1)
        self.gridLayout.addWidget(self.revisoes_atrasadas_lista, 2, 0)
        self.gridLayout.addWidget(self.revisoes_do_dia_lista, 2, 1)
        self.gridLayout.addWidget(self.revisar_atrasado_botao, 3, 0)
        self.gridLayout.addWidget(self.revisar_atual_botao, 3, 1)

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

        style_button(self.voltar_botao, self.voltar_shadow)
        style_button(self.revisar_atrasado_botao, self.revisar_atrasado_shadow)
        style_button(self.revisar_atual_botao, self.revisar_atual_shadow)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaVerDia()
    app.show()
    sys.exit(root.exec_())
