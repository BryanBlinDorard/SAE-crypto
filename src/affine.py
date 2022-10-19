import fonctions_utiles

def encode_affine(texte:str,clef:tuple)->str:
    """Encode un texte donné avec le chiffrement affine grâce à une clef donnée.

    Args:
        texte (str): Un texte à encoder.
        clef (tuple): Une clef sous forme d'un tuple composé de deux entiers.

    Returns:
        str: Un texte encodé.
    """    
    texte_simple = fonctions_utiles.supprimer_caracteres_non_lettres(texte.upper())
    indices_lettres = fonctions_utiles.convertir_en_nombres(texte_simple)
    indices_code = []
    for indice_lettre in indices_lettres:
        indices_code.append((clef[0]*indice_lettre+clef[1])%26)
    return fonctions_utiles.ajouter_caracteres_non_lettres(texte.upper(),fonctions_utiles.convertir_en_lettres(indices_code))

def decode_affine(code:str,clef:tuple)->str:
    """Décode un texte donné avec le chiffrement affine grâce à une clef donnée.

    Args:
        texte (str): Un texte à décoder.
        clef (tuple): Une clef sous forme d'un tuple composé de deux entiers.

    Returns:
        str: Un texte décodé.
    """   
    code_simple = fonctions_utiles.supprimer_caracteres_non_lettres(code.upper()) 
    indices_code = fonctions_utiles.convertir_en_nombres(code_simple)
    indices_lettres = []
    for indice_code in indices_code:
        indices_lettres.append((fonctions_utiles.inverse_modulaire(clef[0],26)*(indice_code-clef[1]))%26)
    return fonctions_utiles.ajouter_caracteres_non_lettres(code.upper(),fonctions_utiles.convertir_en_lettres(indices_lettres))
