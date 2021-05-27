from random import shuffle
class ObjetoRevisao():
	def __init__(self):
		self.objetoFlashcards = None
		self.flashcards = []
		self.cursor = 0
		self.ciclo = 0
		self.max_ciclo = 0
		self.modo = -1 # Sem modo

	def new(self):
		self.objetoFlashcards = None
		self.flashcards = []
		self.cursor = 0
		self.ciclo = 0
		self.max_ciclo = 0
		self.modo = -1 # Sem modo

	def adicionarAoMaxCiclo(self, qtd):
		if qtd < 1:
			self.max_ciclo = 1
		else:
			self.max_ciclo = qtd

	def copiarFlashcardsLista(self):
		for pergunta, resposta in self.objetoFlashcards.flashcards.items():
			self.flashcards.append([pergunta, resposta, 0])

		shuffle(self.flashcards)

	def proximoCursor(self):
		modo_revisao_ordenar = 1
		modo_revisao_retirar = 2

		self.cursor += 1

		if self.cursor >= len(self.flashcards):
			if self.modo == modo_revisao_ordenar:
			    self.flashcards = sorted(self.flashcards, key=lambda flashcards: flashcards[indice_ordem_pergunta]) 
			elif self.modo == modo_revisao_retirar:
				if len(self.flashcards) == 0:
					self.ciclo = self.max_ciclo

			self.cursor = 0
			self.ciclo += 1

	def acabouRevisao(self):
		if self.ciclo >= self.max_ciclo:
			return True
		return False

	def acerteiResposta(self):
		modo_revisao_ordenar = 1
		modo_revisao_retirar = 2

		if self.modo == modo_revisao_ordenar:
			self.flashcards[self.cursor][indice_ordem_pergunta] += 1
		elif self.modo == modo_revisao_retirar:
			del self.flashcards[self.cursor]

		self.proximoCursor()

	def erreiResposta(self):
		modo_revisao_ordenar = 1
		indice_ordem_pergunta = 2

		if self.modo == modo_revisao_ordenar:
			self.flashcards[self.cursor][indice_ordem_pergunta] -= 1

		self.proximoCursor()
