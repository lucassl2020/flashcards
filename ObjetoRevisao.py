from random import shuffle

class ObjetoRevisao():
	def __init__(self):
		self.objetoFlashcards = None
		self.flashcards = []
		self.cursor = 0
		self.ciclo = 0

	def new(self):
		self.objetoFlashcards = None
		self.flashcards = []
		self.cursor = 0
		self.ciclo = 0

	def copiarFlashcardsLista(self):
		for pergunta, resposta in self.objetoFlashcards.flashcards.items():
			self.flashcards.append([pergunta, resposta, 0])

		shuffle(self.flashcards)

	def proximoCursor(self):
		indice_ordem_pergunta = 2

		self.cursor += 1

		if self.cursor >= len(self.flashcards):
			self.flashcards = sorted(self.flashcards, key=lambda flashcards: flashcards[indice_ordem_pergunta]) 
			self.cursor = 0
			self.ciclo += 1

	def acabouRevisao(self):
		if self.ciclo >= 3:
			return True
		return False

	def acerteiResposta(self):
		indice_ordem_pergunta = 2

		self.flashcards[self.cursor][indice_ordem_pergunta] += 1

		self.proximoCursor()

	def erreiResposta(self):
		indice_ordem_pergunta = 2

		self.flashcards[self.cursor][indice_ordem_pergunta] -= 1

		self.proximoCursor()
