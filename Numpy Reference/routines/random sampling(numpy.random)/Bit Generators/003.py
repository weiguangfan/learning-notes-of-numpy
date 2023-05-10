from numpy.random import PCG64,SeedSequence
entropy = 0x87351080e25cb0fad77a44a3be03b491
base_seq = SeedSequence(entropy)
print(base_seq)
# SeedSequence(
#     entropy=179721305894280118117630397609131881617,
# )
child_seqs = base_seq.spawn(12)
print(child_seqs)
"""
[SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(0,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(1,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(2,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(3,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(4,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(5,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(6,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(7,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(8,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(9,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(10,),
), SeedSequence(
    entropy=179721305894280118117630397609131881617,
    spawn_key=(11,),
)]
"""
generators = [PCG64(seq) for seq in child_seqs]
print(generators)
"""
[<numpy.random._pcg64.PCG64 object at 0x000002007F37FF68>, <numpy.random._pcg64.PCG64 object at 0x000002007FD82048>, <numpy.random._pcg64.PCG64 object at 0x000002007FD820F8>, <numpy.random._pcg64.PCG64 object at 0x000002007FD821A8>, <numpy.random._pcg64.PCG64 object at 0x000002007FD82258>, <numpy.random._pcg64.PCG64 object at 0x000002007FD82308>, <numpy.random._pcg64.PCG64 object at 0x000002007FD823B8>, <numpy.random._pcg64.PCG64 object at 0x000002007FD82468>, <numpy.random._pcg64.PCG64 object at 0x000002007FD82518>, <numpy.random._pcg64.PCG64 object at 0x000002007FD825C8>, <numpy.random._pcg64.PCG64 object at 0x000002007FD82678>, <numpy.random._pcg64.PCG64 object at 0x000002007FD82728>]

"""