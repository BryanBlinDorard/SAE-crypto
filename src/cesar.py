import math
from fonctions import *
from string import ascii_uppercase

FR_FREQ = {'A':9.42,'B':1.02,'C':2.64,'D':3.39,'E':15.87,'F':0.95,'G':1.04,'H':0.77,
'I':8.41,'J':0.89,'K':0.00,'L':5.34,'M':3.24,'N':7.15,'O':5.14,'P':2.86,'Q':1.06,
'R':6.46,'S':7.90,'T':7.26,'U':6.24,'V':2.15,'W':0.00,'X':0.30,'Y':0.24,'Z':0.32}

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode_cesar(text, key):
  """chiffrement de césar

  Args:
      text (str): texte à chiffrer
      key (int): clé de chiffrement 

  Returns:
      str: texte chiffré
  """
  text = clear(text)
  result = ""
  for letter in text:
      if letter in alphabet:
          result += alphabet[(alphabet.index(letter) + key) % len(alphabet)]
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
  text = clear(text)
  result = dict()
  for letter in alphabet:
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
  
  cpt=0 #compteur de lettre

  distance=dict() #dictionnaire des distances

  #calcul de la fréquence de chaque lettre et pour chaque indice de décalage
  for i in range(26):
    phrase = encode_cesar(text,i)
    tableau_freq=calculer_frequence_lettre(phrase)
    # print(tableau_freq)
    tableau_de_freq_global[cpt]=tableau_freq
    cpt+=1
  
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

def decode_cesar(text):
  """Décryptage code de césar 

  Args:
      text (str): texte à décrypter

  Returns:
      str: texte décrypté
  """
  cle = cle_cesar(text)
  # print(cle)
  return encode_cesar(text,cle)

def vrai_cle(cle):
  return 26-cle

print(decode_cesar(clear("Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj.Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr.")))