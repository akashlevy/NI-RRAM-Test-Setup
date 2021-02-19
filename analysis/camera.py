# Import libraries
import matplotlib.pyplot as plt, numpy as np, pandas as pd

# Resistance states (LRS <-> 0, HRS <-> 1 in the bitstream)
LRS = 10000
HRS = 80000
ITER = 2
CHIP = 6

# Load bitstream as matrix
bs = np.loadtxt(open("../tests/bitstream.csv"), delimiter=",", skiprows=0, dtype=np.int32)
gold = bs.reshape(256, 256)

# Programming
fig = plt.figure(figsize=(3.2,2.4))
mat = plt.gca().matshow(gold)
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.xticks(np.arange(0, 257, 64))
plt.yticks(np.arange(0, 257, 64))
cbar = fig.colorbar(mat, ticks=[0, 1])
cbar.ax.set_yticklabels(['LRS', 'HRS'])
plt.tight_layout()
plt.savefig('figs/camera-prog-gold.pdf')

# Load target output as dataframe
cols = ['addr', 'READS', 'SETS', 'RESETS', 'success', 'R']
dtypes = {
    'addr': np.int32,
    'READS': np.int32,
    'SETS': np.int32,
    'RESETS': np.int32,
    'success': np.int32,
    'R': np.float64
}
progdata = pd.read_csv(f'../data/target_chip{CHIP}.csv', names=cols, sep='\t', dtype=dtypes, index_col='addr')[65536*ITER:65536*(ITER+1)]
progdata['bin'] = bs

# Load read target output as dataframe
cols = ['addr', 'V', 'I', 'R']
dtypes = {
    'addr': np.int32,
    'V': np.float64,
    'I': np.float64,
    'R': np.float64
}
readdata = pd.read_csv(f'../data/read_target_chip{CHIP}.csv', names=cols, sep='\t', dtype=dtypes, index_col='addr')[65536*ITER:65536*(ITER+1)]
readdata['bin'] = bs

# Create matrices
prog_r_mat = progdata['R'].values.reshape(256, 256) / 1000 # kOhm
read_r_mat = readdata['R'].values.reshape(256, 256) / 1000 # kOhm

# Plot read resistance matrix
fig = plt.figure(figsize=(3.2,2.4))
mat = plt.gca().matshow(read_r_mat, vmin=0, vmax=200)
cbar = plt.colorbar(mat)
cbar.set_label('Resistance (kΩ)', rotation=270)
cbarlabels = [int(x) for x in cbar.ax.get_yticks()[:-1]] + ['>200']
cbar.ax.set_yticklabels(cbarlabels)
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.xticks(np.arange(0, 257, 64))
plt.yticks(np.arange(0, 257, 64))
plt.tight_layout()
plt.savefig('figs/camera-read-res.pdf')

# CDF curves
plt.figure(figsize=(3.2,2.4))
plt.xlim(2, 1e4)
plt.xscale('log')
#plt.title('Resistance Distribution')
for i in range(2):
    rdata = progdata[progdata['bin'] == i]
    counts, bin_edges = np.histogram(rdata['R']/1000, bins=65536, density=True)
    cdf = np.cumsum(counts)
    plt.plot(bin_edges[1:], cdf/cdf[-1]*100)
for i in range(2):
    rdata = readdata[readdata['bin'] == i]
    counts, bin_edges = np.histogram(rdata['R']/1000, bins=65536, density=True)
    cdf = np.cumsum(counts)
    plt.plot(bin_edges[1:], cdf/cdf[-1]*100, 'k--', linewidth=1)
plt.xlabel('Resistance (kΩ)')
plt.ylabel('CDF (%)')
plt.tight_layout()
plt.savefig('figs/camera-res-cdf.pdf')
