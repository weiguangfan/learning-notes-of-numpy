from numpy.random import PCG64,SeedSequence
# seed = get_user_seed()
seed = 120
ss = SeedSequence(seed)
print(ss)
# SeedSequence(
#     entropy=120,
# )
print('seed={}'.format(ss.entropy))
# seed=120
bg = PCG64(ss)
print(bg)
# <numpy.random._pcg64.PCG64 object at 0x000002A7B423FF68>