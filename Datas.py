from datetime import date


def hoje():
	today = date.today() 

	hoje_inteiro = today.year * 100
	hoje_inteiro += today.month
	hoje_inteiro *= 100
	hoje_inteiro += today.day

	return hoje_inteiro

def hojeSplit():
	today = date.today() 

	return today.year, today.month, today.day

def data(ano, mes, dia):
	data_inteiro = ano * 100
	data_inteiro += mes
	data_inteiro *= 100
	data_inteiro += dia

	return data_inteiro
