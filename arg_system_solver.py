from arg_system_verifier import ArgSystemVerifier
import random

class ArgSystemSolver:
    """Cette classe permet de résoudre les différents problèmes
        -SE-CO 
        -DC-CO 
        -DS-CO, 
        -SE-ST 
        -DC-ST
        -DS-ST
    """
    @staticmethod
    def se_co(af):
        """Cette méthode renvoie une extension complète

        Args:
            af (ArgSystemBuilder): Système d'rgumentation
        """
        system_verifier = ArgSystemVerifier()
        
        complete_extensions = system_verifier.complete_extensions(af)
        return random.choice(complete_extensions) if complete_extensions else None

    def dc_co(af, argument):
        """Cette méthode détermine si un argumenent appartient à au moins une extension complète

        Args:
            af (ArgSystemBuilder): système d'argumentation
            argument : argument
        """
        system_verifier = ArgSystemVerifier()
        complete_extensions = system_verifier.complete_extensions(af)
        return any(argument in extension for extension in complete_extensions)

    def ds_co(af, argument):
        """Cette méthode détermine si un argument appartient à toutes les extensions complètes

        Args:
            af (ArgSystemBuilder): Système d'argumentation
            argument : argument
        """
        system_verifier = ArgSystemVerifier()
        complete_extensions = system_verifier.complete_extensions(af)
        return all(argument in extension for extension in complete_extensions)
        
        

    def se_st(af):
        """Cette méthode retourne une extension stable 

        Args:
            af (ArgSystemBuilder): Système d'argumentation
        """
        system_verifier = ArgSystemVerifier()
        stable_extensions = system_verifier.stable_extensions(af)
        return random.choice(stable_extensions) if stable_extensions else None

    def dc_st(af, argument):
        """Cette méthode détermine si un argument appartient à au moins une extension stable

        Args:
            af (ArgSystemBuilder): Système d'argumentation
            argument : argument
        """
        system_verifier = ArgSystemVerifier()
        stable_extensions = system_verifier.stable_extensions(af)
        return any(argument in extension for extension in stable_extensions)
        

    def ds_st(af, argument):
        """Cette méthode détermine si un argument appartient à toutes les extensions stables

        Args:
            af (ArgSystemBuilder): Système d'argumentation
            argument : argument
        """
        system_verifier = ArgSystemVerifier()
        stable_extensions = system_verifier.stable_extensions(af)
        return all(argument in extension for extension in stable_extensions)