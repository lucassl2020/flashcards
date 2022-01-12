from model.Observer import Observer


class DefinirDatasDosFlashcards(Observer):
    def __init__(self, stack_telas, messager):
        self._stack_telas = stack_telas
        self._messager = messager


    def update(self, event):
        if event["codigo"] == 8:
            titulo = self._stack_telas.screens[2].titulo_line.text()   

            if titulo != "":
                if self._stack_telas.screens[2].flashcards_box.count() > 0:
                    self._stack_telas.screens[5].clear()
                    self._stack_telas.open_screen(5)
                else:
                    self._messager.information(None, "Flashcards", "Nenhum flashcard foi criado")       
            else:
                self._messager.information(None, "Flashcards", "Dê um titulo")