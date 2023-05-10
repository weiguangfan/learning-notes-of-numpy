from numpy.random import PCG64,SeedSequence
entropy = 0x87351080e25cb0fad77a44a3be03b491
sequences = [SeedSequence((entropy,work_id,)) for work_id in range(12)]
print(sequences)
"""
[SeedSequence(
    entropy=(179721305894280118117630397609131881617, 0),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 1),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 2),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 3),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 4),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 5),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 6),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 7),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 8),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 9),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 10),
), SeedSequence(
    entropy=(179721305894280118117630397609131881617, 11),
)]

"""
generators = [PCG64(seq) for seq in sequences]
print(generators)
"""
[<numpy.random._pcg64.PCG64 object at 0x000002502FF5FF68>, <numpy.random._pcg64.PCG64 object at 0x0000025030962048>, <numpy.random._pcg64.PCG64 object at 0x00000250309620F8>, <numpy.random._pcg64.PCG64 object at 0x00000250309621A8>, <numpy.random._pcg64.PCG64 object at 0x0000025030962258>, <numpy.random._pcg64.PCG64 object at 0x0000025030962308>, <numpy.random._pcg64.PCG64 object at 0x00000250309623B8>, <numpy.random._pcg64.PCG64 object at 0x0000025030962468>, <numpy.random._pcg64.PCG64 object at 0x0000025030962518>, <numpy.random._pcg64.PCG64 object at 0x00000250309625C8>, <numpy.random._pcg64.PCG64 object at 0x0000025030962678>, <numpy.random._pcg64.PCG64 object at 0x0000025030962728>]

"""