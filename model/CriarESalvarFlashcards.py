from model.Observer import Observer
from model.Datas import data
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command
from shutil import copyfile
import os


class CriarESalvarFlashcards(Observer):
    def __init__(self, stack_telas, messager):
        self._stack_telas = stack_telas
        self._messager = messager
        self._flashcard = {}
        self._datas = []


    def update(self, event):
        if event["codigo"] == 1:
            self._stack_telas.screens[2].clear()
            self._flashcard = {}

            arquivo = open('backup.txt', 'r')
            lista = arquivo.readlines()
            arquivo.close()

            for i in range(0, len(lista), 2):
                pergunta = lista[i]
                resposta = lista[i+1]

                self._flashcard[pergunta] = resposta
                self._stack_telas.screens[2].flashcards_box.addItem(pergunta)

            
        if event["codigo"] == 8:
            self._datas = []

        if event["codigo"] == 6:
            pergunta = self._stack_telas.screens[2].pergunta_texto.toPlainText()
            resposta = self._stack_telas.screens[2].resposta_texto.toPlainText()

            if pergunta != "" and resposta != "":
                if pergunta not in self._flashcard:
                    arquivo = open('backup.txt', 'a')
                    arquivo.write(pergunta.replace("\n", " ") + "\n")
                    arquivo.write(resposta.replace("\n", " ") + "\n")
                    arquivo.close()

                    self._flashcard[pergunta] = resposta
                    self._stack_telas.screens[2].flashcards_box.addItem(pergunta)
                else:
                    self._messager.information(None, "FLASHCARDS", "Você já criou essa pergunta")
            else:
                self._messager.information(None, "FLASHCARDS", "Campo(s) vazio(s)")


        if event["codigo"] == 7:
            pergunta = self._stack_telas.screens[2].flashcards_box.currentText()
            indice = self._stack_telas.screens[2].flashcards_box.currentIndex()

            if pergunta:
                del self._flashcard[pergunta]
                self._stack_telas.screens[2].flashcards_box.removeItem(indice)


        if event["codigo"] == 21:
            data_selecionada =  self._stack_telas.screens[5].calendario_widget.selectedDate()

            ano = data_selecionada.year()
            mes = data_selecionada.month()
            dia = data_selecionada.day()

            data_inteiro = data(ano, mes, dia)

            if data_inteiro not in self._datas:
                self._datas.append(data_inteiro)
                self._stack_telas.screens[5].datas_listwidget.addItem(str(dia) + "/" + str(mes) + "/" + str(ano))


        if event["codigo"] == 22:
            indice_data_selected = self._stack_telas.screens[5].datas_listwidget.currentRow()

            if indice_data_selected > -1:
                del self._datas[indice_data_selected]
                self._stack_telas.screens[5].datas_listwidget.takeItem(indice_data_selected)


        if event["codigo"] == 23:
            if len(self._datas) > 0:
                conexao, cursor = abrir_banco_de_dados()

                titulo = self._stack_telas.screens[2].titulo_line.text()

                lista_titulos = apply_sql_command(cursor, "SELECT 1 FROM Grupos WHERE substr(titulo, 1, %s)='%s'" % (len(titulo), titulo), "fetchall")
                if lista_titulos:
                    titulo += "({})".format(len(lista_titulos))

                id_grupo = apply_sql_command(cursor, "INSERT INTO Grupos (titulo) VALUES ('%s')" % (titulo), "lastrowid")

                for data_ in self._datas:
                    apply_sql_command(cursor, "INSERT INTO Datas (data, id_grupo) VALUES (%s, %s)" % (data_, id_grupo))

                for pergunta, resposta in self._flashcard.items():
                    apply_sql_command(cursor, "INSERT INTO Flashcards (pergunta, resposta, id_grupo) VALUES ('%s', '%s', %s)" % (pergunta, resposta, id_grupo))

                fechar_banco_de_dados(conexao)

                copyfile("C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\flashcards refatorado2\\model\\banco de dados.db", "C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\flashcards refatorado2\\backup\\banco de dados.db")

                os.remove("backup.txt")

                self._stack_telas.open_screen(0)
            else:
                self._messager.information(None, "Datas", "Selecione ao menos 1 data")
