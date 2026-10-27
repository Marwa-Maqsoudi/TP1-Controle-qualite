"""Programme principal : un petit terminal de contrôle qualité, piloté par des commandes."""
from donnees import LOT_A
from qualite import analyser_ligne, rapport

AIDE = """Commandes :
  mesure CODE VALEUR   contrôler une pièce (ex. : mesure AXE-0100 25,04)
  lot                  rapport du lot A
  aide                 afficher cette aide
  quitter              terminer"""


def executer(commande: str, saisies: list[str]) -> bool:
    """Exécute une commande ; renvoie False quand il faut quitter."""
    if commande == "aide":
        print(AIDE)
        return True

    if commande == "quitter":
        print(f"{len(saisies)} pièce(s) contrôlée(s) à la main. Au revoir.")
        return False

    if commande == "lot":
        print(rapport(LOT_A))
        return True

    if commande.startswith("mesure "):
        morceaux = commande.split()

        if len(morceaux) != 3:
            print("Commande inconnue. Tapez aide pour la liste des commandes.")
            return True

        code = morceaux[1]
        valeur = morceaux[2].replace(",", ".")

        try:
            code, mesure, verdict_piece = analyser_ligne(
                f"{code}; {valeur}"
            )
        except ValueError as e:
            print(f"Refusé : {e}")
            return True

        saisies.append(f"{code}; {valeur}")
        print(f"{code} : {mesure:.3f} mm -> {verdict_piece.lower()}")
        return True

    print("Commande inconnue. Tapez aide pour la liste des commandes.")
    return True


def main() -> None:
    print("Contrôle qualité, ligne 2. Tapez aide pour la liste des commandes.")
    saisies: list[str] = []
    continuer = True
    while continuer:
        continuer = executer(input("> ").strip(), saisies)


if __name__ == "__main__":
    main()
