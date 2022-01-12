from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

import sys

from view.Widgets import button, label, textEdit, lineEdit, comboBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaCriarFlashcards(QWidget):
    def __init__(self, parent=None):
        super(TelaCriarFlashcards, self).__init__(parent)

        self.subject = ISubject()
        
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("Criar flashcards")
 

    def _create_widgets(self):
        self.titulo_label = label(self, "Titulo", 148, 30, 60, 25)

        self.titulo_line = lineEdit(self, 192, 30, 440, 25)

        self.pergunta_label = label(self, "Pergunta", 102, 90, 65, 25)

        self.resposta_label = label(self, "Resposta", 407, 90, 65, 25)

        self.pergunta_texto = textEdit(self, 97, 115, 300, 240)

        self.resposta_texto = textEdit(self, 402, 115, 300, 240)

        self.adicionar_botao = button(self, "Adicionar", 97, 355, 605, 50)

        self.flashcards_label = label(self, "Flashcards", 100, 440, 60, 25)

        self.flashcards_box = comboBox(tela=self, duplicates=False, maxCount=40, x=165, y=440, largura=350, altura=25)

        self.deletar_botao = button(self, "Deletar", 520, 430, 177, 40)

        self.definir_datas_botao = button(self, "Definir datas", 97, 510, 302, 50)

        self.cancelar_botao = button(self, "Cancelar", 400, 510, 302, 50)


    def _set_style(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.titulo_label.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")
        self.pergunta_label.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")
        self.resposta_label.setStyleSheet("color: rgb(210, 210, 210); font: 12pt;")
        self.flashcards_label.setStyleSheet("color: rgb(210, 210, 210); font: 10pt;")
  
        self.flashcards_box.setStyleSheet('''QComboBox{
                                            border-radius: 4px; 
                                            color: rgb(210, 210, 210);
                                            background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgba(210, 210, 210, 100), stop: 0 rgba(110, 110, 110, 100));
                                        }
                                        QComboBox QAbstractItemView{
                                            selection-background-color: rgb(34, 34, 34);
                                            color: rgb(210, 210, 210)
                                        }''')
        self.flashcards_box.setEditable(False)
        
        self.titulo_line.setStyleSheet('''color: rgb(210, 210, 210); 
                                        border: 1px solid; 
                                        border-radius: 4px; 
                                        border-color: rgb(84, 84, 84);
                                        font: 14px;''')
        self.pergunta_texto.setStyleSheet('''color: rgb(210, 210, 210); 
                                            border: 1px solid; 
                                            border-top-left-radius: 4px; 
                                            border-top-right-radius: 4px; 
                                            border-color: rgb(84, 84, 84);
                                            font: 14px;''')
        self.resposta_texto.setStyleSheet('''color: rgb(210, 210, 210); 
                                            border: 1px solid; 
                                            border-top-left-radius: 4px; 
                                            border-top-right-radius: 4px; 
                                            border: 1px solid; 
                                            border-color: rgb(84, 84, 84);
                                            font: 14px;''')

        style_button(button=self.adicionar_botao, cor="azul", tam_fonte="12", border_radius=(0, 0, 5, 5), border_color="(123, 166, 205)")
        style_button(button=self.deletar_botao, cor="vermelho", tam_fonte="12", border_radius=(5, 5, 5, 5), border_color="(205, 123, 123)")
        style_button(button=self.definir_datas_botao, cor="verde", tam_fonte="12", border_radius=(5, 0, 5, 0), border_color="(123, 205, 126)")
        style_button(button=self.cancelar_botao, cor="vermelho", tam_fonte="12", border_radius=(0, 5, 0, 5), border_color="(205, 123, 123)")


    def _setConnects(self):
        self.adicionar_botao.clicked.connect(self.botaoAdicionar)
        self.deletar_botao.clicked.connect(self.botaoDeletar)
        self.definir_datas_botao.clicked.connect(self.botaoDefinirDatas)
        self.cancelar_botao.clicked.connect(self.botaoCancelar)
        

    def clear(self, *widget_names):
        self.flashcards_box.clear()
        self.pergunta_texto.clear()
        self.resposta_texto.clear()
        self.titulo_line.clear()

    
    def botaoAdicionar(self):
        event = {"codigo": 6, "descricao": "Botão ADICIONAR da tela CRIAR FLASHCARDS"}
        self.subject.notify(event)


    def botaoDeletar(self):
        event = {"codigo": 7, "descricao": "Botão DELETAR da tela CRIAR FLASHCARDS"}
        self.subject.notify(event)


    def botaoDefinirDatas(self):
        event = {"codigo": 8, "descricao": "Botão DEFINIR DATAS da tela CRIAR FLASHCARDS"}
        self.subject.notify(event)


    def botaoCancelar(self):
        event = {"codigo": 9, "descricao": "Botão CANCELAR da tela CRIAR FLASHCARDS"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaCriarFlashcards()
    app.show()
    sys.exit(root.exec_())
