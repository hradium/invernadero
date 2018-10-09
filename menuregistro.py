from registro import Registro
from datetime import datetime, date

class MenuRegistro:
	def __init__(self, conexion, cursor):
		self.registro = Registro(conexion, cursor)
		
		while True:
			print("1) Agregar Registro")
			print("2) Mostrar Registro")
			print("0) Salir")
			op = input()
		
			if op == '1':
				self.agregar()
			elif op== '2':
				self.buscar()
			elif op == '0':
				break
			
	def agregar(self):
		#cultivo = input("Cultivo: ")
		#fecha = datetime.now().date()
		dia = input("Dia: ")
		mes = input("Mes: ")
		year = input("Año: ")
		fecha = date(int(year), int(mes), int(dia))
		ph = input("pH: ")
		luz = input("Luz: ")
		humedad = input("Humedad: ")
		co2 = input("CO2: ")
		id_planta = input("Id Planta: ")
		#id_clasi = input("Id Clasificacion: ")
		self.registro.agregar(fecha, ph, luz, humedad, co2, id_planta)
	
	def buscar(self):
		id_planta = input("Id Planta: ")
		resultados = self.registro.buscar(id_planta)
		
		for p in resultados:
			print("{0:3} {1:5} {2:5} {3:5} {4:5} {5:5} {6:5}".format(p[0], str(p[1]), p[2], p[3], p[4], p[5], p[6]))