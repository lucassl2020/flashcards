from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QDate

import sys

from view.Widgets import button, label, listWidget, comboBox, lineEdit
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaCriarRotina(QWidget):
    def __init__(self, parent=None):
        super(TelaCriarRotina, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._createWidgets()
        self._setStyle()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(610, 492)
        self.setWindowTitle("Criar rotina")


    def _createWidgets(self):
        self.voltar_botao = button(self, "Voltar", 20, 20, 90, 40)

        self.dia_atividades = label(self, "Dia:", 160, 80, 50, 20) 
        self.dias_box = comboBox(tela=self, duplicates=False, maxCount=7, x=195, y=80, largura=265, altura=25)

        self.remover_botao = button(self, "Remover", 160, 327, 300, 35)

        self.adicionar_botao = button(self, "Adicionar", 160, 422, 300, 30)

        self.atividades_listwidget = listWidget(self, 160, 135, 300, 192)

        self.atividade_line = lineEdit(self, 160, 392, 300, 30)


    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.dia_atividades.setStyleSheet("color: rgb(210, 210, 210); font: 14pt;")
        self.dias_box.setStyleSheet('''QComboBox{
                                            border-radius: 4px; 
                                            color: rgb(210, 210, 210);
                                            background-color: qlineargradient(x1:0, y1:0, x2:1,y2:1, stop: 1 rgba(210, 210, 210, 100), stop: 0 rgba(110, 110, 110, 100));
                                            font: 14px;
                                        }
                                        QComboBox QAbstractItemView{
                                            selection-background-color: rgb(34, 34, 34);
                                            color: rgb(210, 210, 210)
                                        }''')
        self.dias_box.setEditable(False)
        self.atividades_listwidget.setStyleSheet('''color: rgb(210, 210, 210); 
                                            border: 1px solid; 
                                            border-top-left-radius: 4px; 
                                            border-top-right-radius: 4px; 
                                            border-color: rgb(84, 84, 84);
                                            font: 14px;''')

        self.atividade_line.setStyleSheet('''color: rgb(210, 210, 210); 
                                        border: 1px solid; 
                                        border-top-left-radius: 4px; 
                                        border-top-right-radius: 4px; 
                                        border-color: rgb(84, 84, 84);
                                        font: 14px''')        
        
        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")
        style_button(button=self.adicionar_botao, cor="verde", tam_fonte="12", border_radius=(0, 0, 5, 5), border_color="(123, 205, 126)")
        style_button(button=self.remover_botao, cor="vermelho", tam_fonte="12", border_radius=(0, 0, 5, 5), border_color="(205, 123, 123)")


    def _setConnects(self):
        self.voltar_botao.clicked.connect(self.botaoVoltar)
        self.adicionar_botao.clicked.connect(self.botaoAdicionar)
        self.remover_botao.clicked.connect(self.botaoRemover)
        self.dias_box.currentTextChanged.connect(self.comboBoxMudouValor)


    def clear(self):
        self.dias_box.clear()
        self.atividades_listwidget.clear()
        self.atividade_line.clear()


    def botaoVoltar(self):
        event = {"codigo": 26, "descricao": "Botão VOLTAR da tela CRIAR ROTINA"}
        self.subject.notify(event)


    def botaoAdicionar(self):
        if self.atividade_line.text():
            event = {"codigo": 27, "descricao": "Botão ADICIONAR da tela CRIAR ROTINA"}
            self.subject.notify(event)


    def botaoRemover(self):
        if self.atividades_listwidget.currentItem():
            event = {"codigo": 28, "descricao": "Botão REMOVER da tela CRIAR ROTINA"}
            self.subject.notify(event)


    def comboBoxMudouValor(self):
        event = {"codigo": 29, "descricao": "combo box DIAS da tela CRIAR ROTINA"}
        self.subject.notify(event)


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaCriarRotina()
    app.show()
    sys.exit(root.exec_())
