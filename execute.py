def terminal():
  print("----------")
  print("[1] déchiffrer le fichier 1")
  print("[2] déchiffrer le fichier 2")
  print("[3] déchiffrer le fichier 3")
  print("[4] déchiffrer le fichier 4")
  print("[5] déchiffrer le fichier 5")
  input1 = input("Rentrer le num voulu :")

  match input1:
    case "1":
      print("1")
    case "2":
      print("2")
    case "3":
      print("3")
    case "4":
      print("4")
    case "5":
      print("5")
    case _:
      print("Erreur")

terminal()