import sys
import pickle 
import os

from datetime import timedelta, date

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

from tela_inicial import TelaInicial
from tela_ver_dia import TelaVerDia
from tela_criar_flashcards import TelaCriarFlashcards
from objeto_criar_flashcards import ObjetoCriarFlashcards
from tela_revisao import TelaRevisao



class Main(QtWidgets.QStackedLayout):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self._createScreens()
        self._createObject()
        self._connectWidgets()

    def _createObject(self):
        self.objeto_criar_flashcards = ObjetoCriarFlashcards()

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
        self.tela_ver_dia.setConnect("revisar_atrasado_botao", self.telaRevisao_atrasado)
        self.tela_ver_dia.setConnect("revisar_atual_botao", self.telaRevisao_atual)

        self.tela_criar_flashcards.setConnect("salvar_botao", self.salvar_TelaCriarFlashcards)
        self.tela_criar_flashcards.setConnect("deletar_botao", self.deletar_TelaCriarFlashcards)
        self.tela_criar_flashcards.setConnect("salvar_botao", self.finalizar_TelaCriarFlashcards)
        self.tela_criar_flashcards.setConnect("cancelar_botao", self.cancelar_TelaCriarFlashcards)

        self.tela_revisao.setConnect("voltar_botao", self.voltar_TelaRevisao)
        self.tela_revisao.setConnect("anterior_botao", self.anterior_ou_proximo)
        self.tela_revisao.setConnect("proximo_botao", self.anterior_ou_proximo)
        self.tela_revisao.setConnect("acertei_botao", self.acerteiResposta)
        self.tela_revisao.setConnect("errei_botao", self.erreiResposta)

    def abrir_TelaInicial(self):
        self.setCurrentIndex(0)

    def abrir_TelaVerDia(self):
        self.tela_ver_dia.revisoes_do_dia_lista.clear()
        self.tela_ver_dia.revisoes_atrasadas_lista.clear()

        arquivos = os.listdir("flashcards")

        for arquivo in arquivos:
            filehandler = open ("flashcards\\" + arquivo, 'rb')
            flashcard = pickle.load(filehandler)

            if flashcard.isEmptyDatas():
                filehandler_2 = open("C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\flashcards\\finalizados\\" + arquivo, 'wb')
                pickle.dump(flashcard, filehandler_2)
                filehandler.close()
                filehandler_2.close()
                os.remove("flashcards\\" + arquivo)
                continue

            if flashcard.datas[0] == date.today():
                self.tela_ver_dia.revisoes_do_dia_lista.addItem(arquivo[:len(arquivo)-4])
            elif flashcard.datas[0] < date.today():
                self.tela_ver_dia.revisoes_atrasadas_lista.addItem(arquivo[:len(arquivo)-4])

        filehandler.close()

        self.setCurrentIndex(1)

    def abrir_TelaCriarFlashcards(self):
        self.setCurrentIndex(2)

    def cancelar_TelaCriarFlashcards(self):
        self.objeto_criar_flashcards.finalizar()

        self.tela_criar_flashcards.clear()

        self.abrir_TelaInicial()

    def salvar_TelaCriarFlashcards(self):
        pergunta = self.tela_criar_flashcards.pergunta_texto.toPlainText()
        resposta = self.tela_criar_flashcards.resposta_texto.toPlainText()

        if pergunta != "" and resposta != "":
            if self.tela_criar_flashcards.flashcards_box.count() < 40:
                if pergunta in self.objeto_criar_flashcards.flashcards:
                    QMessageBox.information(None, "FLASHCARDS", "Pergunta ja criada")
                else:
                    if self.objeto_criar_flashcards.salvar(pergunta, resposta):
                        self.tela_criar_flashcards.flashcards_box.addItem(pergunta)
                    else:
                        QMessageBox.information(None, "FLASHCARDS", "Ocorreu um erro\n\nTente novamente")
            else:
                QMessageBox.information(None, "FLASHCARDS", "Limite de 40 cards atingidos")
        else:
            QMessageBox.information(None, "FLASHCARDS", "Campo(s) vazio(s)")

    def deletar_TelaCriarFlashcards(self):
        pergunta = self.tela_criar_flashcards.flashcards_box.currentText()
        indice = self.tela_criar_flashcards.flashcards_box.currentIndex()

        if self.objeto_criar_flashcards.deletar(pergunta):
            self.tela_criar_flashcards.flashcards_box.removeItem(indice)
        else:
            QMessageBox.information(None, "FLASHCARDS", "Ocorreu um erro\n\nTente novamente")

    def finalizar_TelaCriarFlashcards(self):
        titulo = self.tela_criar_flashcards.titulo_line.text()

        question_finalizar = QMessageBox.question(None, "Finalizar", "Deseja realmente finalizar a criação de flashcards?", QMessageBox.Yes, QMessageBox.No)

        if question_finalizar == QMessageBox.Yes:
            if titulo != "":
                if self.objeto_criar_flashcards.isEmpty():
                    QMessageBox.information(None, "FLASHCARDS", "Nenhum card foi criado")
                else:
                    arquivos_flashcards = os.listdir("flashcards")

                    if (titulo + ".obj") in arquivos_flashcards:
                        QMessageBox.information(None, "FLASHCARDS", "Um arquivo com esse titulo ja existe")
                    else:
                        filehandler = open("flashcards\\" + titulo + ".obj", 'wb')

                        self.objeto_criar_flashcards.atualizarDatas()
                        self.objeto_criar_flashcards.nome = titulo

                        pickle.dump(self.objeto_criar_flashcards, filehandler)

                        self.objeto_criar_flashcards.finalizar()

                        self.tela_criar_flashcards.clear()

                        filehandler.close()

                        self.abrir_TelaInicial()
            else:
                QMessageBox.information(None, "FLASHCARDS", "Dê um titulo")

    def abrir_TelaRevisao(self, titulo):
        filehandler = open("flashcards\\" + titulo + ".obj", 'rb') 

        self.tela_revisao.titulo = pickle.load(filehandler)

        filehandler.close()

        self.tela_revisao.titulo.iniciarNiveis()
        self.tela_revisao.setText("texto", self.tela_revisao.titulo.nivel[self.tela_revisao.titulo.cursor][0])

        self.setCurrentIndex(3)

    def voltar_TelaRevisao(self):
        self.tela_revisao.titulo = None

        self.abrir_TelaVerDia()

    def telaRevisao_atrasado(self):
        titulo = self.tela_ver_dia.revisoes_atrasadas_lista.currentItem()
        if titulo:
            self.abrir_TelaRevisao(titulo.text())

    def telaRevisao_atual(self):
        titulo = self.tela_ver_dia.revisoes_do_dia_lista.currentItem()
        if titulo:
            self.abrir_TelaRevisao(titulo.text())

    def anterior_ou_proximo(self):
        if self.tela_revisao.pergunta_ou_resposta.text() == "pergunta":
            self.tela_revisao.setText("pergunta_ou_resposta", "resposta")
            self.tela_revisao.setText("texto", self.tela_revisao.titulo.nivel[self.tela_revisao.titulo.cursor][1])
        else:
            self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
            self.tela_revisao.setText("texto", self.tela_revisao.titulo.nivel[self.tela_revisao.titulo.cursor][0])

    def acerteiResposta(self):
        if self.tela_revisao.titulo.acertei_ou_errei(True) == False:
            self.salvarObjeto()
            
        self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
        self.tela_revisao.setText("texto", self.tela_revisao.titulo.nivel[self.tela_revisao.titulo.cursor][0])

    def erreiResposta(self):
        if self.tela_revisao.titulo.acertei_ou_errei(False) == False:
            self.salvarObjeto()

        self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
        self.tela_revisao.setText("texto", self.tela_revisao.titulo.nivel[self.tela_revisao.titulo.cursor][0])

    def salvarObjeto(self):
        filehandler = open("flashcards\\" + self.tela_revisao.titulo.nome + ".obj", 'wb')

        pickle.dump(self.tela_revisao.titulo, filehandler)

        filehandler.close()

        self.abrir_TelaVerDia()


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())
