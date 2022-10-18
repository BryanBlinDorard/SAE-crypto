from string import ascii_uppercase

def convertir_en_nombres(texte:str)->list:
    """Convertie un texte donné en une liste d'entiers 
    suivant la position des lettres dans l'alphabet.

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

def supprimer_caracteres_non_lettres(texte:str)->str:
    """Supprime les caractères n'étant pas des lettres dans une chaine donnée.

    Args:
        texte (str): Un texte dans lequel supprimer les caractères non lettres.

    Returns:
        str: Une chaine de caractères contenant uniquement des lettres.
    """    
    res = ""
    for lettre in texte:
        if lettre in ascii_uppercase:
            res+=lettre
    return res

def ajouter_caractères_non_lettres(texte:str,texte_de_base:str)->str:
    """Ajoute les caractères spéciaux dans un texte donné grâce au texte d'origine.

    Args:
        texte (str): Un texte dans lequel ajouter les caractères spéciaux.
        texte_de_base(str): Le texte initial dans lequel on a retiré les caractère

    Returns:
        str: Un texte avec les caractères spéciaux rajoutés.
    """   
    res = ""
    while len(res) < len(texte_de_base):
        ...