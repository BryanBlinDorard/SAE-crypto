from cesar import *
from fonctions_utiles import *
import math
import CONSTANTES



def encode_vigenere(texte: str, cle: str) -> str:
  """chiffrement de vigenere

  Args:
    c (str: le message à chiffrer sous forme de chaine de caractères
    cle (str): la clé à utiliser sous forme de chaine de caractères
  Returns:
    str: Elle retourne le message chiffré sous forme de chaine de caractères
  """
  texte = texte.upper()
  cle = cle.upper()
  longueur_texte = len(texte)
  indice_de_la_cle = 0
  message_encode = ""

  for i in range(0, longueur_texte):
    if 'A' <= texte[i] <= 'Z':
      convertionTexte = (ord(texte[i]) - ord('A')) #convertion du texte en nombre
      convertionCle = (ord(cle[indice_de_la_cle]) - ord('A')) #convertion de la clé en nombre
      message_encode += chr(((convertionTexte + convertionCle) % 26) + ord('A')) #convertion du message chiffré en lettre
      indice_de_la_cle = (indice_de_la_cle + 1) % len(cle)
    else:
        message_encode +=  texte[i]
  return message_encode


def decode_vigenere(texte: str, cle:str) -> str: 
  """déchiffrement de vigenere

  Args:
      texte (str): le message à déchiffrer sous forme de chaine de caractères
      cle (str): la clé à utiliser sous forme de chaine de caractères

  Returns:
      str: Elle retourne le message déchiffré sous forme de chaine de caractères
  """
  texte = texte.upper()
  cle = cle.upper()
  longueur_texte = len(texte)
  indice_de_la_cle = 0
  message_encode = ""

  for i in range(0, longueur_texte):
      if 'A' <= texte[i] <= 'Z':
        convertionTexte = (ord(texte[i]) - ord('A'))
        convertionCle = (ord(cle[indice_de_la_cle]) - ord('A'))
        message_encode += chr(((convertionTexte - convertionCle ) % 26) + ord('A')) 
        indice_de_la_cle = (indice_de_la_cle + 1) % len(cle)
      else:
          message_encode +=  texte[i]
  return message_encode



# ------------------------------------------------------------------------#
# TROUVER LA TAILLE DE LA CLE



def diviser_texte(texte: str, nb_de_part) -> list:
  """divise le texte en nb_de_part

  Args:
      texte (str): le texte à diviser
      nb_de_part (int): le nombre de partie dans lequel on veut diviser le texte

  Returns:
      list: la liste des parties du texte
  """
  dict = {}
  for i in range(nb_de_part):
    dict[i] = ""
  for i in range(len(texte)):
    dict[i%nb_de_part] += texte[i]
  return dict  
    


def analyse_seq(txt:str, taille=2):
  """analyse de la sequence

  Args:
      txt (str): _description_
      taille (int, optional): taille de la sequence. Defaut a 2.

  Returns:
      dict: renvoie les distances
  """
  dict = {}
  dict_distance = {}
  for i in range(len(txt)):
    texte = txt[i:i+taille]
    if texte not in dict:
      dict[texte] = i
    else:
      if dict[texte] != False:
        var = dict[texte]
        dict[texte] = False
        dict_distance[texte] = i - var
  return dict_distance


def diviseur_du_nombre(valeur):
  liste = []
  for i in range(2, valeur):
    if valeur % i == 0:
      liste.append(i)
  return liste


def diviseur_commun(dict):
  liste_diviseur = []
  dict_frq = {}
  for val in dict:
    liste_diviseur.append(diviseur_du_nombre(dict[val]))
  for i in range(len(liste_diviseur)):
    for elem2 in liste_diviseur[i]:
      if elem2 not in dict_frq:
        dict_frq[elem2] = 1
      else:
        dict_frq[elem2] += 1
  return dict_frq


def rechercher_max(dict):
  # print(dict)
  max = 0
  cle = None
  for elem in dict:
    if dict[elem] > max and elem not in [2,3,4]:
      max = dict[elem]
      cle = elem
  return cle


#--------------------------------------------------------------------------------#
# TROUVER LA CLE

def cesar_vig(message,décalage):
    # effectue le decalage d sur les caracteres de message
    chiffre=''
    for caractere in message:
        chiffre += decalage_lettre(caractere,-décalage)
    return chiffre

def decalage_lettre(caractere,indice):
    # decale une lettre majuscule. Les autres caracteres ne sont pas modifies
    car = ord(caractere.upper())
    car += indice
    while car>90:
        car -= 26
    while car<65:
        car += 26
    return chr(car)

def clef(texte,longueur_cle):
  """permet de trouver la clé

  Args:
      texte (str): le message à déchiffrer
      longueur_cle (int): la longueur de la clé

  Returns:
      str: la clé
  """
  cle = ""
  taille_cle = 0
  for taille_cle in range(longueur_cle):
      partiel = ""
      variable = 0
      while taille_cle+variable < len(texte):
          partiel += texte[taille_cle+variable]
          variable += longueur_cle
      long_message = len(partiel)
      ecart_minimal = 100000000
      for d in range(26):
          ecart = 0.0
          chiffre = cesar_vig(partiel,d)
          frequences = calc_freq(chiffre)
          for i in range(26):
              ecart += abs(frequences[i]/long_message-CONSTANTES.HISTOGRAMME[i])
          if ecart<ecart_minimal:
              ecart_minimal = ecart
              decalage = d
      cle += chr(decalage+65)
  return cle

# ------------------------------------------------------------------------#
# DECHIFFREMENT AUTOMATIQUE

def vigenere_decode_auto(message_chiffre: str) -> str:
  """déchiffrement de vigenere

  Args:
    c (str: le message à déchiffrer sous forme de chaine de caractères
  """
  dict = {}

  message_chiffre = message_chiffre.upper()
  texte = message_chiffre
  message_chiffre = supprimer_caracteres_non_lettres(message_chiffre)


  dict1 = analyse_seq(message_chiffre,2)
  dict2 = analyse_seq(message_chiffre,3)
  dict = (dict1 | dict2)

  diviseur_communs = diviseur_commun(dict)
  taille_cle = rechercher_max(diviseur_communs)

  la_cle = clef(message_chiffre,taille_cle) # la clé est trouvée
  res = decode_vigenere(message_chiffre,la_cle) # le message est déchiffré

  res = ajouter_caracteres_non_lettres(texte,res) # on remet les caracteres non lettres

  print("la clef est : ",la_cle)
  print("le message est : ")
  return res