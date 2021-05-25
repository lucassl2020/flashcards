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



nome = "1111"
data = date.today() + timedelta(days=0)

objeto = abrirObjeto(nome)

printObjeto(objeto)

objeto.datas = [data, data]

printObjeto(objeto)

salvarObjeto(objeto, nome)
