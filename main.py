import sys
import pickle 
import os

from datetime import timedelta, date

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

from TelaInicial import TelaInicial
from TelaVerDia import TelaVerDia
from TelaCriarFlashcards import TelaCriarFlashcards
from ObjetoFlashcards import ObjetoFlashcards
from TelaRevisao import TelaRevisao
from ObjetoRevisao import ObjetoRevisao

class Main(QtWidgets.QStackedLayout):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self._objetoFlashcards = ObjetoFlashcards()
        self._objetoRevisao = ObjetoRevisao()

        self._createScreens()
        self._connectWidgets()

    def _createScreens(self):
        self.tela_inicial = TelaInicial()
        self.tela_ver_dia = TelaVerDia()
        self.tela_criar_flashcards = TelaCriarFlashcards()
        self.tela_revisao = TelaRevisao()

        self.addWidget(self.tela_inicial)
        self.addWidget(self.tela_ver_dia)
        self.addWidget(self.tela_criar_flashcards)
        self.addWidget(self.tela_revisao)

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

    def abrirObjetoFlashcards(self, path, arquivo):
        filehandler = open(path + "\\" + arquivo, 'rb')

        flashcardObjeto = pickle.load(filehandler)

        filehandler.close()

        return flashcardObjeto

    def salvarObjetoFlashcards(self, path, objetoFlashcards):
        filehandler = open(path + "\\" + objetoFlashcards.nome + ".obj", 'wb')

        pickle.dump(objetoFlashcards, filehandler)

        filehandler.close()

    def abrir_TelaInicial(self):
        self.setCurrentIndex(0)

    def abrir_TelaVerDia(self):
        self.tela_ver_dia.clear("revisoes_do_dia_lista")
        self.tela_ver_dia.clear("revisoes_atrasadas_lista")

        arquivos = os.listdir("flashcards")
        pathFlashcards = "flashcards"
        pathFinalizados = "C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\flashcards\\finalizados"
        today = date.today()

        for arquivo in arquivos:
            flashcardsObjeto = self.abrirObjetoFlashcards(pathFlashcards, arquivo)

            if flashcardsObjeto.isEmptyDatas():
                self.salvarObjetoFlashcards(pathFinalizados, flashcardsObjeto)
                os.remove(pathFlashcards + "\\" + arquivo)
                continue

            if flashcardsObjeto.datas[0] == today:
                self.tela_ver_dia.setText("revisoes_do_dia_lista", arquivo[:len(arquivo)-4])
            elif flashcardsObjeto.datas[0] < today:
            	self.tela_ver_dia.setText("revisoes_atrasadas_lista", arquivo[:len(arquivo)-4])

        self.setCurrentIndex(1)

    def abrir_TelaCriarFlashcards(self):
        self.setCurrentIndex(2)

    def cancelar_TelaCriarFlashcards(self):
        self._objetoFlashcards.new()

        self.tela_criar_flashcards.clear("flashcards_box", "pergunta_texto", "resposta_texto", "titulo_line")

        self.abrir_TelaInicial()

    def adicionar_TelaCriarFlashcards(self):
        pergunta = self.tela_criar_flashcards.getText("pergunta_texto")
        resposta = self.tela_criar_flashcards.getText("resposta_texto")

        if pergunta != "" and resposta != "":
            if self.tela_criar_flashcards.flashcards_box.count() < 40:
                if pergunta in self._objetoFlashcards.flashcards:
                    QMessageBox.information(None, "FLASHCARDS", "Pergunta ja criada")
                else:
                    if pergunta[-1] != "?":
                        self._objetoFlashcards.adicionarFlashcard(pergunta+"?", resposta)
                        self.tela_criar_flashcards.flashcards_box.addItem(pergunta+"?")
                    else:
                        self._objetoFlashcards.adicionarFlashcard(pergunta, resposta)
                        self.tela_criar_flashcards.flashcards_box.addItem(pergunta)
            else:
                QMessageBox.information(None, "FLASHCARDS", "Limite de 40 flashcards atingidos")
        else:
            QMessageBox.information(None, "FLASHCARDS", "Campo(s) vazio(s)")

    def deletar_TelaCriarFlashcards(self):
        pergunta = self.tela_criar_flashcards.getText("flashcards_box")
        indice = self.tela_criar_flashcards.flashcards_box.currentIndex()

        if pergunta:
            self._objetoFlashcards.deletarFlashcard(pergunta)
            self.tela_criar_flashcards.flashcards_box.removeItem(indice)

    def salvar_TelaCriarFlashcards(self):
        titulo = self.tela_criar_flashcards.getText("titulo_line")
        pathFlashcards = "flashcards"

        if titulo != "":
            if self._objetoFlashcards.isEmptyFlascards():
                QMessageBox.information(None, "FLASHCARDS", "Nenhum flashcard foi criado")
            else:
                arquivos_flashcards = os.listdir("flashcards")

                if (titulo + ".obj") in arquivos_flashcards:
                    QMessageBox.information(None, "FLASHCARDS", "Um arquivo com esse titulo ja existe")
                else:
                    question_finalizar = QMessageBox.question(None, "Salvar", "Deseja realmente salvar os flashcards?", QMessageBox.Yes, QMessageBox.No)

                    if question_finalizar == QMessageBox.Yes:
                        qtd_dias = [3, 10, 24, 54, 114]
                        for qtd in qtd_dias:
                             self._objetoFlashcards.adicionarData(qtd)
                        
                        self._objetoFlashcards.nome = titulo

                        self.salvarObjetoFlashcards(pathFlashcards, self._objetoFlashcards)

                        self._objetoFlashcards.new()

                        self.tela_criar_flashcards.clear("all")

                        self.abrir_TelaInicial()
        else:
            QMessageBox.information(None, "FLASHCARDS", "Dê um titulo")

    def abrir_TelaRevisao(self, nome_objetoFlashcards):
        pathFlashcards = "flashcards"
        indice_pergunta = 0

        self._objetoRevisao.objetoFlashcards = self.abrirObjetoFlashcards(pathFlashcards, nome_objetoFlashcards + ".obj")

        self._objetoRevisao.copiarFlashcardsLista()

        self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_pergunta])

        self.setCurrentIndex(3)

    def voltar_TelaRevisao(self):
        self._objetoRevisao.new()

        self.abrir_TelaVerDia()

    def revisarAtrasado_TelaVerDia(self):
        nome_objetoFlashcards = self.tela_ver_dia.getText("revisoes_atrasadas_lista")
        if nome_objetoFlashcards:
            self.abrir_TelaRevisao(nome_objetoFlashcards)

    def revisarDoDia_TelaVerDia(self):
        nome_objetoFlashcards = self.tela_ver_dia.getText("revisoes_do_dia_lista")
        if nome_objetoFlashcards:
            self.abrir_TelaRevisao(nome_objetoFlashcards)

    def anteriorOuProximo_TelaRevisao(self):
        indice_pergunta = 0
        indice_resposta = 1

        if self.tela_revisao.getText("pergunta_ou_resposta") == "pergunta":
            self.tela_revisao.setText("pergunta_ou_resposta", "resposta")
            self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_resposta])
        else:
            self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
            self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_pergunta])

    def acerteiResposta(self):
        indice_pergunta = 0
        pathFlashcards = "flashcards"

        self._objetoRevisao.acerteiResposta()

        if self._objetoRevisao.acabouRevisao():
            self._objetoRevisao.objetoFlashcards.deletarData()
            self.salvarObjetoFlashcards(pathFlashcards, self._objetoRevisao.objetoFlashcards)
            self.voltar_TelaRevisao()
        else:
            self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
            self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_pergunta])

    def erreiResposta(self):
        indice_pergunta = 0
        pathFlashcards = "flashcards"

        self._objetoRevisao.erreiResposta()

        if self._objetoRevisao.acabouRevisao():
            self._objetoRevisao.objetoFlashcards.deletarData()
            self.salvarObjetoFlashcards(pathFlashcards, self._objetoRevisao.objetoFlashcards)
            self.voltar_TelaRevisao()
        else:
            self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
            self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_pergunta])


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())
