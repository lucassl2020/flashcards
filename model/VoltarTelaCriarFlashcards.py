from model.Observer import Observer


class VoltarTelaCriarFlashcards(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 37:
            self._stack_telas.open_screen(2)
