from src.test import identity
import numpy as np

assert(np.all(identity([1]) == np.ones(1)))
x_vals = np.random.random_sample(5)
assert(np.all(identity(x_vals) == x_vals))
