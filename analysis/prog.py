# Import libraries
import matplotlib.pyplot as plt, numpy as np, pandas as pd

# Resistance states (LRS <-> 0, HRS <-> 1 in the bitstream)
LRS = 10000
HRS = 80000

# Load bitstream as matrix
bs = np.loadtxt(open("../tests/bitstream.csv"), delimiter=",", skiprows=0, dtype=np.int32)
gold = bs.reshape(256, 256)
gold = gold * (HRS-LRS) + LRS

# Programming 
mat = plt.matshow(gold)
plt.colorbar(mat)
plt.title('Target Resistance (ohm)')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('prog-gold.pdf')

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
data = pd.read_csv('../data/target.csv', names=cols, sep='\t', dtype=dtypes, index_col='addr')
data['pulses'] = data['READS'] + data['SETS'] + data['RESETS']
data['bin'] = bs[:len(data)]
print(data)

# Show number of successes
print(data['success'].value_counts())

# Create matrices
pulse_mat = np.pad(data['pulses'].values, (0, 65536-len(data)), 'mean').reshape(256, 256)
r_mat = np.pad(data['R'].values, (0, 65536-len(data)), 'mean').reshape(256, 256)

# # Programmed Resistance Distribution
# data['R'].hist(bins=15)
# plt.title('Programmed Resistance Distribution')
# plt.xlabel('Resistance (ohm)')
# plt.ylabel('Frequency')
# plt.savefig('form-res-dist.pdf')

# Programming pulse count
mat = plt.matshow(pulse_mat)
plt.colorbar(mat)
plt.title('Full Array Programming Pulse Count')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('prog-pulses.pdf')

# Programmed resistance
mat = plt.matshow(r_mat)
plt.colorbar(mat)
plt.title('Programmed Resistance (ohm)')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('prog-res.pdf')

# CDF curves
plt.figure(figsize=(4,3))
plt.xlim(0, 100)
plt.title('Programmed Resistance Dist.')
for i in range(2):
    rdata = data[data['bin'] == i]
    print(rdata)
    counts, bin_edges = np.histogram(rdata['R']/1000, bins=200, density=True)
    cdf = np.cumsum(counts)
    plt.plot(bin_edges[1:], cdf/cdf[-1]*100)
plt.xlabel('Resistance (kOhm)')
plt.ylabel('CDF (%)')
plt.tight_layout()
plt.savefig('prog-cdf.pdf')
