from model.Observer import Observer


class VoltarParaTelaInicial(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] in (3, 9, 10, 26, 30, 32):
            self._stack_telas.open_screen(0)
