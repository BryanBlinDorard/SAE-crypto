from string import ascii_uppercase

def clear(texte:str) -> str:
    texte = texte.upper()
    new_texte = ''.join(carac for carac in texte if carac.isalnum())
    return new_texte

def frequences(chaine):
    freq = [0] * 26
    for c in chaine:
        if c in ascii_uppercase:
            freq[ord(c) - ord('A')] += 1
    somme=sum(freq)
    freq=[v / somme * 1000.0 for v in freq]
    return freq


def PGCD(val1: int,val2: int) -> int:
	"""Renvoie le PGCD de deux nombres entiers

	Args:
		val1 (int): le premier nombre
		val2 (int): le deuxième nombre

	Returns:
		int: le PGCD des deux nombres
	"""
	while val2 != 0:
		val1, val2 = val2, val1 % val2
	return val1

def calc_freq(texte):
    tab_freq = [0]*26
    for c in texte:
        tab_freq[ord(c)-65] += 1  
    return tab_freq