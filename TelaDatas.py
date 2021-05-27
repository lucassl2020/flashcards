from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect, QLabel, QCalendarWidget, QListWidget
from PyQt5.QtCore import Qt, QRect
import sys
from Suporte import style_button, SetInterface


class TelaDatas(QWidget, SetInterface):
    def __init__(self, parent=None):
        super(TelaDatas, self).__init__(parent)
        self._settings()
        self._createWidgets()
        self._setStyle()
        self._createSetTexts()
        self._createGetTexts()
        self._createConnects()
        self._createSetClears()

    def _settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Datas")
 
    def _createWidgets(self):
        self.adicione_datas = QLabel("Adicione datas para revisão", self)
        self.adicione_datas.setGeometry(QRect(0, 20, 800, 20))
        self.adicione_datas.setAlignment(Qt.AlignCenter)

        self.calendario_widget = QCalendarWidget(self)
        self.calendario_widget.setGeometry(QRect(90, 140, 320, 191))

        self.datas_listwidget = QListWidget(self)
        self.datas_listwidget.setGeometry(QRect(450, 140, 260, 192))

        self.adicionar_botao = QPushButton("adicionar", self)
        self.adicionar_botao.setGeometry(QRect(90, 332, 321, 41))

        self.remover_botao = QPushButton("remover", self)
        self.remover_botao.setGeometry(QRect(450, 332, 261, 41))

        self.finalizar_botao = QPushButton("finalizar", self)
        self.finalizar_botao.setGeometry(QRect(325, 500, 150, 41))

        self.adicionar_shadow = QGraphicsDropShadowEffect()
        self.remover_shadow = QGraphicsDropShadowEffect()
        self.finalizar_shadow = QGraphicsDropShadowEffect()

    def _setStyle(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.adicione_datas.setStyleSheet("font: 14pt;")

        self.calendario_widget.setStyleSheet("color: rgb(0, 0, 0);")
        
        style_button(button=self.adicionar_botao, shadow=self.adicionar_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_border_radius="5")
        style_button(button=self.remover_botao, shadow=self.remover_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_border_radius="5")
        style_button(button=self.finalizar_botao, shadow=self.finalizar_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_border_radius="5")

    def _createSetTexts(self):
        self._setTexts["datas_listwidget"] = self.datas_listwidget.addItem

    def _createGetTexts(self):
        self._getTexts["datas_listwidget"] = self.getText_datasListwidget

    def _createConnects(self):
        self._connects["adicionar_botao"] = self.adicionar_botao.clicked.connect
        self._connects["remover_botao"] = self.remover_botao.clicked.connect
        self._connects["finalizar_botao"] = self.finalizar_botao.clicked.connect

    def _createSetClears(self):
        self._clears["datas_listwidget"] = self.datas_listwidget.clear

    def setText_texto(self, texto):
        pass

    def getText_datasListwidget(self):
        current_item = self.datas_listwidget.currentItem()
        if current_item:
            return current_item.text()
        return ""


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaDatas()
    app.show()
    sys.exit(root.exec_())
