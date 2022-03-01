def identity(x):
    import numpy as np
    ret_val = np.zeros(len(x))
    ret_val[:] = x[:]
    return x
