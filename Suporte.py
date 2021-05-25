from PyQt5.QtGui import QColor
import abc

class SetInterface():
    def __init__(self):
        self._texts = {}
        self._connects = {}

    @abc.abstractmethod
    def _setTexts(self):
        pass

    @abc.abstractmethod
    def _setConnects(self):
        pass

    def setText(self, widget_name, texto):
        func = self._texts[widget_name]
        func(texto)

    def setConnect(self, widget_name, funcao):
        func = self._connects[widget_name]
        func(funcao)


def style_button(button, shadow, cor, tam_fonte, tam_borda):
    button.setStyleSheet("QPushButton{\n"
                                "font: " + tam_fonte + "pt;\n"
                                "background-color: rgb" + cor + ";\n"
                                 "color: rgb(50, 50, 50);\n"
                                "border-radius: " + tam_borda + "px;\n"
                                "border-color: rgb(56, 56, 56)\n"
                            "}\n"

                            "QPushButton:hover{\n"
                                "background-color: rgb(107, 107, 107);\n"
                                "color: rgb(245, 245, 245);\n"
                            "}\n"

                            "QPushButton:pressed{\n"
                                "background-color: rgb(75, 75, 75);\n"
                                "color: rgb(210, 210, 210);\n"
                            "}")

    if shadow:
        shadow.setXOffset(0)
        shadow.setYOffset(2)
        shadow.setBlurRadius(15)
        shadow.setColor(QColor (200, 200, 200))

        button.setGraphicsEffect(shadow) 