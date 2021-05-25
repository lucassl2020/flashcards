import pickle
import os
from datetime import timedelta, date

class Int():
	def __init__(self):
		self.valor = 10

	def mudar_valor(self, valor):
		self.valor = valor
'''
a = Int()

filehandler = open("alo.obj", 'w') 
pickle.dump(a, filehandler)

a.mudar_valor(5)

filehandler = open("alo2.obj", 'w') 
pickle.dump(object, filehandler)

filehandler = open ("alo.obj", 'rb') 
a1 = pickle.load (filehandler)

filehandler = open ("alo2.obj", 'rb') 
a2 = pickle.load (filehandler)


filehandler = open ("flashcards\\Alou.obj", 'rb') 
a = pickle.load(filehandler)
print(a.flashcards)

filehandler = open ("flashcards\\a.obj", 'rb') 
a = pickle.load(filehandler)
print(a.flashcards)
print(a.datas)
a = os.listdir("flashcards")

print(a)

date_required = date.today() + timedelta(days=5)

if date.today() > date_required:
	print("É MENTIRA")
else:
	print("SERÁ")
'''

filehandler = open("flashcards\\teste.obj", 'rb') 
a = pickle.load(filehandler)

print(a.flashcards)
print(a.datas)

a.datas = [date.today() + timedelta(days=0)]

filehandler = open("flashcards\\teste.obj", 'wb') 
pickle.dump(a, filehandler)


