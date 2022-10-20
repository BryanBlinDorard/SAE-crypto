import math

import CONSTANTES

from fonctions_utiles import ajouter_caracteres_non_lettres, supprimer_caracteres_non_lettres

FR_FREQ = {'A':9.42,'B':1.02,'C':2.64,'D':3.39,'E':15.87,'F':0.95,'G':1.04,'H':0.77,
'I':8.41,'J':0.89,'K':0.00,'L':5.34,'M':3.24,'N':7.15,'O':5.14,'P':2.86,'Q':1.06,
'R':6.46,'S':7.90,'T':7.26,'U':6.24,'V':2.15,'W':0.00,'X':0.30,'Y':0.24,'Z':0.32}


def encode_cesar(text, key):
  """chiffrement de césar

  Args:
      text (str): texte à chiffrer
      key (int): clé de chiffrement 

  Returns:
      str: texte chiffré
  """
  result = ""
  for letter in text:
      if letter in CONSTANTES.ALPHABET:
          result += CONSTANTES.ALPHABET[(CONSTANTES.ALPHABET.index(letter) + key) % len(CONSTANTES.ALPHABET)]
      else:
          result += letter
  return result


def calculer_frequence_lettre(text):
  """Calcule la fréquence d'apparition de chaque lettre dans le texte

  Args:
      text (str): texte à analyser

  Returns:
      dict: dictionnaire des fréquences
  """
  result = dict()
  for letter in CONSTANTES.ALPHABET:
      result[letter] = text.count(letter) / len(text) 
  return result

def cle_cesar(text):
  """Analyse fréquencielle pour décryptage code de césar

  Args:
      text (str): texte à analyser

  Returns:
      int: clé de chiffrement
  """
  tableau_de_freq_global=dict()
  cpt_de_lettre=0
  distance=dict() #dictionnaire des distances

  #calcul de la fréquence de chaque lettre et pour chaque indice de décalage
  for i in range(26):
    phrase = encode_cesar(text,i)
    tableau_freq=calculer_frequence_lettre(phrase)
    # print(tableau_freq)
    tableau_de_freq_global[cpt_de_lettre]=tableau_freq
    cpt_de_lettre+=1
  
  #calcul de la distance entre la fréquence de chaque lettre et la fréquence globale
  for sous_tableau_frequence in tableau_de_freq_global:
    calcul=0
    for lettre in tableau_de_freq_global[sous_tableau_frequence]:
      calcul+=(FR_FREQ[lettre]-tableau_de_freq_global[sous_tableau_frequence][lettre])**2
    calcul=math.sqrt(calcul)  
    # print(calcul)
    distance[sous_tableau_frequence]=calcul

  for cle in distance:
    if distance[cle]==min(distance.values()):
      return cle  

def decode_cesar_auto(text):
  """Décryptage code de césar 

  Args:
      text (str): texte à décrypter

  Returns:
      str: texte décrypté
  """
  text = text.upper()
  texte = supprimer_caracteres_non_lettres(text)
  cle = cle_cesar(texte)
  # print(cle)
  res = encode_cesar(texte,cle)
  res = ajouter_caracteres_non_lettres(text,res)
  print("la clef est : ",vrai_cle(cle))
  return res

def vrai_cle(cle):
  return 26-cle
