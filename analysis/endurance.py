# Import libraries
import matplotlib.pyplot as plt, numpy as np, pandas as pd

# Load bitstream as matrix
R = np.loadtxt(open("../data/endurance.csv"), delimiter="\t", skiprows=0, dtype=np.float64)
R = R/1000 # kOhm
G = 1e3/R # uS

cycle = np.arange(0, 150000, step=500)
plt.figure(figsize=(4,3))
plt.xlabel("Cycle")
plt.ylabel("Resistance (kOhm)")
plt.ylim(0, 100)
plt.plot(cycle[:len(R)], R, ".")
plt.tight_layout()
plt.savefig("figs/endurance-R.pdf")

plt.figure(figsize=(4,3))
plt.xlabel("Cycle")
plt.ylabel("Conductance (uS)")
plt.plot(cycle[:len(G)], G, ".")
plt.tight_layout()
plt.savefig("figs/endurance-G.pdf")
