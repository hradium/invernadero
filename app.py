import mysql.connector
from dueno import Dueno
from menudueno import MenuDueno
from menuinvernadero import MenuInvernadero
from menuusuario import MenuUsuario
from menuplanta import MenuPlanta
from menuregistro import MenuRegistro
conexion = mysql.connector.connect(user='carlos',password='12345',database='invernadero')
cursor = conexion.cursor()

while True:
	print("1) Menu Dueño")
	print("2) Menu Invernadero")
	print("3) Menu Usuario")
	print("4) Menu Planta")
	print("5) Menu Registro")
	print("0) Salir")
	op=input()
	
	if op == "1":
		menuD = MenuDueno(conexion, cursor)
	elif op == "2":
		menuI=MenuInvernadero(conexion, cursor)
	elif op == "3":
		menuU=MenuUsuario(conexion, cursor)
	elif op == "4":
		menuP=MenuPlanta(conexion, cursor)
	elif op == "5":
		menuR = MenuRegistro(conexion, cursor)
	elif op == "0":
		break
