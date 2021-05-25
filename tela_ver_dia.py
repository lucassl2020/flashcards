from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect, QLabel, QListWidget
from PyQt5.QtCore import Qt, QRect
import sys
from Suporte import style_button, SetInterface


class TelaVerDia(QWidget, SetInterface):
    def __init__(self, parent=None):
        super(TelaVerDia, self).__init__(parent)
        self._settings()
        self._create_widgets()
        self._set_style()
        self._setTexts()
        self._setConnects()

    def _settings(self):
        self.resize(800, 600)
        self.setWindowTitle("Ver dia")
 
    def _create_widgets(self):
        self.voltar_botao = QPushButton("voltar", self)
        self.voltar_botao.setGeometry(QRect(20, 20, 90, 40))

        self.revisoes_atrasadas_label = QLabel("revisões atrasadas", self)
        self.revisoes_atrasadas_label.setGeometry(QRect(100, 170, 100, 30))

        self.revisoes_do_dia_label = QLabel("revisões do dia", self)
        self.revisoes_do_dia_label.setGeometry(QRect(405, 170, 100, 30))

        self.revisoes_atrasadas_lista = QListWidget(self)
        self.revisoes_atrasadas_lista.setGeometry(QRect(95, 200, 300, 240))

        self.revisoes_do_dia_lista = QListWidget(self)
        self.revisoes_do_dia_lista.setGeometry(QRect(400, 200, 300, 240))

        self.revisar_atrasado_botao = QPushButton("revisar atrasado", self)
        self.revisar_atrasado_botao.setGeometry(QRect(95, 440, 301, 41))

        self.revisar_atual_botao = QPushButton("revisar atual", self)
        self.revisar_atual_botao.setGeometry(QRect(400, 440, 301, 41))

        self.voltar_shadow = QGraphicsDropShadowEffect()
        self.revisar_atrasado_shadow = QGraphicsDropShadowEffect()
        self.revisar_atual_shadow = QGraphicsDropShadowEffect()

    def _set_style(self):
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        style_button(button=self.voltar_botao, shadow=self.voltar_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_borda="10")
        style_button(button=self.revisar_atrasado_botao, shadow=self.revisar_atrasado_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_borda="5")
        style_button(button=self.revisar_atual_botao, shadow=self.revisar_atual_shadow, cor="(235, 235, 235)", tam_fonte="10", tam_borda="5")

    def _setTexts(self):
        pass

    def _setConnects(self):
        self._connects["voltar_botao"] = self.voltar_botao.clicked.connect
        self._connects["revisar_atrasado_botao"] = self.revisar_atrasado_botao.clicked.connect
        self._connects["revisar_atual_botao"] = self.revisar_atual_botao.clicked.connect


if __name__ == '__main__':
    root = QApplication(sys.argv)
    app = TelaVerDia()
    app.show()
    sys.exit(root.exec_())
