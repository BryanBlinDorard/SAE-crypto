import os

from CONSTANTES import *
from vigenere import *
from cesar import *

def menu():
  print("----------")
  print("[1] déchiffrer le fichier 1 (affine)")
  print("[2] déchiffrer le fichier 2 (vigenere)")
  print("[3] déchiffrer le fichier 3 (hill?) ")
  print("[4] déchiffrer le fichier 4 (cesar)")
  print("[5] déchiffrer le fichier 5 (substitution)")
  print("[6] quitter")
  print("----------")

def clear_terminal():
  os.system('cls')
  

def terminal():
  boucle = True
  while(boucle):
    menu()
    input1 = input("Rentrer le numéro voulu :")
    clear_terminal()
    match input1:
      case "1":
        print("1")
      case "2":
        print(vigenere_decode_auto(TEXTE_2))
      case "3":
        print("3")
      case "4":
        print(decode_cesar_auto(TEXTE_4))
      case "5":
        print("5")
      case "6":
        boucle = False  
      case _:
        print("Erreur")

terminal()