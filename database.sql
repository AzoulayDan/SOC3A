DROP TABLE IF EXISTS Compte CASCADE;

CREATE TABLE Compte(
	id			SERIAL PRIMARY KEY,
	login		Varchar(25),
	password	Varchar(25),
	role 		Varchar(25)
);

INSERT INTO Compte(login, password, role) VALUES('babar', 'merde', 'admin')