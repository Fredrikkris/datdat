import sqlite3
import hashlib
import os
from tracemalloc import start
from typing import Tuple
import hmac

con = sqlite3.connect("coffee.db")
cursor = con.cursor()

pw_hash_dict = {}
salt_dict = {}



def velkommen():
    handling = input("Hvilken brukerhistorie vil du teste? (1-5)")

def hash_new_password(password: str) -> Tuple[bytes, bytes]:
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    print(is_correct_password(salt, pw_hash, password))
    return salt, pw_hash

def is_correct_password(salt: bytes, pw_hash: bytes, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

def registrer():
    epost = input("Skriv inn e-postadresse: ")
    fulltnavn = input("Skriv inn Fullt Navn: ")
    passord = input("Skriv inn passord: ")
    passord2 = input("Skriv inn passordet en gang til: ")
    while (passord != passord2):
        print("Dette var rart. Prøv på nytt")
        passord = input("Skriv inn passord: ")
        passord2 = input("Skriv inn passordet en gang til: ")
    salt, hashedPas = hash_new_password(passord)
    salt_dict[epost] = salt
    pw_hash_dict[epost] = hashedPas
    print(epost, fulltnavn, passord, hashedPas)
    

    cursor.execute('''INSERT INTO Bruker (Epost, Fornavn, Etternavn, Passord, salt) 
    VALUES (''' + epost + ", " + fulltnavn +", " + fulltnavn + ", " + hashedPas + ", " + salt +')')
    con.commit()
    velkommen()

def login():
    loggedin = False
    while (loggedin == False):
        epost = input("Skriv inn epost: ")
        passord = input("Passord: ")

        if(epost not in pw_hash_dict):
            print("Feil E-post")
        else:
            if (is_correct_password(salt_dict[epost], pw_hash_dict[epost], passord)):
                loggedin = True
    
    velkommen()
                
"""startmeny = input("Login eller Registrer (L/R): ")
if (startmeny == "L"):
    login()
else:
    registrer()"""


def bh1():
    brenneri = input("Skriv inn navn på brenneri: ")
    kaffenavn = input("Skriv inn et kaffenavn: ")
    poeng = input("Hva rater du kaffen? (0-10) ")
    smaksnotat = input("Si litt om kaffen: ")
    cursor.execute("INSERT INTO Brenneri (Navn) VALUES (:brenneri);", {"brenneri":brenneri})
    
    con.commit()

bh1()

con.close()
    
    










