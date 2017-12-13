from permutohedral.permutohedral import *
import numpy as np

x = Permutohedral()
m = np.array([[2.0, 0.0],
              [0.0, 2.0]], dtype=np.float32)

x.init(m)
x.compute(m, True)
