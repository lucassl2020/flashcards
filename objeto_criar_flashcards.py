from datetime import timedelta, date
from random import shuffle


class ObjetoCriarFlashcards():
	def __init__(self):
		self.flashcards = {}
		self.datas = []
		self.nivel = []
		self.cursor = 0
		self.ciclo = 0
		self.nome = ''

	def salvar(self, pergunta, resposta):
		try:
			self.flashcards[pergunta] = resposta
			return True
		except:
			return False

	def deletar(self, pergunta):
		try:
			del self.flashcards[pergunta]
			return True
		except:
			return False

	def finalizar(self):
		self.flashcards = {}
		self.datas = []
		self.nivel = []
		self.cursor = 0
		self.ciclo = 0
		self.nome = ''

	def atualizarDatas(self):
		days = [3, 10, 24, 54, 114]

		for qtd in days:
			self.datas.append(date.today() + timedelta(days=qtd))

	def isEmpty(self):
		if len(self.flashcards) == 0:
			return True
		return False

	def isEmptyDatas(self):
		if len(self.datas) == 0:
			return True
		return False

	def iniciarNiveis(self):
		for pergunta in self.flashcards:
			self.nivel.append([pergunta, self.flashcards[pergunta], 0])

		shuffle(self.nivel)

	def proximo(self):
		self.cursor += 1

		if self.cursor >= len(self.nivel):
			self.nivel = sorted(self.nivel, key=lambda nivel: nivel[2]) 
			self.cursor = 0
			self.ciclo += 1

		if self.ciclo >= 6:
			return False

		return True

	def acertei_ou_errei(self, resposta):
		if resposta == True:
			self.nivel[self.cursor][2] += 1
		else:
			self.nivel[self.cursor][2] -= 1

		if self.proximo():
			return True

		self.modificarDatas()
		return False

	def modificarDatas(self):
		del self.datas[0]
		self.nivel = []
		self.cursor = 0
		self.ciclo = 0