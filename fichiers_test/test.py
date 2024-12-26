from arg_system_builder import ArgSystemBuilder
from arg_system_verifier import ArgSystemVerifier
from arg_system_solver import ArgSystemSolver

# arg  = ArgSystemBuilder()
# arg.add_argument('a')
# arg.add_argument('b')
# arg.add_argument('c')
# arg.add_argument('d')
# arg.add_attack('a', 'b')
# arg.add_attack('b', 'c')
# arg.add_attack('b', 'd')

arg = ArgSystemBuilder.get_from_file("fichiers_test/test_af1.apx")
# arg1 = ArgSystemBuilder()
# arg1.attacks = {'a', 'b', 'c', 'd'}
# attacks = {('a', 'b'), ('b', 'c'), ('b', 'd')}

# print(f"Arguments: {arg.arguments}\n")
# print(f"Attaques: {list(arg.attacks)}\n")

agrs = ArgSystemVerifier()
# no_conflit = agrs.all_free_subset(arg)
# print(f"Sans conflits: {no_conflit}\n")

# adms = agrs.all_admissible_sets(arg)

# print(f"Admissibles: {adms}\n")
    
compt = agrs.complete_extensions(arg)
print(f"complte : {compt}\n")

# stab = agrs.stable_extensions(arg)
# print(f"Stable: {stab}")

se_co = ArgSystemSolver.se_co(af=arg)

print("###################Credious Complete################")
for argument in arg.arguments:
    dc_co = ArgSystemSolver.dc_co(af=arg, argument=argument)
    print(f"{argument}: {dc_co}")
print("###################Spectical Complete################")
for argument in arg.arguments:
    ds_co = ArgSystemSolver.ds_co(af=arg, argument=argument)
    print(f"{argument}: {ds_co}")

se_st = ArgSystemSolver.se_st(arg)

print("\n\n###################Credious Stable################")
for argument in arg.arguments:
    dc_st = ArgSystemSolver.dc_st(af=arg, argument=argument)
    print(f"{argument}: {dc_st}")

print("###################Spectical Stable################")  
for argument in arg.arguments:
    ds_st = ArgSystemSolver.ds_st(af=arg, argument=argument)
    print(f"{argument}: {ds_st}")

# print(se_st)

