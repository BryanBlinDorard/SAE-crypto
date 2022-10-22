import math
import fonctions_utiles
import CONSTANTES

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

def calcul_distance(textes_possibles:dict):
    """Permet de calculer la distance pour chaque texte possible.

    Args:
        textes_possibles (dict): Un dictionnaire avec toutes les possibilités de décodage d'un texte.

    Returns:
        dict: Un dictionnaire avec toutes les possibilités de décodage d'un texte et leur distance.
    """
    tableau_de_freq=dict()
    distance = dict()

    #calcul de la fréquence de chaque lettre pour chaque possibilité
    for texte in textes_possibles:
        texte = fonctions_utiles.supprimer_caracteres_non_lettres(texte)
        freq_lettres_du_texte = fonctions_utiles.calculer_frequence_lettre(texte)
        tableau_de_freq[texte] = freq_lettres_du_texte

    #calcul de la distance entre la fréquence de chaque lettre et la fréquence de la langue FR
    for texte in tableau_de_freq:
        calcul=0
        for lettre in tableau_de_freq[texte]:
            calcul+=(CONSTANTES.FR_FREQ[lettre]-tableau_de_freq[texte][lettre])**2
        calcul=math.sqrt(calcul)  
        distance[texte]=calcul
    return distance


def distance_la_plus_petite(distance:dict)->str:
    """Permet de trouver le texte avec la distance la plus petite.

    Args:
        distance (dict): Un dictionnaire avec toutes les possibilités de décodage d'un texte et leurs distances.

    Returns:
        str: Le texte avec la distance la plus petite.
    """

    distance_mini = None
    for texte in distance:
        if distance_mini == None:
            distance_mini = distance[texte]
        if distance[texte] < distance_mini:
            distance_mini = distance[texte]
            texte_mini = texte
    return texte_mini


def test_toutes_les_possibilites(code:str):
    """Permet de générer un dictionnaire avec toutes les possibilités de décodage d'un texte.

    Args:
        code (str): Un code crypté avec le chiffrement affine.

    Returns:
        dict: Un dictionnaire avec toutes les possibilités de décodage d'un texte.
    """    
    possibilites = {}
    for premier_avec_26 in CONSTANTES.PREMIERS_AVEC_26:
        for i in range(26):
            phrase_potentiel_decodage = decode_affine(code,(premier_avec_26,i))
            possibilites[phrase_potentiel_decodage] = (premier_avec_26,i)
    return possibilites

def casser_affine_auto(texte_a_decoder:str)->str:
    """Permet de casser un message codé avec chiffrement affine.

    Args:
        texte (str): Un texte à décoder.

    Returns:
        str: Le texte décodé.
    """    
    texte_a_decoder = texte_a_decoder.upper()

    possibilites = test_toutes_les_possibilites(texte_a_decoder)
    distance = calcul_distance(possibilites)
    texte = distance_la_plus_petite(distance)
    
    texte_final = fonctions_utiles.ajouter_caracteres_non_lettres(texte_a_decoder,texte)
    return texte_final