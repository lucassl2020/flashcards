from model.Observer import Observer


class AbrirTelaOpcoesRevisao(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        if event["codigo"] in (4, 5):
            self._stack_telas.screens[4].clear()
            self._stack_telas.screens[4].qtd_ciclos_spinbox.setValue(10)
            self._stack_telas.screens[4].qtd_ciclos_spinbox.setMinimum(1)
            self._stack_telas.open_screen(4)
