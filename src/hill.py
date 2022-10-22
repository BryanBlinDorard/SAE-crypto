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


def determinant_matrice(matrice):
  return matrice[0][0]*matrice[1][1] - matrice[0][1]*matrice[1][0]

def matrice_cofacteurs(matrice):
  return [[matrice[1][1],-matrice[0][1]],[-matrice[1][0],matrice[0][0]]]

def inverse_matrice(matrice):
  det = determinant_matrice(matrice)
  if det == 0:
    return "Erreur: Matrice non inversible"

  matrice_cof = matrice_cofacteurs(matrice)
  new_matrice = [[],[]]

  for i in range(2):
    for j in range(2):
      new_matrice[i].append((matrice_cof[i][j]/det)%26)
  return new_matrice
