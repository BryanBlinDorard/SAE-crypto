
import math
import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "



PONCTUATION = [',' , ':' , ';' , '.' , "'" , '-' , '!' , '?',"(",")","[","]","{","}","/","<",">","«","»","'",'"',"0","1","2","3","4","5","6","7","8","9","\n"]
# Caractere indésirable

def correction(chaine : str) -> str:
    """Permet d'enlever la ponction et remplacer les minuscule, accent
        Args:
            str: text
        Return :
            str : text correct
    """
    accent_a = [192,224,226] # contient les lettre accentuée
    accent_c = [199,231] # contient les lettre accentuée
    accent_e = [200,201,202,232,233,234,235] # contient les lettre accentuée
    accent_i = [238,239] # contient les lettre accentuée
    accent_o = [244] # contient les lettre accentuée
    accent_u = [249,251,252] # contient les lettre accentuée

    s_sub = ""
    for caractere in chaine: # pour chaque lettre du texte
        if(ord(caractere) in range(97,123)):
            caractere = chr(ord(caractere)-32)
        if ord(caractere) in accent_a:
            caractere = "A" # remplace les lettre accentuée par leur lettre non accentuée
        if ord(caractere) in accent_c:
            caractere = "C"
        if ord(caractere) in accent_e:
            caractere = "E"
        if ord(caractere) in accent_i:
            caractere = "I"
        if ord(caractere) in accent_o:
            caractere = "O"
        if ord(caractere) in accent_u:
            caractere = "U"
        s_sub += caractere

    #Enlever la ponctuation
    for caractere in PONCTUATION:
        s_sub = s_sub.replace(caractere," ")
    return s_sub
def open_fichier(file : str) -> str:
    """
    Permet d'ouvrir un fichier
        Args:
            str: file
        Return :
            str : text
    """
    with open(file,"r") as fichier: # ouverture du fichier
        text = fichier.read() # lecture du fichier
    return text 

# On prend un texte et on analyse les bigrammes

def dico_occurence(text : str) -> dict:
    """ Renvoie un dictionaire avec les occurence de chaque lettre
        Args:
            str: text
        Return :
            dict : dictionnaire des occurence
    """
    dico = {} # dictionnaire des occurence
    for lettre in text: # pour chaque lettre du texte
        if lettre in dico: # si la lettre est déjà dans le dictionnaire
            dico[lettre] += 1 # on incrémente la valeur
        else:
            dico[lettre] = 1 # sinon on initialise la valeur à 1
    return dico

def dico_bigrams(text : str) -> dict:
    """Permet de créer un dictionnaire des bigrammes
        Args:
            str: file
        Return :
            dict : dictionnaire des bigrammes
    """
    dico = {}
    text = correction(text) # on corrige le texte
    # Pour chaque lettre noter la fréquance de la lettre suivante
    for i in range(len(text)-1):
        if text[i] not in dico: # si la lettre n'est pas dans le dictionnaire
            dico[text[i]] = {} # on l'ajoute
        if text[i+1] not in dico[text[i]]: # si la lettre suivante n'est pas dans le dictionnaire
            dico[text[i]][text[i+1]] = 0 # on l'ajoute
        dico[text[i]][text[i+1]] += 1 # on incrémente la valeur
    return dico

def dico_freq_bigrame(dico_bigrame,dico_occurence : dict) -> dict: 
    """Permet de créer un dictionnaire des frequence des bigrammes
        Args:
            dict: dico_bigrame
            dict: dico_occurence
        Return :
            dict : dictionnaire des bigrammes
    """
    dico = {} # dictionnaire des occurence
    for lettre in ALPHABET: # pour chaque lettre du texte
        dico[lettre] = {} # on l'ajoute
        for lettre2 in ALPHABET: # pour chaque lettre du texte
            dico[lettre][lettre2] = 0 # on l'ajoute

    for lettre in dico_bigrame: # pour chaque lettre du texte

        for lettre2 in dico_bigrame[lettre]: # pour chaque lettre du texte
            dico[lettre][lettre2] = round(dico_bigrame[lettre][lettre2]/dico_occurence[lettre]*100,2) # on l'ajoute
    return dico

#text = open_fichier("text_reference.txt")
#text = correction(text)
#r = dico_bigrams(text)
#f = dico_occurence(text)
#freq = dico_freq_bigrame(r,f)
#print(freq)

DICO_BIGRAME ={
    'A': {'A': 0.03, 'B': 1.62, 'C': 2.43, 'D': 0.93, 'E': 0.07, 'F': 0.35, 'G': 1.8, 'H': 0.18, 'I': 25.25, 'J': 0.19, 'K': 0.0, 'L': 3.47, 'M': 2.55, 'N': 14.48, 'O': 0.04, 'P': 2.15, 'Q': 0.43, 'R': 7.29, 'S': 4.7, 'T': 3.45, 'U': 7.12, 'V': 6.23, 'W': 0, 'X': 0.01, 'Y': 0.61, 'Z': 0.04, ' ': 14.58},
    'B': {'A': 8.32, 'B': 0.08, 'C': 0, 'D': 0.13, 'E': 15.24, 'F': 0, 'G': 0, 'H': 0.02, 'I': 16.87, 'J': 0.87, 'K': 0, 'L': 25.62, 'M': 0.05, 'N': 0, 'O': 12.88, 'P': 0, 'Q': 0, 'R': 14.32, 'S': 3.24, 'T': 0.35, 'U': 1.8, 'V': 0.03, 'W': 0, 'X': 0, 'Y': 0.03, 'Z': 0, ' ': 0.14}, 
    'C': {'A': 6.88, 'B': 0, 'C': 1.31, 'D': 0.04, 'E': 28.94, 'F': 0.01, 'G': 0.01, 'H': 15.52, 'I': 5.51, 'J': 0.01, 'K': 0.04, 'L': 2.11, 'M': 0.02, 'N': 0.0, 'O': 24.18, 'P': 0.01, 'Q': 0.07, 'R': 3.92, 'S': 0.18, 'T': 3.19, 'U': 3.73, 'V': 0.0, 'W': 0, 'X': 0, 'Y': 0.11, 'Z': 0.01, ' ': 4.2}, 
    'D': {'A': 11.01, 'B': 0.0, 'C': 0.02, 'D': 0.04, 'E': 53.2, 'F': 0, 'G': 0.01, 'H': 0.49, 'I': 9.28, 'J': 0.04, 'K': 0, 'L': 0.03, 'M': 0.54, 'N': 0.02, 'O': 6.45, 'P': 0.26, 'Q': 0.02, 'R': 3.06, 'S': 0.73, 'T': 0.16, 'U': 10.57, 'V': 0.01, 'W': 0, 'X': 0, 'Y': 0.12, 'Z': 0, ' ': 3.94}, 
    'E': {'A': 1.03, 'B': 0.18, 'C': 2.45, 'D': 0.74, 'E': 1.52, 'F': 0.58, 'G': 0.61, 'H': 0.09, 'I': 0.75, 'J': 0.27, 'K': 0.0,'L': 4.89, 'M': 3.69, 'N': 10.78, 'O': 0.32, 'P': 1.29, 'Q': 0.29, 'R': 7.75, 'S': 12.18, 'T': 7.99, 'U': 4.28, 'V': 1.25,'W': 0.0, 'X': 0.44, 'Y': 0.02, 'Z': 0.64, ' ': 35.98}, 
    'F': {'A': 24.93, 'B': 0, 'C': 0.01, 'D': 0.16, 'E': 13.8, 'F': 9.64, 'G': 0, 'H': 0, 'I': 13.74, 'J': 0, 'K': 0, 'L': 5.05, 'M': 0, 'N': 0, 'O': 17.16, 'P': 0, 'Q': 0, 'R': 9.51, 'S': 0.53, 'T': 0.06, 'U': 3.9, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, ' ': 1.5},
    'G': {'A': 10.8, 'B': 0, 'C': 0.02, 'D': 0.02, 'E': 34.41, 'F': 0.02, 'G': 0.18, 'H': 0.07, 'I': 7.72, 'J': 0, 'K': 0, 'L': 3.42, 'M': 0.16, 'N': 9.66, 'O': 4.58, 'P': 0, 'Q': 0, 'R': 17.16, 'S': 0.24, 'T': 1.91, 'U': 8.55, 'V': 0, 'W': 0, 'X': 0, 'Y': 0.13, 'Z': 0, ' ': 0.98},
    'H': {'A': 28.97, 'B': 0.02, 'C': 0.07, 'D': 0, 'E': 42.92, 'F': 0, 'G': 0, 'H': 0, 'I': 7.18, 'J': 0, 'K': 0, 'L': 0, 'M': 0.17, 'N': 0.07, 'O': 12.82, 'P': 0, 'Q': 0, 'R': 1.76, 'S': 0.05, 'T': 0.05, 'U': 2.72, 'V': 0, 'W': 0, 'X': 0, 'Y': 0.81, 'Z': 0, ' ': 2.39}, 
    'I': {'A': 1.05, 'B': 0.62, 'C': 1.6, 'D': 1.27, 'E': 10.74, 'F': 0.82, 'G': 1.5, 'H': 0.01, 'I': 0.07, 'J': 0.05, 'K': 0, 'L': 10.31, 'M': 2.52, 'N': 9.74, 'O': 3.1, 'P': 0.28, 'Q': 1.0, 'R': 7.54, 'S': 14.65, 'T': 21.04, 'U': 0.02, 'V': 1.56, 'W': 0, 'X': 0.28, 'Y': 0.0, 'Z': 0.05, ' ': 10.16},
    'J': {'A': 22.25, 'B': 0, 'C': 0, 'D': 0, 'E': 46.38, 'F': 0, 'G': 0, 'H': 0.04, 'I': 0.31, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 23.42, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 7.31, 'V': 0, 'W': 0, 'X': 0, 'Y': 0.29, 'Z': 0, ' ': 0}, 
    'K': {'A': 8.33, 'B': 0, 'C': 0, 'D': 0, 'E': 33.33, 'F': 0, 'G': 0, 'H': 0, 'I': 25.0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 4.17, 'P': 0, 'Q': 0, 'R': 4.17, 'S': 4.17, 'T': 0, 'U': 4.17, 'V': 0, 'W': 0, 'X': 0, 'Y': 8.33, 'Z': 0, ' ': 8.33}, 
    'L': {'A': 19.59, 'B': 0.34, 'C': 0.11, 'D': 0.08, 'E': 35.88, 'F': 0.06, 'G': 0.18, 'H': 0.63, 'I': 5.7, 'J': 0.01, 'K': 0.0, 'L': 13.02, 'M': 0.14, 'N': 0.07, 'O': 3.69, 'P': 0.15, 'Q': 1.01, 'R': 0.04, 'S': 1.52, 'T': 0.26, 'U': 7.94, 'V': 0.05, 'W': 0, 'X': 0, 'Y': 0.18, 'Z': 0.01, ' ': 9.32}, 
    'M': {'A': 20.39, 'B': 4.0, 'C': 0.0, 'D': 0.03, 'E': 37.1, 'F': 0, 'G': 0, 'H': 0.01, 'I': 6.19, 'J': 0.0, 'K': 0, 'L': 0.18, 'M': 10.0, 'N': 0.1, 'O': 11.85, 'P': 6.75, 'Q': 0, 'R': 0.0, 'S': 0.15, 'T': 0.09, 'U': 1.45, 'V': 0.01, 'W': 0, 'X': 0, 'Y': 0.31, 'Z': 0, ' ': 1.38}, 
    'N': {'A': 4.77, 'B': 0.04, 'C': 5.17, 'D': 6.9, 'E': 14.44, 'F': 0.73, 'G': 1.46, 'H': 0.18, 'I': 2.59, 'J': 0.1, 'K': 0.0, 'L': 0.15, 'M': 0.14, 'N': 4.53, 'O': 4.02, 'P': 0.24, 'Q': 0.36, 'R': 0.18, 'S': 9.36, 'T': 22.65, 'U': 1.38, 'V': 0.9, 'W': 0.0, 'X': 0.04, 'Y': 0.26, 'Z': 0.03, ' ': 19.39}, 
    'O': {'A': 0.02, 'B': 1.02, 'C': 1.57, 'D': 1.71, 'E': 0.76, 'F': 0.49, 'G': 0.35, 'H': 0.1, 'I': 10.87, 'J': 0.08, 'K': 0.0, 'L': 2.1, 'M': 8.17, 'N': 25.32, 'O': 2.19, 'P': 1.15, 'Q': 0.28, 'R': 7.3, 'S': 2.97, 'T': 3.29, 'U': 26.71, 'V': 0.16, 'W': 0, 'X': 0.02, 'Y': 1.28, 'Z': 0.01, ' ': 2.05},
    'P': {'A': 24.94, 'B': 0.01, 'C': 0.2, 'D': 0.04, 'E': 16.62, 'F': 0.01, 'G': 0, 'H': 1.38, 'I': 3.07, 'J': 0.01, 'K': 0, 'L': 10.52, 'M': 0, 'N': 0.01, 'O': 16.28, 'P': 3.89, 'Q': 0, 'R': 14.88, 'S': 2.25, 'T': 1.16, 'U': 3.36, 'V': 0.0, 'W': 0, 'X': 0, 'Y': 0.01, 'Z': 0, ' ': 1.35},
    'Q': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0.01, 'G': 0, 'H': 0.01, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 99.79, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, ' ': 0.19},
    'R': {'A': 11.2, 'B': 0.31, 'C': 2.32, 'D': 2.9, 'E': 31.26, 'F': 0.32, 'G': 0.58, 'H': 0.01, 'I': 7.32, 'J': 0.06, 'K': 0, 'L': 0.84, 'M': 1.61, 'N': 0.85, 'O': 5.8, 'P': 0.44, 'Q': 0.37, 'R': 1.9, 'S': 4.21, 'T': 4.71, 'U': 1.18, 'V': 0.6, 'W': 0, 'X': 0, 'Y': 0.05, 'Z': 0.01, ' ': 21.12},
    'S': {'A': 8.24, 'B': 0.11, 'C': 1.0, 'D': 0.51, 'E': 13.64, 'F': 0.18, 'G': 0.06, 'H': 0.07, 'I': 6.8, 'J': 0.14, 'K': 0.0, 'L': 0.47, 'M': 0.49, 'N': 0.14, 'O': 6.3, 'P': 1.39, 'Q': 1.21, 'R': 0.17, 'S': 6.44, 'T': 4.55, 'U': 2.78, 'V': 0.14, 'W': 1.15, 'X': 0, 'Y': 0.17, 'Z': 0.0, ' ': 43.83}, 
    'T': {'A': 9.52, 'B': 0.07, 'C': 0.47, 'D': 0.53, 'E': 19.04, 'F': 0.09, 'G': 0.04, 'H': 0.49, 'I': 7.45, 'J': 0.1, 'K': 0, 'L': 0.4, 'M': 0.24, 'N': 0.06, 'O': 4.12, 'P': 0.45, 'Q': 0.28, 'R': 8.09, 'S': 2.11, 'T': 3.84, 'U': 1.94, 'V': 0.08, 'W': 0.0, 'X': 0, 'Y': 0.05, 'Z': 0, ' ': 40.52}, 
    'U': {'A': 2.56, 'B': 0.51, 'C': 1.45, 'D': 0.99, 'E': 15.82, 'F': 0.49, 'G': 0.33, 'H': 0.06, 'I': 13.09, 'J': 0.52, 'K': 0, 'L': 2.69, 'M': 0.87, 'N': 10.44, 'O': 0.98, 'P': 1.34, 'Q': 0.2, 'R': 15.13, 'S': 10.04, 'T': 6.8, 'U': 0.46, 'V': 3.51, 'W': 0.0, 'X': 3.53, 'Y': 0.15, 'Z': 0.01, ' ': 8.0}, 
    'V': {'A': 28.68, 'B': 0, 'C': 0, 'D': 0, 'E': 31.5, 'F': 0, 'G': 0, 'H': 0, 'I': 14.37, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 19.32, 'P': 0, 'Q': 0, 'R': 4.23, 'S': 0, 'T': 0, 'U': 1.86, 'V': 0, 'W': 0, 'X': 0, 'Y': 0.04, 'Z': 0, ' ': 0.01}, 
    'W': {'A': 99.72, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0.28, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, ' ': 0}, 
    'X': {'A': 3.74, 'B': 0.08, 'C': 4.88, 'D': 0.45, 'E': 5.03, 'F': 0.34, 'G': 0.15, 'H': 0.38, 'I': 5.67, 'J': 0.15, 'K': 0.04, 'L': 0.76, 'M': 0.98, 'N': 0.15, 'O': 0.3, 'P': 6.84, 'Q': 2.5, 'R': 0.19, 'S': 0.38, 'T': 4.01, 'U': 0.08, 'V': 0.64, 'W': 0, 'X': 0, 'Y': 0.19, 'Z': 0, ' ': 62.08}, 
    'Y': {'A': 25.46, 'B': 0.05, 'C': 0.61, 'D': 0.33, 'E': 17.66, 'F': 0.05, 'G': 0.28, 'H': 0, 'I': 0.19, 'J': 0.09, 'K': 0, 'L': 1.5, 'M': 2.82, 'N': 0.19, 'O': 3.76, 'P': 1.03, 'Q': 0.05, 'R': 1.27, 'S': 10.71, 'T': 0.61, 'U': 0.05, 'V': 0.05, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0.05, ' ': 33.21}, 
    'Z': {'A': 1.81, 'B': 0.5, 'C': 0.2, 'D': 1.1, 'E': 5.92, 'F': 0, 'G': 0.1, 'H': 0, 'I': 0.2, 'J': 0.3, 'K': 0, 'L': 2.01, 'M': 1.4, 'N': 0.2, 'O': 3.51, 'P': 0.7, 'Q': 0.3, 'R': 0, 'S': 0.6, 'T': 0.6, 'U': 1.5, 'V': 6.82, 'W': 0, 'X': 0, 'Y': 0.6, 'Z': 0.4, ' ': 71.21}, 
    ' ': {'A': 8.09, 'B': 1.57, 'C': 7.37, 'D': 12.7, 'E': 7.78, 'F': 2.81, 'G': 1.04, 'H': 0.53, 'I': 2.39, 'J': 2.23, 'K': 0.0, 'L': 9.86, 'M': 5.53, 'N': 3.22, 'O': 1.68, 'P': 8.71, 'Q': 5.83, 'R': 2.81, 'S': 7.53, 'T': 2.95, 'U': 2.19, 'V': 2.86, 'W': 0.01, 'X': 0.01, 'Y': 0.31, 'Z': 0.02, ' ': 0}}

# Dico fait avec les fonctions au dessus basé sur le texte de swaan

# Fonction de calcul de plausibilité 
def plausibilite(text,dico_freq : dict) -> float:
    """
    Calcul un score de probabilité
    somme(log(pi)) tend  vers 4.47 pour un texte français  
    n : le nb de lettre
    p : la probabilité de la lettre suivante sachant la lettre précédente

    Args :
        text : un message 
    Return: 
        int un score 
    """
    score = 0 
    n = len(text) 
    liste_bigramme = []
    for i in range(n-1): # On parcours le texte
        liste_bigramme.append(dico_freq[text[i]][text[i+1]]) # On ajoute la probabilité du bigramme dans la liste
    for i in range(0,len(liste_bigramme)-1): # On parcours la liste des probabilités
        score += liste_bigramme[i] * liste_bigramme[i+1] # On multiplie les probabilités pour avoir la plaussibilité du texte plus un texte a une probabilité plus élevé plus il est plausibles
        
    return math.log(score,10) # On retourne le log pour avoir un score plus facilement lisible



print(plausibilite("CETTE PHRASE EST TRES LONGUE ET DEMAIN ON VA MANGER DES PATES AU BEURRE AVEC DE LA SAUCE TOMATE ET DU THON CAR BASTIEN EST DEBILE ET HIER ON A MANGER DES VACHES AVEC DU JAMBON ET DU FROMAGE AVEC DES YAOURTS ET DU FROMAGE ET ENCORE DU FROMAGE",DICO_BIGRAME))
print(plausibilite("FIOUHIHUIHUIH IUHUISFIFSFIOSFIO FNKFSONOSINOISFN FSSFSFSFSG",DICO_BIGRAME))

def permutation(text : str ,a : int ,b : int ) -> str: 
    """
        Permute les lettres de la position a et b
    """
    lettre_a = ALPHABET[a] # On récupère la lettre de la position a
    lettre_b = ALPHABET[b] # On récupère la lettre de la position b
    text = text.replace(lettre_a,lettre_b) # On remplace la lettre a par la lettre b
    return text

# Fonction de déchiffrement de texte
def dechiffrement(text : str,dico_freq : dict) -> str:
    """
    Déchiffre un texte en fonction du dictionnaire de fréquence

    Args :
        text : un message 
    Return: 
        str : le message déchiffré
    """
    #base sur l'algo metroplis
    a = 0
    b = 0
    text_dechiffre = text
    score = plausibilite(text,dico_freq) # On récupère le score du texte
    score_dechiffrement = 0 
    liste_lettre_permute = []
   
    while score < 4.47 and len(liste_lettre_permute) < 326 : # possibilité de permutation
            #on prend deux lettre à inverser parmis les combinaison déja faites
        while len(liste_lettre_permute) < 326: # 326 possibilité de permutation
                print(len(liste_lettre_permute))
                a = random.randint(0,25) # On prend une lettre au hasard
                b = random.randint(0,25)
                if (a,b) not in liste_lettre_permute and (b,a) not in liste_lettre_permute and a != b: # On vérifie que les lettres ne sont pas déjà inversées et que ce ne sont pas la même lettre
                    break
            
        liste_lettre_permute.append((a,b)) # On ajoute les lettres à la liste des lettres inversées
        print("couple :" +ALPHABET[a],ALPHABET[b]) 
        # on inverse les lettres
        text_dechiffre = text.replace(ALPHABET[a], ALPHABET[b])
        # on calcule la plausibilité du texte
        score_dechiffrement = plausibilite(text_dechiffre,dico_freq)
        # on compare les deux plausibilités 
#        print("=====================================================================================================================================================================================")
#        print("texte dechiffre : ",text_dechiffre, "score : ",score)
#        print("=====================================================================================================================================================================================")

        if score * 2 > score_dechiffrement > score*0.90: # Si le score du texte déchiffré est compris entre 90% et 200% du score du texte chiffré on accepte le nouveau texte 
            score = score_dechiffrement
            liste_lettre_permute = []
        else:
            # on inverse les lettres car on a regresse
            text_dechiffre = text_dechiffre.replace(ALPHABET[b],ALPHABET[a])
            liste_lettre_permute.append((a,b))


    return text_dechiffre
#text = open_fichier("texte.txt")
#text = correction(text)
#print("=====================================================================================================================================================================================")
#print("texte dechiffre : ", dechiffrement(text, DICO_BIGRAME))
#print("=====================================================================================================================================================================================")

#text = correction("Os dom sb kbrog : wf bok bykg-ewzbof ywm lwoxo r'wf zglmgf, hwol wf mbfug, hwol wf ygv-mkgm, hwol wf egmossgf dol bw ugwm rw pgwk. Rwmkgfe eibfmb rw Sbfndbff, Zbkzbkb wf dbrkoubs r'Bkbugf, Lmoei-Kbfrbss wf bok r' Borb.")
#dechiffrement(text,DICO_BIGRAME)

def chiffrement(text : str, cle: str) -> str:
    """
    Chiffre un texte avec une clé

    Args :
        text : un message
        cle : une clé
    Return:
        str : le message chiffré
    """
    text_chiffre = ""
    for i in range(len(text)):
        if text[i] == " ":
            text_chiffre += " "
        else:
            text_chiffre += ALPHABET[(ALPHABET.index(text[i]) + ALPHABET.index(cle[i%len(cle)]))%26] # On ajoute la lettre chiffrée à la suite du texte chiffré
    return text_chiffre
print(chiffrement("CETTE PHRASE EST TRES LONGUE ET DEMAIN ON VA MANGER DES PATES AU BEURRE AVEC DE LA SAUCE TOMATE ET DU THON CAR BASTIEN EST DEBILE ET HIER ON A MANGER DES VACHES AVEC DU JAMBON ET DU FROMAGE AVEC DES YAOURTS ET DU FROMAGE ET ENCORE DU FROMAGE","BASTIEN"))

def dechiffrement_cle(text : str, cle : str) -> str:
    """
    Déchiffre un texte avec une clé

    Args :
        text : un message
        dico_freq : un dictionnaire de fréquence
    Return:
        str : le message déchiffré
    """
    text_dechiffre = ""
    for i in range(len(text)):
        if text[i] == " ":
            text_dechiffre += " "
        else:
            text_dechiffre += ALPHABET[(ALPHABET.index(text[i]) - ALPHABET.index(cle[i%len(cle)]))%26] # On ajoute la lettre déchiffrée à la suite du texte déchiffré
    return text_dechiffre
print(dechiffrement_cle("DELMM CIRSLM RTT MZIF LGGOYR EL LIZBIF WR WA FIRTFR WMW QALXA NV TXCVEF SOMG EE EI FBUUX XBNALX IG DM BLBO UTZ OBSLBMR FSL LIOJLW MX IIWK SA A FIRTFR WMW WAUAMW BVWV HH JSFJSA EL LY GRGFIKR ANXK QFS RISHSTK MX EU YZSZBGW MX FNUHZI EU YZSZBGW","BASTIEN"))
