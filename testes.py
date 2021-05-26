import pickle
import os
from datetime import timedelta, date


def abrirObjeto(nome):
	filehandler = open("flashcards\\" + nome + ".obj", 'rb') 
	objeto = pickle.load(filehandler)
	filehandler.close()

	return objeto	

def printObjeto(objeto):
	print(objeto.flashcards)
	print(objeto.datas)
	print()

def salvarObjeto(objeto, nome):
	filehandler = open("flashcards\\" + nome + ".obj", 'wb') 
	pickle.dump(objeto, filehandler)
	filehandler.close()


#nomes_e_dias = (["1", 0], ["2", 0], ["3", 0])
nomes_e_dias = (["1", 0], ["1", 0])

for nome, dia in nomes_e_dias:
	data1 = date.today() + timedelta(days=dia)
	data2 = date.today() + timedelta(days=dia-1)

	objeto = abrirObjeto(nome)

	printObjeto(objeto)

	objeto._datas = [data1, data2]

	printObjeto(objeto)

	salvarObjeto(objeto, nome)
