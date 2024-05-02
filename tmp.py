from pytisean import tiseano, tiseanio
import numpy as np
dat = np.random.uniform(0,1,100)

stps, _ = tiseanio("stp", '-d1', '-m2', '-t400', '-%0.5', data=dat)
# stps, _ = tiseanio("stp", '-d1', '-t400', '-%0.5', data=dat)

