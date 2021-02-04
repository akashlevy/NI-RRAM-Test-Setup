# Import numpy
import numpy as np

# Create bitstream
data = np.loadtxt(open("4b_32w_1s/array_R_map_0.csv", "r"), delimiter=",", skiprows=0, dtype=np.int32).transpose().flatten()
data = np.vectorize(lambda x: 1-x)(data)
np.savetxt('bitstream.csv', data, fmt='%d')