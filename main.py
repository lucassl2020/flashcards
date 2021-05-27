import sys
import pickle 
import os

from datetime import timedelta, date

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon

from TelaInicial import TelaInicial
from TelaVerDia import TelaVerDia
from TelaCriarFlashcards import TelaCriarFlashcards
from ObjetoFlashcards import ObjetoFlashcards
from TelaRevisao import TelaRevisao
from TelaOpcoesRevisao import TelaOpcoesRevisao
from TelaDatas import TelaDatas
from ObjetoRevisao import ObjetoRevisao


class Main(QtWidgets.QStackedLayout):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self._objetoFlashcards = ObjetoFlashcards()
        self._objetoRevisao = ObjetoRevisao()
        self.icon = QIcon("icone.png")
        self._createScreens()
        self._connectWidgets()

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
                if pergunta[-1] != "?":
                    pergunta += "?"

                if pergunta in self._objetoFlashcards.flashcards:
                    QMessageBox.information(None, "FLASHCARDS", "Pergunta ja criada")
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
                        self._objetoFlashcards.nome = titulo

                        self.tela_criar_flashcards.clear("all")

                        self.abrir_telaDatas()
                        
        else:
            QMessageBox.information(None, "FLASHCARDS", "Dê um titulo")

    def abrir_TelaOpcoesRevisao(self):
        self.tela_opcoes_revisao.clear("all")

        self.setCurrentIndex(4)

    def abrir_TelaRevisao(self):
        indice_pergunta = 0

        self.tela_revisao.clear("all")

        self._objetoRevisao.copiarFlashcardsLista()
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

    def revisarAtrasado_TelaVerDia(self):
        pathFlashcards = "flashcards"

        nome_objetoFlashcards = self.tela_ver_dia.getText("revisoes_atrasadas_lista")

        if nome_objetoFlashcards:
            self._objetoRevisao.objetoFlashcards = self.abrirObjetoFlashcards(pathFlashcards, nome_objetoFlashcards + ".obj")
            self.abrir_TelaOpcoesRevisao()

    def revisarDoDia_TelaVerDia(self):
        pathFlashcards = "flashcards"

        nome_objetoFlashcards = self.tela_ver_dia.getText("revisoes_do_dia_lista")

        if nome_objetoFlashcards:
            self._objetoRevisao.objetoFlashcards = self.abrirObjetoFlashcards(pathFlashcards, nome_objetoFlashcards + ".obj")
            self.abrir_TelaOpcoesRevisao()

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
        self._objetoRevisao.acerteiResposta()

        self.proximo_ObjetoRevisao()

    def erreiResposta(self, ):
        self._objetoRevisao.erreiResposta()

        self.proximo_ObjetoRevisao()

    def proximo_ObjetoRevisao(self): 
        pathFlashcards = "flashcards"
        indice_pergunta = 0
        indice_primeira_data = 0

        if self._objetoRevisao.acabouRevisao():
            self._objetoRevisao.objetoFlashcards.deletarData(indice_primeira_data)
            self.salvarObjetoFlashcards(pathFlashcards, self._objetoRevisao.objetoFlashcards)
            self.voltar_TelaRevisao()
        else:
            self.tela_revisao.setText("pergunta_ou_resposta", "pergunta")
            self.tela_revisao.setText("texto", self._objetoRevisao.flashcards[self._objetoRevisao.cursor][indice_pergunta])
            self.tela_revisao.setText("ciclo_line", str(self._objetoRevisao.ciclo+1))

    def abrir_telaDatas(self):
        self.tela_datas.clear("all")

        hoje = date.today()

        self.tela_datas.calendario_widget.setMinimumDate(QDate(hoje.year, hoje.month, hoje.day))

        self.setCurrentIndex(5)

    def adicionar_TelaDatas(self):
        data_selecionada = self.tela_datas.calendario_widget.selectedDate()

        ano = data_selecionada.year()
        mes = data_selecionada.month()
        dia = data_selecionada.day()

        data = date(ano, mes, dia)
        data_str = str(dia) + "/" + str(mes) + "/" + str(ano)         
        
        if data not in self._objetoFlashcards.datas:
            self._objetoFlashcards.adicionarData(data)

            self.tela_datas.setText("datas_listwidget", data_str)

    def remover_TelaDatas(self):
        indice_data_selected = self.tela_datas.datas_listwidget.currentRow()

        if indice_data_selected > -1:
            self.tela_datas.datas_listwidget.takeItem(indice_data_selected)

            self._objetoFlashcards.deletarData(indice_data_selected)

    def finalizar_TelaDatas(self):
        pathFlashcards = "flashcards"
        
        if self._objetoFlashcards.isEmptyDatas():
            QMessageBox.information(None, "FLASHCARDS", "Nenhuma data foi definida")
        else:
            self.salvarObjetoFlashcards(pathFlashcards, self._objetoFlashcards)

            self._objetoFlashcards.new()

            self.abrir_TelaInicial()


if __name__ == '__main__':
    root = QtWidgets.QApplication(sys.argv)
    app = Main()
    sys.exit(root.exec_())
