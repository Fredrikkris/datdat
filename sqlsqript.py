import sqlite3
con = sqlite3.connect("coffee.db")
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Kaffe ( 
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Brenningsgrad TEXT CHECK( Brenningsgrad IN ('mørk','middels','lys')) NOT NULL,
    Navn VARCHAR(65) NOT NULL,
    Beskrivelse VARCHAR(655) DEFAULT NULL,
    Kilopris DOUBLE NOT NULL,
    BrenneriID INTEGER NOT NULL,
    PartiID INTEGER NOT NULL,
    FOREIGN KEY (BrenneriID) REFERENCES Brenneri (ID),
    FOREIGN KEY (PartiID) REFERENCES Parti (ID)
);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Vurdering (
    KaffeID INTEGER NOT NULL,
    BrukerID INTEGER NOT NULL,
    Dato DATE DEFAULT NULL,
    Notat VARCHAR(655) DEFAULT NULL,
    Poeng INTEGER NOT NULL,
    CHECK (Poeng BETWEEN 1 AND 10),
    PRIMARY KEY (KaffeID, BrukerID),
    FOREIGN KEY (KaffeID) REFERENCES Kaffe (ID),
    FOREIGN KEY (BrukerID) REFERENCES Bruker (ID)
);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Foredlingsmetode (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(65) NOT NULL,
    Beskrivelse VARCHAR(655) DEFAULT NULL
);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS BestårAv (
  	PartiID INTEGER NOT NULL,
    BønneID INTEGER NOT NULL,
    PRIMARY KEY (PartiID, BønneID),
    FOREIGN KEY (PartiID) REFERENCES Parti (ID),
    FOREIGN KEY (BønneID) REFERENCES Kaffebønne (ID)
);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Kaffeparti (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Innhøstningsår YEAR NOT NULL,
    Kilopris DOUBLE NOT NULL,
    GårdID INTEGER NOT NULL,
    ForedlingsID INTEGER NOT NULL,
    FOREIGN KEY (GårdID) REFERENCES Gård (ID),
    FOREIGN KEY (ForedlingsID) REFERENCES Foredlingsmetode (ID)
);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Gård(
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(65) NOT NULL,
    MOH INTEGER NOT NULL,
    Land VARCHAR(65) NOT NULL,
    Region VARCHAR (65) NOT NULL,
    CHECK (MOH BETWEEN -500 AND 9000)
);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Bruker (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Epost VARCHAR(319) NOT NULL UNIQUE,
    Fornavn VARCHAR(255) NOT NULL,
    Etternavn VARCHAR(255) NOT NULL,
    Passord REAL NOT NULL,
    Salt REAL NOT NULL
);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Brenneri (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(255) NOT NULL
);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Kaffebønne (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Art VARCHAR(255) NOT NULL UNIQUE
);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS DyrkesAv (
	BønneID INTEGER NOT NULL,
    GårdID INTEGER NOT NULL,
    PRIMARY KEY (BønneID, GårdID),
    FOREIGN KEY (BønneID) REFERENCES Kaffebønne (ID),
    FOREIGN KEY (GårdID) REFERENCES Gård (ID)
);""")




for row in cursor.execute("SELECT * FROM Brenneri"):
    print(row)
con.close()
