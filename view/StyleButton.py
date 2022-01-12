from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor


def style_button(button, cor, tam_fonte, border_radius, rgb_da_letra="(50, 50, 50)", border_color="(84, 84, 84)"):
    cores = {"cinza": "(235, 235, 235)", 
            "azul": "(125, 185, 255)", 
            "vermelho": "(255, 135, 135)", 
            "verde": "(156, 255, 176)", 
            "cinza_escuro": "(64, 64, 64)"}

    button.setStyleSheet("QPushButton{\n"
                                "font: " + tam_fonte + "pt;\n"
                                "background-color: rgb" + cores[cor] + ";\n"
                                "color: rgb" + rgb_da_letra + ";\n"
                                "border: 1px solid;\n"
                                "border-top-left-radius: " + str(border_radius[0]) + "px;\n" 
                                "border-top-right-radius: " + str(border_radius[1]) + "px;\n" 
                                "border-bottom-left-radius: " + str(border_radius[2]) + "px;\n" 
                                "border-bottom-right-radius: " +  str(border_radius[3]) + "px;\n" 
                                "border-color: rgb" + border_color + ";\n"
                            "}\n"

                            "QPushButton:hover{\n"
                                "background-color: rgb(107, 107, 107);\n"
                                "color: rgb(245, 245, 245);\n"
                            "}\n"

                            "QPushButton:pressed{\n"
                                "background-color: rgb(75, 75, 75);\n"
                                "color: rgb(210, 210, 210);\n"
                            "}")

    #shadow = QGraphicsDropShadowEffect()
    #shadow.setXOffset(0)
    #shadow.setYOffset(2)
    #shadow.setBlurRadius(10)
    #shadow.setColor(QColor (200, 200, 200))

    #button.setGraphicsEffect(shadow)
