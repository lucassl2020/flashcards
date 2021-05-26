from datetime import timedelta, date

class ObjetoFlashcards():
	def __init__(self):
		self._nome = ''
		self._flashcards = {}
		self._datas = []

	@property
	def flashcards(self):
		return self._flashcards

	@property
	def nome(self):
		return self._nome

	@property
	def datas(self):
		return self._datas

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	def isEmptyFlascards(self):
		if len(self.flashcards) == 0:
			return True
		return False

	def isEmptyDatas(self):
		if len(self.datas) == 0:
			return True
		return False

	def new(self):
		self._nome = ''
		self._flashcards = {}
		self._datas = []

	def adicionarFlashcard(self, pergunta, resposta):
		self._flashcards[pergunta] = resposta

	def deletarFlashcard(self, pergunta):
		del self._flashcards[pergunta]

	def adicionarData(self, qtd_dias):
		self._datas.append(date.today() + timedelta(days=qtd_dias))

	def deletarData(self):
		del self._datas[0]
