from math import dist
import os

import CONSTANTES
from fonctions_utiles import ajouter_caracteres_non_lettres
import vigenere
import cesar
import affine

def menu():
  print("")
  print("Que voulez-vous faire ?")
  print("----------")
  print("[0] déchiffrer un texte tt seul")
  print("[1] déchiffrer le fichier 1 (affine)")
  print("[2] déchiffrer le fichier 2 (vigenere)")
  print("[3] déchiffrer le fichier 3 (hill?) ")
  print("[4] déchiffrer le fichier 4 (cesar)")
  print("[5] déchiffrer le fichier 5 (substitution)")
  print("[6] quitter")
  print("----------")

def clear_terminal():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


def full_auto():
  inputTexte = input("Rentrer le texte à décrypter :")
  inputTexte = inputTexte.upper()
  clear_terminal()
  dico = dict()

  resultatAffine = affine.casser_affine_auto(inputTexte)
  affineT = resultatAffine[0]
  affineCle = resultatAffine[1]
  
  resutatVigenere = vigenere.vigenere_decode_auto(inputTexte)
  vigenereT = resutatVigenere[0]
  vigenereCle = resutatVigenere[1]

  resultatCesar = cesar.decode_cesar_auto(inputTexte)
  cesarT = resultatCesar[0]
  cesarCle = resultatCesar[1]

  dico[affineT] = "affine"
  dico[vigenereT] = "vigenere"
  dico[cesarT] = "cesar"

  distance = affine.calcul_distance(dico)
  texte = affine.distance_la_plus_petite(distance)
  texte = ajouter_caracteres_non_lettres(inputTexte,texte)
  for elem in dico:
    if elem == texte:
      print("Le texte est : " + elem)
      print("Le chiffrement utilisé est : " + dico[elem])
      if dico[elem] == "affine":
        print("La clé est : " + str(affineCle))
      if dico[elem] == "cesar":
        print("La clé est : " + str(cesarCle))
      if dico[elem] == "vigenere":
        print("La clé est : " + str(vigenereCle))

def terminal():
  boucle = True
  while(boucle):
    menu()
    input1 = input("Rentrer le numéro voulu :")
    clear_terminal()
    match input1:
      case "0":
        full_auto()
      case "1":
        print(affine.casser_affine_auto(CONSTANTES.TEXTE_1))
      case "2":
        print(vigenere.vigenere_decode_auto(CONSTANTES.TEXTE_2))
      case "3":
        print("3")
      case "4":
        print(cesar.decode_cesar_auto(CONSTANTES.TEXTE_4))
      case "5":
        print("5")
      case "6":
        boucle = False  
      case _:
        print("Erreur")

terminal()