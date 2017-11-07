#-*- encoding:utf-8 -*-
from flask import Flask, make_response
from flask_cors import CORS
import json
from databaseManager import *

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/')
def index():
	coucou = check_account('hello', 'babar', 'admin')
	print(coucou);

	resp = make_response(json.dumps({'hello':'hello world', 'babar':coucou}))
	resp.mimetype = 'application/json'
	return resp


########################
# Initialisation BDD
########################
@app.route('/debug/db/reset')
def init_db():
	'''
	Initialisation de la base de données
	'''
	db = Db()
	db.executeFile('database.sql')
	db.close()
	return 'Database OK'

########################
# Methodes GET
########################
@app.route('/admin/connect', methods=['GET'])
def connect_admin():
	'''
	Cette route est appelée lors de la connection de
	l'administrateur de la solution.
	'''
	return 'connexion de admin'

@app.route('/admin/teams', methods=['GET'])
def get_infos_teams():
	'''
	Cette route est appelée lorsque l'administrateur
	de la solution désire l'ensemble des informations
	concernant les différentes teams.
	'''
	return 'différentes teams'

@app.route('/admin/teams/<team>', methods=['GET'])
def get_infos_team():
	'''
	Cette route est appelée lorsque l'administrateur
	de la solution désire l'ensemble des informations
	concernant une team.
	'''
	return 'infos a propos de une seule team'

@app.route('/game/connect/', methods=['GET'])
def connect_player():
	'''
	Cette route est appelée lorsqu'un joueur se 
	connecte à une team en particulier.
	Le client envoie ainsi au serveur l'équipe qu'il 
	rejoins, et son nom propre à lui.
	'''
	return 'connexion à une team pour le jeu'

@app.route('/game/mission/<team>', methods=['GET'])
def get_mission(team):
	'''
	Cette route est appelée lorsque l'on envoie une
	au client une mission pour une équipe en
	particulier.
	'''
	return 'envoyer une mission à une équipe en particulier'


########################
# Methodes POST
########################
@app.route('/game/team/create_account', methods=['POST'])
def create_account():
	'''
	Cette route est appelée lorsque une équipe crée
	son compte afin de jouer.
	'''
	return 'une equipe nouvelle est crée dans le jeu'

@app.route('/game/validate_photo/<team>', methods=['POST'])
def validate_picture(team):
	'''
	Cette route est appelée lorsque le client vérifie
	si la photo qu'il a pris a été correcte ou non.
	A mettre ici l'analyse d'image ou non (reste à voir)
	'''
	return 'valider une image ici'

if __name__ == '__main__':
	app.run()

