from model.Observer import Observer
from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command

class ControleDaRevisaoFlashcards(Observer):
    def __init__(self, stack_telas, abrir_tela_ver_dia):
        self._stack_telas = stack_telas
        self._abrir_tela_ver_dia = abrir_tela_ver_dia

        self._indice_flashcard = 0
        self._flashcards = []
        self._id_grupo = -1
        self._id_data = -1
        self._ciclo = 1
        self._modo = -1
        self._max_ciclos = -1


    def update(self, event):
        if event["codigo"] in (4, 5):
            self._flashcards = []

            item = self._stack_telas.screens[1].revisoes_do_dia_lista.currentItem()
            if event["codigo"] == 4:
                item = self._stack_telas.screens[1].revisoes_atrasadas_lista.currentItem()
            titulo = item.text()  

            conexao, cursor = abrir_banco_de_dados()

            id_grupo = apply_sql_command(cursor, "SELECT id FROM Grupos WHERE titulo='%s'" % (titulo), "fetchall")
            self._id_grupo = id_grupo[0][0]

            id_data = apply_sql_command(cursor, "SELECT id FROM Datas WHERE id_grupo=%s ORDER BY data" % (self._id_grupo), "fetchall")
            self._id_data = id_data[0][0]

            lista_lashcards = apply_sql_command(cursor, "SELECT pergunta, resposta FROM Flashcards WHERE id_grupo='%s'" % (self._id_grupo), "fetchall")

            for tupla in lista_lashcards:
                pergunta = tupla[0]
                resposta = tupla[1]
                valor_para_ordenar = 0

                self._flashcards.append({"pergunta": pergunta, "resposta": resposta, "valor para ordenar": valor_para_ordenar})


            fechar_banco_de_dados(conexao)


        if event["codigo"] == 13:
            self._indice_flashcard = 0
            self._ciclo = 1
            self._stack_telas.screens[3].ciclo_line.setText(str(self._ciclo))
            self._max_ciclos = self._stack_telas.screens[4].qtd_ciclos_spinbox.value()

            self._modo = 1
            if self._stack_telas.screens[4].ordenar_flashcards_radiobutton.isChecked():
                self._modo = 0

            self._stack_telas.screens[3].texto.setText(self._flashcards[self._indice_flashcard]["pergunta"])

            
        if event["codigo"] in (15, 16):
            pergunta_ou_resposta = self._stack_telas.screens[3].pergunta_ou_resposta.text()

            if pergunta_ou_resposta == "Pergunta":
                self._stack_telas.screens[3].pergunta_ou_resposta.setText("Resposta")
                self._stack_telas.screens[3].texto.setText(self._flashcards[self._indice_flashcard]["resposta"])
            else:
                self._stack_telas.screens[3].pergunta_ou_resposta.setText("Pergunta")
                self._stack_telas.screens[3].texto.setText(self._flashcards[self._indice_flashcard]["pergunta"])
        

        if event["codigo"] in (17, 18):
            modo_ordenar = 0

            if event["codigo"] == 17:
                if self._modo == modo_ordenar:
                    self._flashcards[self._indice_flashcard]["valor para ordenar"] += 1
                else:
                    del self._flashcards[self._indice_flashcard]
                    self._indice_flashcard -= 1
            elif self._modo == modo_ordenar:
                self._flashcards[self._indice_flashcard]["valor para ordenar"] -= 1 


            self._indice_flashcard += 1

            if self._indice_flashcard >= len(self._flashcards):
                self._indice_flashcard = 0
                self._ciclo += 1

                if self._modo == modo_ordenar:
                    self._flashcards = sorted(self._flashcards, key=lambda flashcards: flashcards["valor para ordenar"]) 


            if (self._ciclo > self._max_ciclos) or (len(self._flashcards) <= 0):
                conexao, cursor = abrir_banco_de_dados()

                apply_sql_command(cursor,"DELETE FROM Datas WHERE id=%s" % (self._id_data))

                fechar_banco_de_dados(conexao)


                self._abrir_tela_ver_dia.update({"codigo": 0, "descricao": "Fim da revisão de flashcards"}) # FORÇANDO ABERTURA DA TELA VER DIA
            else:
                self._stack_telas.screens[3].pergunta_ou_resposta.setText("Pergunta")
                self._stack_telas.screens[3].texto.setText(self._flashcards[self._indice_flashcard]["pergunta"])
                self._stack_telas.screens[3].ciclo_line.setText(str(self._ciclo))


        if event["codigo"] == 20:
            pergunta_ou_resposta = self._stack_telas.screens[3].pergunta_ou_resposta.text().lower()
            new_text = self._stack_telas.screens[3].texto.toPlainText()

            if new_text != self._flashcards[self._indice_flashcard][pergunta_ou_resposta]:
                conexao, cursor = abrir_banco_de_dados()


                apply_sql_command(cursor, "UPDATE Flashcards SET %s = '%s' WHERE %s='%s' AND id_grupo=%s" % (pergunta_ou_resposta, new_text, pergunta_ou_resposta, self._flashcards[self._indice_flashcard][pergunta_ou_resposta], self._id_grupo))
                self._flashcards[self._indice_flashcard][pergunta_ou_resposta] = new_text
                    

                fechar_banco_de_dados(conexao)



