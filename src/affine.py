import fonctions_utiles

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
    indices_lettres = fonctions_utiles.convertir_en_nombres(texte)
    indices_code = []
    for indice_lettre in indices_lettres:
        indices_code.append((clef[0]*indice_lettre+clef[1])%26)
    return fonctions_utiles.convertir_en_lettres(indices_code)

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
    indices_code = fonctions_utiles.convertir_en_nombres(code)
    indices_lettres = []
    for indice_code in indices_code:
        indices_lettres.append((clef[0]*indice_code+clef[1])%26)
    return fonctions_utiles.convertir_en_lettres(indices_lettres)
 