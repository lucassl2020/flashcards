from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListWidgetItem
from PyQt5.QtCore import Qt

import sys

from view.Widgets import button, label, listWidget, comboBox
from view.StyleButton import style_button

from model.Observer import ISubject


class TelaRotina(QWidget):
    def __init__(self, parent=None):
        super(TelaRotina, self).__init__(parent)

        self.subject = ISubject()

        self._settings()
        self._createWidgets()
        self._setStyle()
        self._setConnects()


    def _settings(self):
        self.setFixedSize(610, 490)
        self.setWindowTitle("Rotina")


    def _createWidgets(self):
        self.voltar_botao = button(self, "Voltar", 20, 20, 90, 40)

        self.atividades = label(self, "", 160, 110, 300, 20) 
        self.atividades.setAlignment(Qt.AlignCenter)

        self.atividades_listwidget = listWidget(self, 160, 135, 300, 250)


    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.atividades.setStyleSheet("color: rgb(210, 210, 210); font: 14pt;")

        self.atividades_listwidget.setStyleSheet('''color: rgb(210, 210, 210); 
                                            border: 1px solid; 
                                            border-top-left-radius: 4px; 
                                            border-top-right-radius: 4px; 
                                            border-color: rgb(84, 84, 84);
                                            font: 14px''')   
        
        style_button(button=self.voltar_botao, cor="cinza_escuro", tam_fonte="12", border_radius=(10, 10, 10, 10), rgb_da_letra="(210, 210, 210)")


    def _setConnects(self):
        self.voltar_botao.clicked.connect(self.botaoVoltar)
        self.atividades_listwidget.itemChanged.connect(self.listaCheckbox)


    def clear(self):
        self.atividades_listwidget.clear()


    def botaoVoltar(self):
        event = {"codigo": 30, "descricao": "Botão VOLTAR da tela ROTINA"}
        self.subject.notify(event)


    def listaCheckbox(self):
        event = {"codigo": 31, "descricao": "lista checkbox ATIVIDADES da tela ROTINA"}
        self.subject.notify(event)


    def adicionarCheckBox(self, titulo, state):
        item = QListWidgetItem(titulo)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)

        if state:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)

        self.atividades_listwidget.addItem(item)

        return item


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaRotina()
    app.show()
    sys.exit(root.exec_())
