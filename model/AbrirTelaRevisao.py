from model.Observer import Observer


class AbrirTelaRevisao(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] == 13:
            self._stack_telas.screens[3].clear()
            self._stack_telas.open_screen(3)
