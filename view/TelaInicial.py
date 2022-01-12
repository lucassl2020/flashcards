from PyQt5.QtWidgets import QApplication, QWidget

import sys

from view.Widgets import button
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaInicial(QWidget):
    def __init__(self, parent=None):
        super(TelaInicial, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(350, 620)
        self.setWindowTitle("Inicio")
 

    def _create_widgets(self):
        self.rotina_botao = button(self, "Rotina", 20, 30, 310, 60)
        self.revisoes_botao = button(self, "Revisões", 20, 130, 310, 60)
        self.criar_rotina_botao = button(self, "Criar rotina", 20, 230, 310, 60)
        self.criar_flashcards_botao = button(self, "Criar flashcards", 20, 330, 310, 60)
        self.flashcards_botao = button(self, "Flashcards", 20, 430, 310, 60)
        self.historico_botao = button(self, "Histórico", 20, 530, 310, 60)
        

    def _set_style(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        style_button(button=self.rotina_botao, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.revisoes_botao, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.criar_rotina_botao, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.criar_flashcards_botao, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.flashcards_botao, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.historico_botao, cor="cinza_escuro", tam_fonte="14", border_radius=(5, 5, 5, 5), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.rotina_botao.clicked.connect(self.botaoRotina)
        self.revisoes_botao.clicked.connect(self.botaoRevisoes)
        self.criar_rotina_botao.clicked.connect(self.botaoCriarRotina)
        self.criar_flashcards_botao.clicked.connect(self.botaoCriarFlashcards)
        self.flashcards_botao.clicked.connect(self.botaoFlashcards)
        self.historico_botao.clicked.connect(self.botaoHistorico)
    

    def botaoRevisoes(self):
        event = {"codigo": 0, "descricao": "Botão REVISOES da tela INICIAL"}
        self.subject.notify(event)

    def botaoCriarFlashcards(self):
        event = {"codigo": 1, "descricao": "Botão CRIAR FLASHCARDS da tela INICIAL"}
        self.subject.notify(event)

    def botaoFlashcards(self):
        event = {"codigo": 2, "descricao": "Botão FLASHCARDS da tela INICIAL"}
        self.subject.notify(event)

    def botaoRotina(self):
        event = {"codigo": 24, "descricao": "Botão ROTINA da tela INICIAL"}
        self.subject.notify(event)

    def botaoCriarRotina(self):
        event = {"codigo": 25, "descricao": "Botão CRIAR ROTINA da tela INICIAL"}
        self.subject.notify(event)

    def botaoHistorico(self):
        event = {"codigo": 33, "descricao": "Botão HISTÓRICO da tela INICIAL"}
        self.subject.notify(event)

        
if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaInicial()
    app.show()
    sys.exit(root.exec_())
