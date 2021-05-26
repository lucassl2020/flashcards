from PyQt5.QtGui import QColor
import abc

class SetInterface():
    def __init__(self):
        self._setTexts = {}
        self._getTexts = {}
        self._connects = {}
        self._clears = {}

    @abc.abstractmethod
    def _createSetTexts(self):
        pass

    @abc.abstractmethod
    def _createGetTexts(self):
        pass

    @abc.abstractmethod
    def _createConnects(self):
        pass

    @abc.abstractmethod
    def _createSetClears(self):
        pass

    def setText(self, widget_name, texto):
        func = self._setTexts[widget_name]
        func(texto)

    def getText(self, widget_name):
        func = self._getTexts[widget_name]
        return func()

    def setConnect(self, widget_name, funcao):
        func = self._connects[widget_name]
        func(funcao)

    def clear(self, *widget_names):
        if "all" in widget_names:
            widget_names = self._clears.keys()
            
        for widget_name in widget_names:
            func = self._clears[widget_name]
            func()


def style_button(button, shadow, cor, tam_fonte, tam_border_radius):
    button.setStyleSheet("QPushButton{\n"
                                "font: " + tam_fonte + "pt;\n"
                                "background-color: rgb" + cor + ";\n"
                                 "color: rgb(50, 50, 50);\n"
                                "border-radius: " + tam_border_radius + "px;\n"
                                "border: 1px double;\n"
                                "border-color: rgb(200, 200, 200)\n"
                            "}\n"

                            "QPushButton:hover{\n"
                                "background-color: rgb(107, 107, 107);\n"
                                "color: rgb(245, 245, 245);\n"
                            "}\n"

                            "QPushButton:pressed{\n"
                                "background-color: rgb(75, 75, 75);\n"
                                "color: rgb(210, 210, 210);\n"
                            "}")

    shadow.setXOffset(0)
    shadow.setYOffset(2)
    shadow.setBlurRadius(10)
    shadow.setColor(QColor (200, 200, 200))

    button.setGraphicsEffect(shadow) 