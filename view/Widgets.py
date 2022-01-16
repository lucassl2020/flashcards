from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit, QCalendarWidget, QComboBox, QGroupBox, QListWidget, QRadioButton, QSpinBox, QTableWidget, QProgressBar
from PyQt5.QtCore import QRect


def button(tela, nome, x, y, largura, altura):
    button = QPushButton(nome, tela)
    button.setGeometry(QRect(x, y, largura, altura))

    return button


def label(tela, nome, x, y, largura, altura):
    label_ = QLabel(nome, tela)
    label_.setGeometry(QRect(x, y, largura, altura))

    return label_


def lineEdit(tela, x, y, largura, altura):
    line_edit = QLineEdit(tela)
    line_edit.setGeometry(QRect(x, y, largura, altura))

    return line_edit


def textEdit(tela, x, y, largura, altura):
    text_edit = QTextEdit(tela)
    text_edit.setGeometry(QRect(x, y, largura, altura))

    return text_edit


def calendar(tela, x, y, largura, altura):
    calendar_ = QCalendarWidget(tela)
    calendar_.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
    calendar_.setGridVisible(True)
    calendar_.setGeometry(QRect(x, y, largura, altura))

    return calendar_


def comboBox(tela, duplicates, maxCount, x, y, largura, altura):
    combo_box = QComboBox(tela)
    combo_box.setDuplicatesEnabled(duplicates)
    combo_box.setMaxCount(maxCount)
    combo_box.setEditable(True)
    combo_box.setGeometry(QRect(x, y, largura, altura))

    return combo_box


def groupBox(tela, nome, x, y, largura, altura):
    group_box = QGroupBox(nome, tela)
    group_box.setGeometry(QRect(x, y, largura, altura))

    return group_box


def listWidget(tela, x, y, largura, altura):
    a_list = QListWidget(tela)
    a_list.setGeometry(QRect(x, y, largura, altura))

    return a_list


def radioButton(tela, nome, x, y, largura, altura):
    radio_button = QRadioButton(nome, tela)
    radio_button.setGeometry(QRect(x, y, largura, altura))

    return radio_button


def spinBox(tela, x, y, largura, altura):
    spin_box = QSpinBox(tela)
    spin_box.setGeometry(QRect(x, y, largura, altura))

    return spin_box


def table(tela, x, y, largura, altura):
    tableWidget = QTableWidget(tela)
    tableWidget.setGeometry(QRect(x, y, largura, altura))

    return tableWidget


def progressBar(tela, x, y, largura, altura):
    progressBarWidget = QProgressBar(tela)
    progressBarWidget.setGeometry(QRect(x, y, largura, altura))

    return progressBarWidget
