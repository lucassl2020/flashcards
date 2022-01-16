from model.Observer import Observer
import os


class AbrirTelaCriarFlashcards(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 1:
            self._stack_telas.open_screen(2)

            if not os.path.exists("backup.txt"):
                arquivo = open('backup.txt', 'w')
                arquivo.close()       
