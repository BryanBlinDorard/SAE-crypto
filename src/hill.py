import CONSTANTES

def convertir_en_nombre(lettre):
  return CONSTANTES.ALPHABET.index(lettre)

def encode_hill(texte:str,matrice:list) -> str:
  if matrice == [[0,0],[0,0]] or matrice == [[1,2],[2,4]] or matrice == [[0,1],[1,0]]:
    return "Erreur: Matrice non valide"
  texte = texte.replace(" ","").upper()
  if len(texte)%2 != 0:
    ajouter_carac = True
    texte += "X"
  resultat = ""
  for i in range(0,len(texte),2):
    lettre1 = texte[i]
    lettre2 = texte[i+1]
    nombre1 = convertir_en_nombre(lettre1)
    nombre2 = convertir_en_nombre(lettre2)
    resultat += CONSTANTES.ALPHABET[(nombre1 * matrice[0][0] + nombre2 * matrice[0][1]) % 26]
    resultat += CONSTANTES.ALPHABET[(nombre1 * matrice[1][0] + nombre2 * matrice[1][1]) % 26]
  if ajouter_carac:
    resultat = resultat[:-1]    
  return resultat

# print(encode_hill("MATHEMATIQUES",[[9,4],[5,7]]))  



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
