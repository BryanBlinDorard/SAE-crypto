from string import ascii_uppercase

"""
Formule : 
    Pour un clef (a,b) et une lettre à encoder x on a :
    ax+b=resultat_encodage
"""

def encode_affine(texte:str,clef:tuple)->str:
    """Encode un texte donné avec le chiffrement affine grâce à une clef donnée.

    Args:
        texte (str): Un texte à encoder.
        clef (tuple): Un clef sous forme d'un tuble composé de deux entiers.

    Returns:
        str: Un texte encodé.
    """    
    indices_lettres = convertir_en_nombres(texte)
    indices_code = []
    for indice_lettre in indices_lettres:
        indices_code.append((clef[0]*indice_lettre+clef[1])%26)
    return convertir_en_lettres(indices_code)

def convertir_en_nombres(texte:str)->list:
    """Convertie un texte donnné en une liste d'entiers suivant la position des lettres dans l'alphabet.

    Args:
        texte (str): Un texte à convertir.

    Returns:
        list: Une liste d'entiers.
    """   
    res = []
    texte_en_maj = texte_en_majuscules(texte)
    for lettre in texte_en_maj:
        for i in range(len(ascii_uppercase)):
            if lettre==ascii_uppercase[i]:
                res.append(i)

def convertir_en_lettres(chiffres:list)->str:
    """Convertie un liste d'entiers (compris entre 0 et 26 exclu) donnée en une chaine de caractères.

    Args:
        chiffres (list): Une liste d'entiers à convertir.

    Returns:
        str: Une chaine de caractères.
    """    
    res = ""
    for chiffre in chiffres:
        for i in range(len(ascii_uppercase)):
            if chiffre==i:
                res+=ascii_uppercase[i]
    return res

def texte_en_majuscules(texte:str)->str:
    """Retourne le texte donné en majuscules.

    Args:
        texte (str): Un texte à mettre en majuscules.

    Returns:
        str: Un texte en majuscules.
    """    
    res = ""
    for lettre in texte:
        res+=lettre.upper()
    return res