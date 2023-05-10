from numpy.random import PCG64,Generator
rng = Generator(PCG64())
print(rng)
# Generator(PCG64)
print(rng.standard_normal())
# 1.0054121461846355
