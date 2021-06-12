import sys
import pickle 
import os

from datetime import date

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon

from Telas.TelaInicial import TelaInicial
from Telas.TelaVerDia import TelaVerDia
from Telas.TelaCriarFlashcards import TelaCriarFlashcards
from Telas.TelaRevisao import TelaRevisao
from Telas.TelaOpcoesRevisao import TelaOpcoesRevisao
from Telas.TelaDatas import TelaDatas

from ObjetoRevisao import ObjetoRevisao

import mysql.connector as mysql

from Datas import hoje, hojeSplit, data

class Main(QtWidgets.QStackedLayout):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self._objetoRevisao = ObjetoRevisao()
        self._id_grupo = None
        self._id_data = None

        self._createScreens()
        self._connectWidgets()
        self._createDataBase()

    def _createScreens(self):
        self.tela_inicial = TelaInicial()
        self.tela_ver_dia = TelaVerDia()
        self.tela_criar_flashcards = TelaCriarFlashcards()
        self.tela_revisao = TelaRevisao()
        self.tela_opcoes_revisao = TelaOpcoesRevisao()
        self.tela_datas = TelaDatas()

        self.addWidget(self.tela_inicial)
        self.addWidget(self.tela_ver_dia)
        self.addWidget(self.tela_criar_flashcards)
        self.addWidget(self.tela_revisao)
        self.addWidget(self.tela_opcoes_revisao)
        self.addWidget(self.tela_datas)

    def _connectWidgets(self):
        self.tela_inicial.setConnect("ver_dia_botao", self.abrir_TelaVerDia)
        self.tela_inicial.setConnect("criar_flashcards_botao", self.abrir_TelaCriarFlashcards)

        self.tela_ver_dia.setConnect("voltar_botao", self.abrir_TelaInicial)
        self.tela_ver_dia.setConnect("revisar_atrasado_botao", self.revisarAtrasado_TelaVerDia)
        self.tela_ver_dia.setConnect("revisar_atual_botao", self.revisarDoDia_TelaVerDia)

        self.tela_criar_flashcards.setConnect("adicionar_botao", self.adicionar_TelaCriarFlashcards)
        self.tela_criar_flashcards.setConnect("deletar_botao", self.deletar_TelaCriarFlashcards)
        self.tela_criar_flashcards.setConnect("salvar_botao", self.salvar_TelaCriarFlashcards)
        self.tela_criar_flashcards.setConnect("cancelar_botao", self.cancelar_TelaCriarFlashcards)

        self.tela_revisao.setConnect("voltar_botao", self.voltar_TelaRevisao)
        self.tela_revisao.setConnect("anterior_botao", self.anteriorOuProximo_TelaRevisao)
        self.tela_revisao.setConnect("proximo_botao", self.anteriorOuProximo_TelaRevisao)
        self.tela_revisao.setConnect("acertei_botao", self.acerteiResposta)
        self.tela_revisao.setConnect("errei_botao", self.erreiResposta)  

        self.tela_opcoes_revisao.setConnect("iniciar_botao", self.abrir_TelaRevisao) 
        self.tela_opcoes_revisao.setConnect("voltar_botao", self.abrir_TelaVerDia) 

        self.tela_datas.setConnect("adicionar_botao", self.adicionar_TelaDatas) 
        self.tela_datas.setConnect("remover_botao", self.remover_TelaDatas) 
        self.tela_datas.setConnect("finalizar_botao", self.finalizar_TelaDatas) 

    def applySqlCommand(self, sql_command, retorno=None):
        conexao = mysql.connect(host="localhost", db="flashcardsDB", user="root", passwd="")

        cursor = conexao.cursor()

        cursor.execute(sql_command)

        if retorno == "fetchall":
            valor = cursor.fetchall()
        elif retorno == "lastrowid":
            valor = cursor.lastrowid 
        else:
            valor = None

        conexao.commit()

        conexao.close()

        return valor

    def _createDataBase(self):
        self.applySqlCommand("SET default_storage_engine=InnoDB;")

        sql_command = """CREATE TABLE IF NOT EXISTS Grupos(
                    id INTEGER AUTO_INCREMENT PRIMARY KEY UNIQUE,
                    titulo TEXT NOT NULL
                );"""
        self.applySqlCommand(sql_command)

        sql_command = """CREATE TABLE IF NOT EXISTS Flashcards(
                    id INTEGER AUTO_INCREMENT PRIMARY KEY UNIQUE,
                    pergunta TEXT NOT NULL, 
                    resposta TEXT NOT NULL,
                    id_grupo INTEGER NOT NULL,
                    CONSTRAINT fk_grupo FOREIGN KEY (id_grupo) REFERENCES Grupo (id)
                );"""
        self.applySqlCommand(sql_command)

        sql_command = """CREATE TABLE IF NOT EXISTS Datas(
                    id INTEGER AUTO_INCREMENT PRIMARY KEY UNIQUE,
                    data INTEGER NOT NULL, 
                    id_grupo INTEGER NOT NULL,
                    CONSTRAINT fk_grupo FOREIGN KEY (id_grupo) REFERENCES Grupo (id)
                );"""
        self.applySqlCommand(sql_command)

    def abrir_TelaInicial(self):
        self._id_grupo = None

        self.setCurrentIndex(0)

    def abrir_TelaVerDia(self):
        self.tela_ver_dia.clear("revisoes_do_dia_lista")
        self.tela_ver_dia.clear("revisoes_atrasadas_lista")

        self._id_data = None

        lista_grupos_flashcards = self.applySqlCommand("SELECT g.titulo, d.data FROM Grupos AS g INNER JOIN Datas AS d on g.id=d.id_grupo", retorno="fetchall")

        for tupla in lista_grupos_flashcards:
            titulo = tupla[0]
            data_flashcards = tupla[1]

            if hoje() == data_flashcards:
                self.tela_ver_dia.setText("revisoes_do_dia_lista", titulo)
            elif hoje() > data_flashcards:
            	self.tela_ver_dia.setText("revisoes_atrasadas_lista", titulo)

        self.setCurrentIndex(1)

    def revisarAtrasado_TelaVerDia(self):
        tiulo_grupo = self.tela_ver_dia.getText("revisoes_atrasadas_lista")

        if tiulo_grupo:
            lista_grupo = self.applySqlCommand("SELECT id FROM Grupos WHERE titulo='%s'" % (tiulo_grupo), "fetchall")
            id_grupo = lista_grupo[0][0]

            lista_data = self.applySqlCommand("SELECT id FROM Datas WHERE id_grupo=%s ORDER BY data" % (id_grupo), "fetchall")
            self._id_data = lista_data[0][0]

            lista_grupo = self.applySqlCommand("SELECT pergunta, resposta FROM Flashcards WHERE id_grupo=%s" % (id_grupo), "fetchall")

            self._objetoRevisao.adicionarFlashcards(lista_grupo)

            self.abrir_TelaOpcoesRevisao()

    def revisarDoDia_TelaVerDia(self):
        tiulo_grupo = self.tela_ver_dia.getText("revisoes_do_dia_lista")

        if tiulo_grupo:
            lista_grupo = self.applySqlCommand("SELECT id FROM Grupos WHERE titulo='%s'" % (tiulo_grupo), "fetchall")
            id_grupo = lista_grupo[0][0]

            lista_data = self.applySqlCommand("SELECT id FROM Datas WHERE id_grupo=%s ORDER BY data" % (id_grupo), "fetchall")
            self._id_data = lista_data[0][0]

            lista_grupo = self.applySqlCommand("SELECT pergunta, resposta FROM Flashcards WHERE id_grupo='%s'" % (id_grupo), "fetchall")

            self._objetoRevisao.adicionarFlashcards(lista_grupo)

            self.abrir_TelaOpcoesRevisao()

    def abrir_TelaOpcoesRevisao(self):
        self.tela_opcoes_revisao.clear("all")

        self.setCurrentIndex(4)

    def abrir_TelaRevisao(self):
        indice_pergunta = 0

        self.tela_revisao.clear("all")

        self._objetoRevisao.adicionarAoMaxCiclo(self.tela_opcoes_revisao.qtd_ciclos_spinbox.value())

        if self.tela_opcoes_revisao.ordenar_flashcards_radiobutton.isChecked():
            modo_revisao_ordenar = 1
            self. _objetoRevisao.modo = modo_revisao_ordenar
        elif self.tela_opcoes_revisao.retirar_flashcard_radiobutton.isChecked():
            modo_revisao_retirar = 2
            self._objetoRevisao.modo = modo_revisao_retirar

        self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
        self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_pergunta])
        self.tela_revisao.setText("ciclo_line", "1")

        self.setCurrentIndex(3)

    def voltar_TelaRevisao(self):
        self._objetoRevisao.new()

        self.abrir_TelaVerDia()

    def anteriorOuProximo_TelaRevisao(self):
        indice_pergunta = 0
        indice_resposta = 1

        if self.tela_revisao.getText("pergunta_ou_resposta") == "pergunta":
            self.tela_revisao.setText("pergunta_ou_resposta", "resposta")
            self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_resposta])
        else:
            self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
            self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_pergunta])

    def proximo_ObjetoRevisao(self): 
        indice_pergunta = 0
        indice_primeira_data = 0

        if self._objetoRevisao.acabouRevisao():
            self.applySqlCommand("DELETE FROM Datas WHERE id=%s" % (self._id_data))
            self.voltar_TelaRevisao()
        else:
            self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
            self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_pergunta])
            self.tela_revisao.setText("ciclo_line", str(self._objetoRevisao.ciclo+1))

    def acerteiResposta(self):
        self._objetoRevisao.acerteiResposta()

        self.proximo_ObjetoRevisao()

    def erreiResposta(self):
        self._objetoRevisao.erreiResposta()

        self.proximo_ObjetoRevisao()

    def abrir_TelaCriarFlashcards(self):
        self._id_grupo = self.applySqlCommand("INSERT INTO Grupos (titulo) VALUES ('default')", "lastrowid")

        self.setCurrentIndex(2)

    def abrir_TelaCriarFlashcards(self):
        self._id_grupo = self.applySqlCommand("INSERT INTO Grupos (titulo) VALUES ('default')", "lastrowid")

        self.setCurrentIndex(2)

    def cancelar_TelaCriarFlashcards(self):
        self.applySqlCommand("DELETE FROM Grupos WHERE id=%s" % (self._id_grupo))
        self.applySqlCommand("DELETE FROM Flashcards WHERE id_grupo=%s" % (self._id_grupo))
        self.applySqlCommand("DELETE FROM Datas WHERE id_grupo=%s" % (self._id_grupo))

        self.tela_criar_flashcards.clear("flashcards_box", "pergunta_texto", "resposta_texto", "titulo_line")

        self.abrir_TelaInicial()

    def adicionar_TelaCriarFlashcards(self):
        pergunta = self.tela_criar_flashcards.getText("pergunta_texto")
        resposta = self.tela_criar_flashcards.getText("resposta_texto")

        if pergunta != "" and resposta != "":
            if self.tela_criar_flashcards.flashcards_box.count() < 40:
                if pergunta[-1] != "?":
                    pergunta += "?"

                self.applySqlCommand("INSERT INTO Flashcards (pergunta, resposta, id_grupo) VALUES ('%s', '%s', %s)" % (pergunta, resposta, self._id_grupo))
                self.tela_criar_flashcards.flashcards_box.addItem(pergunta)
            else:
                QMessageBox.information(None, "FLASHCARDS", "Limite de 40 flashcards atingidos")
        else:
            QMessageBox.information(None, "FLASHCARDS", "Campo(s) vazio(s)")

    def deletar_TelaCriarFlashcards(self):
        pergunta = self.tela_criar_flashcards.getText("flashcards_box")
        indice = self.tela_criar_flashcards.flashcards_box.currentIndex()

        if pergunta:
            self.applySqlCommand("DELETE FROM Flashcards WHERE pergunta='%s' AND id_grupo=%s " % (pergunta, self._id_grupo))
            self.tela_criar_flashcards.flashcards_box.removeItem(indice)

    def salvar_TelaCriarFlashcards(self):
        titulo = self.tela_criar_flashcards.getText("titulo_line")

        if titulo != "":
            lista_flashcards = self.applySqlCommand("SELECT * FROM Flashcards WHERE id_grupo=%s" % (self._id_grupo), "fetchall")

            if lista_flashcards:
                question_finalizar = QMessageBox.question(None, "Salvar", "Deseja realmente salvar os flashcards?", QMessageBox.Yes, QMessageBox.No)

                if question_finalizar == QMessageBox.Yes:
                    lista_titulo = self.applySqlCommand("SELECT 1 FROM Grupos WHERE substr(titulo, 1, %s)='%s'" % (len(titulo), titulo), "fetchall")

                    if lista_titulo:
                        titulo += "({})".format(len(lista_titulo))

                    self.applySqlCommand("UPDATE Grupos SET titulo='%s' WHERE id=%s" % (titulo, self._id_grupo))

                    self.tela_criar_flashcards.clear("all")

                    self.abrir_telaDatas()
            else:
                QMessageBox.information(None, "FLASHCARDS", "Nenhum flashcard foi criado")       
        else:
            QMessageBox.information(None, "FLASHCARDS", "Dê um titulo")

    def abrir_telaDatas(self):
        self.tela_datas.clear("all")

        ano, mes, dia = hojeSplit()

        self.tela_datas.calendario_widget.setMinimumDate(QDate(ano, mes, dia))

        self.setCurrentIndex(5)

    def adicionar_TelaDatas(self):
        data_selecionada = self.tela_datas.calendario_widget.selectedDate()

        ano = data_selecionada.year()
        mes = data_selecionada.month()
        dia = data_selecionada.day()

        data_inteiro = data(ano, mes, dia)
        data_str = str(dia) + "/" + str(mes) + "/" + str(ano)

        datas_lista = self.applySqlCommand("SELECT 1 FROM Datas WHERE data=%s AND id_grupo=%s" % (data_inteiro, self._id_grupo), "fetchall")
        
        if not datas_lista:
            self.applySqlCommand("INSERT INTO Datas (data, id_grupo) VALUES (%s, %s)" % (data_inteiro, self._id_grupo))

            self.tela_datas.setText("datas_listwidget", data_str)

    def remover_TelaDatas(self):
        indice_data_selected = self.tela_datas.datas_listwidget.currentRow()

        if indice_data_selected > -1:
            data_str = self.tela_datas.datas_listwidget.takeItem(indice_data_selected).text()

            data_lista = data_str.split("/")

            dia = int(data_lista[0])
            mes = int(data_lista[1])
            ano = int(data_lista[2])

            data_inteiro = data(ano, mes, dia)

            self.applySqlCommand("DELETE FROM Datas WHERE data=%s AND id_grupo=%s" % (data_inteiro, self._id_grupo))
            
    def finalizar_TelaDatas(self):
        lista_datas = self.applySqlCommand("SELECT 1 FROM Datas WHERE id_grupo=%s" % (self._id_grupo), "fetchall")

        if lista_datas:
            self.abrir_TelaInicial()
        else:
            QMessageBox.information(None, "FLASHCARDS", "Nenhuma data foi definida")


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())
