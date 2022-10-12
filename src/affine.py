from string import ascii_uppercase

"""
Formule : 
    Pour un clef (a,b) et une lettre à encoder x on a :
    ax+b=résultat_encodage
"""

def encode_affine(texte:str,clef:tuple)->str:
    """Encode un texte donné avec le chiffrement affine grâce à une clef donnée.

    Args:
        texte (str): Un texte à encoder.
        clef (tuple): Une clef sous forme d'un tuple composé de deux entiers.

    Returns:
        str: Un texte encodé.
    """    
    indices_lettres = convertir_en_nombres(texte)
    indices_code = []
    for indice_lettre in indices_lettres:
        indices_code.append((clef[0]*indice_lettre+clef[1])%26)
    return convertir_en_lettres(indices_code)

"""
Formule :
    Pour une clef (a,b) et une lettre x à déchiffrer on a :
    résultat_decodage=(x-b)/a
"""

def decode_affine(code:str,clef:tuple)->str:
    """Décode un texte donné avec le chiffrement affine grâce à une clef donnée.

    Args:
        texte (str): Un texte à décoder.
        clef (tuple): Une clef sous forme d'un tuple composé de deux entiers.

    Returns:
        str: Un texte décodé.
    """    
    indices_code = convertir_en_nombres(code)
    indices_lettres = []
    for indice_code in indices_code:
        indices_lettres.append((clef[0]*indice_code+clef[1])%26)
    return convertir_en_lettres(indices_lettres)

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

def sauvergarder_carateres_non_lettres(texte:str)->dict:
    """Sauvegarde dans un dictionnaire les caractères n'étant 
    pas des lettres ainsi que leur position dans la chaine de caractères initiale.

    Args:
        texte (str): Un texte à sauvegarder.

    Returns:
        dict: Le dictionnaire ayant en clef l'indice de la position du caractère dans le texte inital 
        et ayant en valeur le caractère.
    """    

def supprimer_caracteres_non_lettres(texte:str)->str:
    """Supprime les caractères n'étant pas des lettres dans une chaine donnée.

    Args:
        texte (str): Un texte dans lequel supprimer les caractères non lettres.

    Returns:
        str: Une chaine de caractères contenant uniquement des lettres.
    """    

def ajouter_caractères_non_lettres(texte:str,positions:dict)->str:
    """Ajoute les caractères spéciaux dans un texte donné grâce aux positions données.

    Args:
        texte (str): Un texte dans lequel ajouter les caractères spéciaux.
        positions (dict): Un dictionnaire contentant les positions des caractères spéciaux 
        dans la chaine initiale ainsi que les caractères en eux même.

    Returns:
        str: Un texte avec les caractères spéciaux rajoutés.
    """    