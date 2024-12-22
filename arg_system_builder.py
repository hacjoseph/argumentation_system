import sys

class ArgSystemBuilder:
    """Cette classe permet de dire et analyser les fichiers pour construire un 
        un système d'argumentation
    """
    def __init__(self) -> None:
        self.arguments = set()
        self.attacks = set()

    def add_argument(self, argument):
        """Ette méthode permet d'ajouter un argument à l'ensembles des arguments

        Args:
            argument (str): argument à ajouter
        """
        self.arguments.add(argument)
        
    def add_attack(self, attaquant, attaque):
        """Cette méthode paemet d'ajouter une attaque à l'ensembles des attaques

        Args:
            attaquant (str): l'agument qui attaque
            attaque (str): l'argument qui est attaqué
        """
        self.attacks.add((attaquant, attaque))
        
    def get_from_file(fichier):
        system_argumentation = ArgSystemBuilder()
        line_number = 0
        try:
            with open(fichier, 'r') as f:
                for ligne in f:
                    line_number += 1
                    ligne = ligne.strip()
                    try:
                        if not ligne:
                            continue
                        if ligne.startswith("arg("):
                            if ligne.endswith(")."):
                                arg = ligne[4:-2]
                                system_argumentation.add_argument(arg)
                            elif ligne.endswith(")"):
                                arg = ligne[4:-1]
                                system_argumentation.add_argument(str(arg))
                            elif not ligne.endswith(")."):
                                raise ValueError("La définition d'argument est incorrecte.")
                        elif ligne.startswith("att("):
                            if ligne.endswith(")."):
                                parties = ligne.strip()[4:-2].split(',')
                                system_argumentation.add_attack(parties[0], parties[1])
                            elif ligne.endswith(")"):
                                parties = ligne.strip()[4:-1].split(',')
                                system_argumentation.add_attack(parties[0], parties[1])
                            elif not ligne.endswith(")."):
                                raise ValueError("La définition de l'attaque est incorrecte.")
                        else:
                            print("Le fichier n'est pas bien formé")
                    except ValueError as e:
                        print(f"Erreur à la ligne {line_number} du ficher : {e}")
                        sys.exit(1)
            return system_argumentation
        except FileNotFoundError:
            return None