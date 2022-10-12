a_dechiffrer = "Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."


def encode_vigenere(texte: str, cle: str) -> str:
  """chiffrement de vigenere

  Args:
    c (str: le message à chiffrer sous forme de chaine de caractères
    cle (str): la clé à utiliser sous forme de chaine de caractères
    
  Returns:
    str: Elle retourne le message chiffré sous forme de chaine de caractères
  """
  texte = texte.upper()
  cle = cle.upper()
  longueur_texte = len(texte)
  indice_de_la_cle = 0
  message_encode = ""

  for i in range(0, longueur_texte):
      if 'A' <= texte[i] <= 'Z':
        convertionTexte = (ord(texte[i]) - ord('A')) #convertion du texte en nombre
        convertionCle = (ord(cle[indice_de_la_cle]) - ord('A')) #convertion de la clé en nombre
        message_encode += chr(((convertionTexte + convertionCle) % 26) + ord('A')) #convertion du message chiffré en lettre
        indice_de_la_cle = (indice_de_la_cle + 1) % len(cle)
      else:
          message_encode +=  texte[i]
  return message_encode


def decode_vigenere(texte: str, cle:str) -> str: 
  """déchiffrement de vigenere

  Args:
      texte (str): le message à déchiffrer sous forme de chaine de caractères
      cle (str): la clé à utiliser sous forme de chaine de caractères

  Returns:
      str: Elle retourne le message déchiffré sous forme de chaine de caractères
  """
  texte = texte.upper()
  cle = cle.upper()
  longueur_texte = len(texte)
  indice_de_la_cle = 0
  message_encode = ""

  for i in range(0, longueur_texte):
      if 'A' <= texte[i] <= 'Z':
        convertionTexte = (ord(texte[i]) - ord('A'))
        convertionCle = (ord(cle[indice_de_la_cle]) - ord('A'))
        message_encode += chr(((convertionTexte - convertionCle ) % 26) + ord('A')) 
        indice_de_la_cle = (indice_de_la_cle + 1) % len(cle)
      else:
          message_encode +=  texte[i]
  return message_encode

