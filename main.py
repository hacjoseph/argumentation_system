import argparse
from arg_system_builder import ArgSystemBuilder
from arg_system_solver import ArgSystemSolver
from rich import print

def main():
    parser = argparse.ArgumentParser(description="Application permettant de resoudre les problèmes d'un Système d'argumentation AF")
    parser.add_argument("-p", type=str, required=True, help="Le type de problème (SE-XX, DC-XX, DS-XX)")
    parser.add_argument("-f", type=str, required=True, help="Fichier permettant de construire le système d'argumentation")
    parser.add_argument("-a", help="Argument nécessaire pour les problèmes de type (DC-XX, DS-XX)")

    args = parser.parse_args()
    
    # Construction du système d'argumentation à partir fichier saisi en ligne de commande
    argumentatoin_system = ArgSystemBuilder.get_from_file(args.f)
    if argumentatoin_system is None:
        print("[red]Impossible de continuer : le fichier n'exixte pas ou le chemin du fichier est incorrecte[/red]")
    else:
        # Identification et résolution de problème
        problem = args.p.upper()
        if problem == "SE-CO":
            co_extension = ArgSystemSolver.se_co(af=argumentatoin_system)
            if co_extension == []:
                print("[]")
            else:
                print(f"[{','.join(co_extension)}]" if co_extension else "NO")
        elif problem == "SE-ST":
            st_extension = ArgSystemSolver.se_st(af=argumentatoin_system)
            if st_extension == []:
                print("[]")
            else:
                print(f"[{','.join(st_extension)}]" if st_extension else "NO")
        elif problem in {"DC-CO", "DS-CO", "DC-ST", "DS-ST"}:
            if not args.a:
                print("Il manque l'argument '-a' pour ce type de problème")
                return
            elif args.a not in argumentatoin_system.arguments:
                print(f"L'argument [red]'{args.a}'[/red] n'existe pas dans le systeme d'argumentation. Ensemble des arguments: [green]{argumentatoin_system.arguments}[/green]")
                return
            
            argument = args.a
            if problem == "DC-CO":
                result = ArgSystemSolver.dc_co(af=argumentatoin_system, argument=argument)
            elif problem == "DS-CO":
                result = ArgSystemSolver.ds_co(af=argumentatoin_system, argument=argument)
            elif problem == "DC-ST":
                result = ArgSystemSolver.dc_st(af=argumentatoin_system, argument=argument)
            elif problem == "DS-ST":
                result = ArgSystemSolver.ds_st(af=argumentatoin_system, argument=argument)
            
            print("[bold green] YES [/bold green]" if result else "[bold red] NO [/bold red]")
        else:
            print("[red]Le type de problème est inconnu.[/red] [green]Les différents types de problèmes: SE-XX, DC-XX ou DS-XX. XX= CO ou ST[/green]")

if __name__== "__main__":
    main()