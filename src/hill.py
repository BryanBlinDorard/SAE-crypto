from base64 import encode
import CONSTANTES
import fonctions_utiles

def convertir_en_nombre(lettre):
  return CONSTANTES.ALPHABET.index(lettre)

def encode_hill(texte:str, clef:list)->str:
  """Encode un texte donné avec Hill.

  Args:
      texte (str): Un texte à encoder.
      clef (list): Une matrice clef sous la forme [[],[]]

  Returns:
      str: Le texte encodé.
  """  
  est_impair = False
  texte_encode = ""
  texte_encode_en_nombres = []

  if not fonctions_utiles.matrice_inversible(clef):
    print("La clef n'est pas inversible.")
    return None

  if len(texte)%2!=0:
    est_impair = True
    texte+="H"
  
  texte = texte.upper()
  texte_sans_caract_spe = fonctions_utiles.supprimer_caracteres_non_lettres(texte)
  texte_en_nombres = fonctions_utiles.convertir_en_nombres(texte_sans_caract_spe)
  texte_en_nombres_groupe = fonctions_utiles.grouper_par_deux(texte_en_nombres)

  for duo in texte_en_nombres_groupe:
    texte_encode_en_nombres.append(((clef[0][0]*duo[0])+(clef[0][1]*duo[1]))%26)
    texte_encode_en_nombres.append(((clef[1][0]*duo[0])+(clef[1][1]*duo[1]))%26)

  if est_impair:
    texte_encode_en_nombres.pop(-1)

  texte_encode = fonctions_utiles.convertir_en_lettres(texte_encode_en_nombres)

  return texte_encode

def decode_hill(code:str,clef:list)->str:
    """Décode un matrice codée avec Hill grâce à sa clef d'encodage.

    Args:
        code (str): Un texte codé avec Hill.
        clef (list): La clef utilisée pour l'encodage.

    Returns:
        str: Le texte décodé
    """  
    inverse_clef = fonctions_utiles.inverse_matrice(clef)
    print(inverse_clef)
    return encode_hill(code,inverse_clef)
texte = "coucou"
clef = [[3,5],[1,2]]
texte_code = encode_hill(texte, clef)
texte_decode = decode_hill(texte_code, clef)
print(texte)
print(texte_code)
print(texte_decode)