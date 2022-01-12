from model.Observer import Observer
import os 


class BackupTemporarioCriarFlashcards(Observer):
    def __init__(self, stack_telas):
        self._stack_telas = stack_telas


    def update(self, event):
        # VER BOTÃO ADICIONAR, DELETAR NO CRIAR FLASHCARDS
        # VER BOTÃO FINALIZAR EM DATAS
        # VER BOTÃO CRIAR FLASHCARDS NA TELA INICIAL
        # SE FINALIZAR, DELETA O ARQUIVO, SENÃO QUANDO O USUARIO ABRIR A TELA CRIAR FLASHCARDS AS PERGUNTAS E RESPOSTAS VÃO ESTAR LÁ.
        #if event["codigo"] == 2: os.remove("arquivo.txt")
            
            