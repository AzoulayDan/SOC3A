#-*- encoding:utf-8 -*-
from db import Db

def check_account(login, password, role):
	'''
	Cette fonction permet de vérifier que la team existe ou non.
	Valeur de retour:
		* -1 dans le cas où la team n'existe pas.
		* 0 dans le cas où la team existe.
	'''
	number = 0
	db = Db()
	print('passage ici')
	count = db.select("SELECT COUNT(*) FROM Account WHERE (login = %s AND password = %s AND role = %s)" %(login, password, role))
	print('passage la')

	if (count == 0):
		number = -1
	else:
		number = 0
	db.close()
	return number


