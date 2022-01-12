from PyQt5.QtWidgets import QApplication, QMessageBox

import sys

from view.TelaInicial import TelaInicial
from view.TelaRevisoes import TelaRevisoes
from view.TelaCriarFlashcards import TelaCriarFlashcards
from view.TelaRevisao import TelaRevisao
from view.TelaOpcoesRevisao import TelaOpcoesRevisao
from view.TelaDatas import TelaDatas
from view.TelaFlashcards import TelaFlashcards
from view.TelaCriarRotina import TelaCriarRotina
from view.TelaRotina import TelaRotina
from view.TelaHistorico import TelaHistorico
from view.StackTelas import StackTelas

from model.CreateDatabase import create_database
from model.AbrirTelaRevisoes import AbrirTelaRevisoes
from model.AbrirTelaCriarFlashcards import AbrirTelaCriarFlashcards
from model.AbrirTelaFlashcards import AbrirTelaFlashcards
from model.VoltarParaTelaInicial import VoltarParaTelaInicial
from model.CriarESalvarFlashcards import CriarESalvarFlashcards
from model.DefinirDatasDosFlashcards import DefinirDatasDosFlashcards
from model.AbrirTelaOpcoesRevisao import AbrirTelaOpcoesRevisao
from model.AbrirTelaRevisao import AbrirTelaRevisao
from model.ControleDaRevisaoFlashcards import ControleDaRevisaoFlashcards
from model.DeletarFlashcard import DeletarFlashcard
from model.AbrirTelaCriarRotina import AbrirTelaCriarRotina
from model.CriarESalvarRotina import CriarESalvarRotina
from model.AbrirTelaRotina import AbrirTelaRotina
from model.SalvarEstadoDaAtividade import SalvarEstadoDaAtividade
from model.AbrirTelaHistorico import AbrirTelaHistorico


def create_screens():
	telas = []

	telas.append(TelaInicial()) # 0

	telas.append(TelaRevisoes()) # 1

	telas.append(TelaCriarFlashcards()) # 2

	telas.append(TelaRevisao()) # 3

	telas.append(TelaOpcoesRevisao()) # 4

	telas.append(TelaDatas()) # 5

	telas.append(TelaFlashcards()) # 6

	telas.append(TelaCriarRotina()) # 7

	telas.append(TelaRotina()) # 8

	telas.append(TelaHistorico()) # 9

	return telas


def create_observers(stack_telas):
	voltar_para_tela_inicial = VoltarParaTelaInicial(stack_telas)
	criar_e_salvar_flashcards = CriarESalvarFlashcards(stack_telas, QMessageBox)
	abrir_tela_revisoes = AbrirTelaRevisoes(stack_telas)
	controle_da_revisao_flashcards = ControleDaRevisaoFlashcards(stack_telas, abrir_tela_revisoes)

	stack_telas.screens[0].subject.subscribe(abrir_tela_revisoes)
	stack_telas.screens[0].subject.subscribe(AbrirTelaCriarFlashcards(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaFlashcards(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaCriarRotina(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaRotina(stack_telas))
	stack_telas.screens[0].subject.subscribe(AbrirTelaHistorico(stack_telas))

	stack_telas.screens[1].subject.subscribe(voltar_para_tela_inicial)
	stack_telas.screens[2].subject.subscribe(voltar_para_tela_inicial)
	stack_telas.screens[6].subject.subscribe(voltar_para_tela_inicial)

	stack_telas.screens[0].subject.subscribe(criar_e_salvar_flashcards)
	stack_telas.screens[2].subject.subscribe(criar_e_salvar_flashcards)
	stack_telas.screens[5].subject.subscribe(criar_e_salvar_flashcards)

	stack_telas.screens[2].subject.subscribe(DefinirDatasDosFlashcards(stack_telas, QMessageBox))

	stack_telas.screens[1].subject.subscribe(AbrirTelaOpcoesRevisao(stack_telas))
	stack_telas.screens[4].subject.subscribe(abrir_tela_revisoes)

	stack_telas.screens[4].subject.subscribe(AbrirTelaRevisao(stack_telas))

	stack_telas.screens[3].subject.subscribe(abrir_tela_revisoes)

	stack_telas.screens[1].subject.subscribe(controle_da_revisao_flashcards)
	stack_telas.screens[4].subject.subscribe(controle_da_revisao_flashcards)
	stack_telas.screens[3].subject.subscribe(controle_da_revisao_flashcards)

	stack_telas.screens[6].subject.subscribe(DeletarFlashcard(stack_telas, QMessageBox))

	stack_telas.screens[7].subject.subscribe(voltar_para_tela_inicial)

	stack_telas.screens[7].subject.subscribe(CriarESalvarRotina(stack_telas))

	stack_telas.screens[8].subject.subscribe(voltar_para_tela_inicial)
	stack_telas.screens[8].subject.subscribe(SalvarEstadoDaAtividade(stack_telas))

	stack_telas.screens[9].subject.subscribe(voltar_para_tela_inicial)


if __name__ == '__main__':
	root = QApplication(sys.argv)


	create_database()
	stack_telas = StackTelas(create_screens())
	create_observers(stack_telas)


	sys.exit(root.exec_())
