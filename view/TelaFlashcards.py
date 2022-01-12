from PyQt5.QtWidgets import QApplication, QWidget

import sys

from view.Widgets import button, label, listWidget
from view.StyleButton import style_button

from model.Observer import ISubject

class TelaFlashcards(QWidget):
    def __init__(self, parent=None):
        super(TelaFlashcards, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("flashcards")
 

    def _create_widgets(self):
        self.voltar_botao = button(self, "Voltar", 20, 20, 90, 40)

        self.flashcards_label = label(self, "Flashcards", 350, 80, 100, 30)

        self.flashcards_lista = listWidget(self, 110, 110, 580, 400)

        self.editar_botao = button(self, "Editar", 110, 510, 290, 51)

        self.deletar_botao = button(self, "Deletar", 400, 510, 290, 51)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.flashcards_label.setStyleSheet("color: rgb(210, 210, 210);font: 16pt;")
        self.flashcards_lista.setStyleSheet('''color: rgb(210, 210, 210); 
                                            border: 1px solid; 
                                            border-top-left-radius: 4px; 
                                            border-top-right-radius: 4px; 
                                            border-color: rgb(84, 84, 84);
                                            font: 14px''')

        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.editar_botao, cor="azul", tam_fonte="13", border_radius=(0, 0, 5, 0), border_color="(123, 166, 205)")
        style_button(button=self.deletar_botao, cor="vermelho", tam_fonte="13", border_radius=(0, 0, 0, 5), border_color="(205, 123, 123)")


    def _setConnects(self):
        self.voltar_botao.clicked.connect(self.botaoVoltar)
        self.editar_botao.clicked.connect(self.botaoEditar)
        self.deletar_botao.clicked.connect(self.botaoDeletar)


    def clear(self):
        self.flashcards_lista.clear()


    def botaoVoltar(self):
        event = {"codigo": 10, "descricao": "Botão VOLTAR da tela FLASHCARDS"}
        self.subject.notify(event)


    def botaoEditar(self):
        if self.flashcards_lista.currentItem():
            event = {"codigo": 11, "descricao": "Botão EDITAR da tela FLASHCARDS"}
            self.subject.notify(event)


    def botaoDeletar(self):
        if self.flashcards_lista.currentItem():
            event = {"codigo": 12, "descricao": "Botão DELETAR da tela FLASHCARDS"}
            self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaFlashcards()
    app.show()
    sys.exit(root.exec_())
