from datetime import date, datetime


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

def dia_da_semana():
	dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]

	return dias[datetime.today().weekday()]


def dia_da_semana_indice():
	return datetime.today().weekday()


def hojeFormatado():
	today = date.today() 

	return f"{today.year}-{today.month}-{today.day}"


def diaDaSemanaData(data):
	dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]

	data = data.split("/")

	return dias[date(year=int(data[2]), month=int(data[1]), day=int(data[0])).weekday()]


def dataFormatada(data):
	data = data.split('/')

	return f"{data[2]}-{data[1]}-{data[0]}"