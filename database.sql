DROP TABLE IF EXISTS Account CASCADE;

CREATE TABLE Account(
	id			SERIAL PRIMARY KEY,
	login		Varchar(25),
	password	Varchar(25),
	role 		Varchar(25)
);

INSERT INTO Account(login, password, role) VALUES('babar', 'merde', 'admin')