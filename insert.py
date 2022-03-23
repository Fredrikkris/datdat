import sqlite3
import hashlib

con = sqlite3.connect("coffee.db")
cursor = con.cursor()

tables = ["Brenneri", "Gård", "Kaffe", "Vurdering", "KaffeParti", "Kaffebønne", "Foredlingsmetode", "DyrkesAv", "Bruker", "BestårAv"]
cursor.execute("DELETE FROM sqlite_sequence")
con.commit()
for table in tables:
    cursor.execute("DELETE FROM %s" %table)
    con.commit()

cursor.execute('''INSERT INTO Brenneri (Navn) VALUES ("Jacobsen & Svart");''')
cursor.execute('''INSERT INTO Brenneri (Navn) VALUES ("Thomas");''')
cursor.execute('''INSERT INTO Brenneri (Navn) VALUES ("Fredrik & Co");''')


cursor.execute('''INSERT INTO Gård (Navn, MOH, Land, Region) VALUES ("Costa del Sol", 100, "Paraguay", "San Pedro");''')
cursor.execute('''INSERT INTO Gård (Navn, MOH, Land, Region) VALUES ("Hamza el Hamdallah", 800, "Paraguay", "Amambay");''')
cursor.execute('''INSERT INTO Gård (Navn, MOH, Land, Region) VALUES ("El Negro des Coffee", 553, "Angola", "Lunda Sul");''')
cursor.execute('''INSERT INTO Gård (Navn, MOH, Land, Region) VALUES ("Nombre de Dios", 1500, "El Salvador", "Santa Ana");''')
cursor.execute('''INSERT INTO Gård (Navn, MOH, Land, Region) VALUES ("Gåros Colombus", 723, "Colombia", "El Colomb");''')
cursor.execute('''INSERT INTO Gård (Navn, MOH, Land, Region) VALUES ("Gåros Rwandur", 321, "Rwanda", "El Rwandus");''')


cursor.execute('''INSERT INTO Kaffebønne (Art) VALUES ("coffea arabica");''')
cursor.execute('''INSERT INTO Kaffebønne (Art) VALUES ("coffea robusta");''')
cursor.execute('''INSERT INTO Kaffebønne (Art) VALUES ("coffea liberica");''')


cursor.execute('''INSERT INTO Foredlingsmetode (Navn, Beskrivelse) VALUES ("Bærtørket", "tørker i bær");''')
cursor.execute('''INSERT INTO Foredlingsmetode (Navn, Beskrivelse) VALUES ("Vasket", "vasket i rent edelmetall");''')
cursor.execute('''INSERT INTO Foredlingsmetode (Navn, Beskrivelse) VALUES ("soltørket", "tørket i stekende solbris");''')

cursor.execute('''INSERT INTO Kaffe (Brenningsgrad, Navn, Beskrivelse, Kilopris, BrenneriID, PartiID) 
VALUES ("lys", "Vinterkaffe", "En velsmakende og kompleks kaffe for mørketiden", 600, 1, 1);''')
cursor.execute('''INSERT INTO Kaffe (Brenningsgrad, Navn, Beskrivelse, Kilopris, BrenneriID, PartiID) 
VALUES ("mørk", "mørkekaffe", "Skikkelig mørk for dem som liker det mørk da", 2000, 2, 2);''')
cursor.execute('''INSERT INTO Kaffe (Brenningsgrad, Navn, Beskrivelse, Kilopris, BrenneriID, PartiID) 
VALUES ("middels", "Tropekaffe", "En tropisk kaffe med smak av alle jungelens frukter og bær. For den lekende sjel.", 200, 3, 3);''')


cursor.execute('''INSERT INTO Kaffeparti (Innhøstningsår, Kilopris, GårdID, ForedlingsID) VALUES (2021, 8, 4, 1);''')
cursor.execute('''INSERT INTO Kaffeparti (Innhøstningsår, Kilopris, GårdID, ForedlingsID) VALUES (2015, 5, 2, 3);''')


cursor.execute('''INSERT INTO Bruker (Epost, Fornavn, Etternavn, Passord, salt) VALUES ("Fredrakr@gmail.com","Fredrik", "Augustus", "fredrik123", "salt");''')
cursor.execute('''INSERT INTO Bruker (Epost, Fornavn, Etternavn, Passord, salt) VALUES ("Magnua2304@gmail.com","Magnus", "Skribeland", "magnus123", "salt");''')
cursor.execute('''INSERT INTO Bruker (Epost, Fornavn, Etternavn, Passord, salt) VALUES ("thomas@gmail.com","Thomas", "Fagerli", "thomas123", "salt");''')





#cursor.execute()






con.commit()
for row in cursor.execute("SELECT * FROM Brenneri"):
    print(row)
con.close()