from itertools import chain, combinations


class ArgSystemVerifier:
    """Cette classe permet de vérifier si un système d'argumentation est:
        -Sans confilt
        -un ensembles admissible
        -une extension complète
        -une extension stable
    """
    
    def gen_subsets(self,arguments):
        """Cette méthode permet de générer des sous-ensembles à partir des arguments

        Args:
            arguments : Liste des arguments
        """
        s = list(arguments)
        return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
    
    def is_no_conflit(self,af, subset):
        """_summary_

        Args:
            af : System d'argumentation 
            subset : Sous ensemble des enguments dont on veut verifier s'il est sans conflit ou pas.
        """
        
        # convertir le sunset en ensemble pour une recherche plus rapide
        
        subset_set = set(subset)
        for (a, b) in af.attacks:
            if a in subset_set and b in subset_set:
                return False
            
        return True
    
    def all_free_subset(self,af):
        """Cette méthode retourne la liste de tous les sous ensembles sans conflit

        Args:
            af : système d'argumentation

        Returns:
            ensembles_sans_conlit: la liste de tous les sous-ensmbles sans conflits
        """
        ensembles_sans_conlit = []
        for subset in self.gen_subsets(af.arguments):
            if self.is_no_conflit(af = af, subset = subset):
                ensembles_sans_conlit.append(list(subset))
    
        return ensembles_sans_conlit
    
    def is_argument_defended(self, argument, subset, af):
        """Cette méthode permet de vérifier si un sous-ensemble défend ses arguments

        Args:
            argument : argument dont on veut vérifier s'il est défendu ou pas
            subset : sous ensembles qui défend ses argument 
            argumentation_system (ArgSystemBuilder): Systèmes d'argumentation

        Returns:
            retourne True si l'argument est défendu sinon False
        """
        for attacker in {a for a, b in af.attacks if b == argument}:
            if not any((defender, attacker) in af.attacks for defender in subset):
                return False
        return True
    
    def is_admissible(self, subset, af):
        """Cette méthode permet de vérifier si un sous-ensemble est sans conflit

        Args:
            subset: sous-ensemble
            af (ArgSystemBuilder): système d'argumentation

        Returns:
            La méthode retourne False s'il y'a un conflit dans le sous-ensemble sinon elle vérifie si tous les arguments sont défendu
        """
        
        if not self.is_no_conflit(af = af, subset = subset):
            return False
        
        for argument in subset:
            # Si l'argument n'est pas défendu retourner False
            if not self.is_argument_defended(argument=argument, subset=subset, af=af):
                return False
        return True
    
    
    def all_admissible_sets(self,af):
        """Cette méthode retourne la liste de tous les sous-ensembles admissibles

        Args:
            af : systeme d'argumentation

        Returns:
            admissible_sets: liste de tous les sous-ensembles admissibles
        """
        admissible_sets = []
        for subset in self.gen_subsets(af.arguments):
            if self.is_admissible(subset=subset, af=af):
                admissible_sets.append(list(subset))
        return admissible_sets
    
    def complete_extensions(self, af):
        """Cette méthode retourne toutes les extensions complètes

        Args:
            argumentation_system (ArgSystemBuilder): Système d'argumentation

        Returns:
            Retourne une liste des extension complètes
        """
        complete_extentions = []
        for subset in self.all_admissible_sets(af):
            # if self.is_admissible(subset=subset, argumentation_system=argumentation_system):
            defended_arguments = [
                a for a in af.arguments if all(
                    (attacker, a) not in af.attacks or 
                    any((defender, attacker) in af.attacks for defender in subset)
                    for attacker in af.arguments
                )
            ]
            if list(subset) == defended_arguments:
                complete_extentions.append(list(subset))
        return complete_extentions
    
    
    def stable_extensions(self, af):
        """Cette méthode retourn toutes les extensions stables

        Args:
            af (ArgSystemBuilder): Systeme d'argumentation

        Returns:
            une liste des extensions stables
        """
        stable_extensions = []
        for subset in self.all_free_subset(af):
            if self.is_no_conflit(af = af, subset = subset):
                attacked = [target for attacker in subset for (attacker2, target) in af.attacks if attacker == attacker2]
                
            if set(attacked) == af.arguments - set(subset):
                stable_extensions.append(list(subset))
        return stable_extensions