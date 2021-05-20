from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QGraphicsDropShadowEffect, QTextEdit, QLabel, QComboBox, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QColor
import sys


class TelaCriarFlashcards(QWidget):
    def __init__(self, parent=None):
        super(TelaCriarFlashcards, self).__init__(parent)
        self.settings()
        self.create_widgets()
        self.set_layout()
        self.set_style()

    def settings(self):
        self.resize(800, 400)
        self.setWindowTitle("Criar flashcards")
 
    def create_widgets(self):
        self.flashcards_label = QLabel("flashcards")
        self.flashcards_box = QComboBox()
        self.flashcards_box.setDuplicatesEnabled(False)
        self.flashcards_box.setMaxCount(40)

        self.salvar_botao = QPushButton("salvar")
        self.deletar_botao = QPushButton("deletar")
        self.finalizar_botao = QPushButton("finalizar")
        self.cancelar_botao = QPushButton("cancelar")

        self.salvar_shadow = QGraphicsDropShadowEffect() 
        self.deletar_shadow = QGraphicsDropShadowEffect()
        self.finalizar_shadow = QGraphicsDropShadowEffect()  
        self.cancelar_shadow = QGraphicsDropShadowEffect()  

        self.pergunta_label = QLabel("pergunta")
        self.resposta_label = QLabel("resposta")

        self.pergunta_texto = QTextEdit()
        self.resposta_texto = QTextEdit()
        
        self.titulo_label = QLabel("titulo")
        self.titulo_line = QLineEdit()

    def set_layout(self):
        self.gridLayout = QGridLayout()
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_2 = QHBoxLayout()
        self.verticalLayout = QVBoxLayout()

        self.horizontalLayout_1.addWidget(self.titulo_label)
        self.horizontalLayout_1.addWidget(self.titulo_line)
        self.horizontalLayout_2.addWidget(self.flashcards_label)
        self.horizontalLayout_2.addWidget(self.flashcards_box)
        self.horizontalLayout_2.addWidget(self.deletar_botao)
        
        self.gridLayout.addWidget(self.pergunta_label, 3, 0)
        self.gridLayout.addWidget(self.resposta_label, 3, 2)
        self.gridLayout.addWidget(self.pergunta_texto, 4, 0)
        self.gridLayout.addWidget(self.salvar_botao, 4, 1)
        self.gridLayout.addWidget(self.resposta_texto, 4, 2)
        self.gridLayout.addWidget(self.finalizar_botao, 5, 0)
        self.gridLayout.addWidget(self.cancelar_botao, 5, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.setLayout(self.verticalLayout)

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

        style_button(self.salvar_botao, self.salvar_shadow)
        style_button(self.deletar_botao, self.deletar_shadow)
        style_button(self.finalizar_botao, self.finalizar_shadow)
        style_button(self.cancelar_botao, self.cancelar_shadow)

        self.flashcards_box.setStyleSheet("height: 30px;")

    def clear(self):
        self.flashcards_box.clear()
        self.pergunta_texto.setText("")
        self.resposta_texto.setText("")
        self.titulo_line.setText("")


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaCriarFlashcards()
    app.show()
    sys.exit(root.exec_())
