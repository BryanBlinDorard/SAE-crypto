import math
import CONSTANTES

def convertir_en_nombres(texte:str)->list:
    """Convertie un texte donné en une liste d'entiers 
    suivant la position des lettres dans l'alphabet.

    Args:
        texte (str): Un texte à convertir.

    Returns:
        list: Une liste d'entiers.
    """   
    res = []
    texte.upper()
    for lettre in texte:
        for i in range(len(CONSTANTES.ALPHABET)):
            if lettre==CONSTANTES.ALPHABET[i]:
                res.append(i)
    return res

def convertir_en_lettres(chiffres:list)->str:
    """Convertit une liste d'entiers (compris entre 0 et 26 exclu) donnée en une chaine de caractères.

    Args:
        chiffres (list): Une liste d'entiers à convertir.

    Returns:
        str: Une chaine de caractères.
    """    
    res = ""
    for chiffre in chiffres:
        for i in range(len(CONSTANTES.ALPHABET)):
            if chiffre==i:
                res+=CONSTANTES.ALPHABET[i]
    return res

def supprimer_caracteres_non_lettres(texte:str)->str:
    """Supprime les caractères n'étant pas des lettres dans une chaine donnée.

    Args:
        texte (str): Un texte dans lequel supprimer les caractères non lettres.

    Returns:
        str: Une chaine de caractères contenant uniquement des lettres.
    """    
    res = ""
    for lettre in texte:
        if lettre in CONSTANTES.ALPHABET:
            res+=lettre
    return res

def ajouter_caracteres_non_lettres(texte_de_base:str,texte:str)->str:
    """Ajoute les caractères spéciaux dans un texte donné grâce au texte d'origine.

    Args:
        texte_de_base(str): Le texte initial dans lequel on a retiré les caractère
        texte (str): Un texte dans lequel ajouter les caractères spéciaux.

    Returns:
        str: Un texte avec les caractères spéciaux rajoutés.
    """   
    res = ""
    indice_texte = 0
    indice_texte_de_base = 0
    while len(res) < len(texte_de_base):
        if texte_de_base[indice_texte_de_base] not in CONSTANTES.ALPHABET:
            res+=texte_de_base[indice_texte_de_base]
        else:
            res+=texte[indice_texte]
            indice_texte+=1
        indice_texte_de_base+=1
    return res

def inverse_modulaire(chiffre:int, modulo:int)->int:
    """Calcule l'inverse modulaire d'un nombre donné en premier paramètre modulo le deuxième.

    Args:
        chiffre (int): Un nombre.
        modulo (int): Un modulo

    Returns:
        int: L'inverse modulaire.
    """    
    inverse=2
    while chiffre*inverse%modulo!=1:
        inverse+=1
        if inverse>chiffre**10:
            break
    return inverse


# pour vigenere
def calc_freq(texte):
    tab_freq = [0]*26
    for c in texte:
        tab_freq[ord(c)-65] += 1  
    return tab_freq


# pour affine et cesar
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

def pgcd(num1:int,num2:int)->int:
    """Calcule le plus grand commun diviseur de deux nombres donnés 
    grâce à l'algorithme d'Euclide.

    Args:
        num1 (int): Un premier entier.
        num2 (int): Un deuxième entier.

    Returns:
        int: Le plus grand commun diviseur.
    """    
    reste = num1%num2
    if reste==0:
        return reste
    elif pgcd(num2, reste)==0:
        return reste
    else:
        reste = pgcd(num2, reste)
    return reste

def premiers_avec(num:int)->list:
    """Cherche les nombres premiers avec le chiffre donné en paramètre.

    Args:
        num (int): Un chiffre quelconque.

    Returns:
        list: La liste des nombres premiers avec le chiffre donné.
    """    
    res = []
    for i in range(num):
        if pgcd(i,num)==1:
            res.append(i)
    return res

def grouper_par_deux(liste:list)->list:
    """Permet de grouper deux par deux dans des sous-listes les éléments d'une liste donnée.

    Args:
        liste (list): Une liste d'éléments à grouper par deux.

    Returns:
        list: Une liste d'éléments groupés deux par deux.
    """    
    res = []
    sous_liste = []
    for i in range(len(liste)):
        if (i+1)%2==0:
            sous_liste.append(liste[i])
            res.append(sous_liste.copy())
            sous_liste = []
        else:
            sous_liste.append(liste[i])
    return res

def determinant_matrice(matrice:list)->int:
    """Calcule le déterminant d'une matrice donnée.

    Args:
        matrice (list): Une matrice de taille 2*2 de la forme [[],[]]

    Returns:
        int: Le déterminant de la matrice.
    """    
    return (matrice[0][1]*matrice[1][1])-(matrice[0][1]*matrice[1][0])

def matrice_inversible(matrice:list)->bool:
    """Détermine si la matrice donnée est inversible ou non.

    Args:
        matrice (list): Une matrice de taille 2*2 sous la forme [[],[]].

    Returns:
        bool: True si la matrice est inversible. False sinon.
    """    
    return determinant_matrice(matrice)!=0

def matrice_cofacteurs(matrice):
    return [[matrice[1][1],-matrice[0][1]],[-matrice[1][0],matrice[0][0]]]

def inverse_matrice(matrice:list)->list:
    """Inverse une matrice donnée.

    Args:
        matrice (list): Une matrice de taille 2*2 sous la forme [[],[]].

    Returns:
        list: La matrice inverse de la matrice donnée en paramètre.
    """    
    det = determinant_matrice(matrice)
    if det == 0:
        return "Erreur: Matrice non inversible"

    matrice_cof = matrice_cofacteurs(matrice)
    new_matrice = [[],[]]

    for i in range(2):
        for j in range(2):
            new_matrice[i].append(math.floor((matrice_cof[i][j]/det)%26))
    return new_matrice