from model.Observer import Observer


class AbrirTelaCriarFlashcards(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 1:
            self._stack_telas.screens[2].clear()
            self._stack_telas.open_screen(2)
