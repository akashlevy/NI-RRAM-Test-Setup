# Import libraries
import matplotlib.pyplot as plt, numpy as np, pandas as pd

# Resistance states (LRS <-> 0, HRS <-> 1 in the bitstream)
LRS = 10000
HRS = 80000
ITER = 4
CHIP = 5

# Load bitstream as matrix
bs = np.loadtxt(open("../tests/testbs.csv", encoding='utf-8-sig'), delimiter=",", dtype=np.int32)
gold = bs.reshape(256, 32)
gold = gold * (HRS-LRS) + LRS

# Programming 
mat = plt.matshow(gold, vmin=0, vmax=150000)
plt.colorbar(mat)
plt.title('Target Resistance (ohm)')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('test-prog-gold.pdf')



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
data = pd.read_csv(f'../data/target_chip{CHIP}.csv', names=cols, sep='\t', dtype=dtypes, index_col='addr')[8192*ITER:8192*(ITER+1)]
data['pulses'] = data['READS'] + data['SETS'] + data['RESETS']
data['bin'] = bs[:len(data)]

# Show number of successes
print(data['success'].value_counts())

# Create matrices
pulse_mat = np.pad(data['pulses'].values, (0, 8192-len(data)), 'mean').reshape(256, 32)
r_mat = np.pad(data['R'].values, (0, 8192-len(data)), 'mean').reshape(256, 32)

# Programming pulse count
mat = plt.matshow(pulse_mat, vmin=0, vmax=50)
plt.colorbar(mat)
plt.title('Full Array Programming Pulse Count')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('test-prog-pulses.pdf')

# Programmed resistance
mat = plt.matshow(r_mat, vmin=0, vmax=150000)
plt.colorbar(mat)
plt.title('Programmed Resistance (ohm)')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('test-prog-res.pdf')

# CDF curves
plt.figure(figsize=(4,3))
plt.xlim(5, 1e3)
plt.xscale('log')
plt.title('Programmed Resistance Dist.')
for i in range(2):
    rdata = data[data['bin'] == i]
    counts, bin_edges = np.histogram(rdata['R']/1000, bins=8192, density=True)
    cdf = np.cumsum(counts)
    plt.plot(bin_edges[1:], cdf/cdf[-1]*100)
plt.xlabel('Resistance (kOhm)')
plt.ylabel('CDF (%)')
plt.tight_layout()
plt.savefig('test-prog-cdf.pdf')

# CDF curves
plt.figure(figsize=(4,3))
plt.xlim(0, 150)
plt.title('Programmed Conductance Dist.')
for i in range(2):
    rdata = data[data['bin'] == i]
    counts, bin_edges = np.histogram(1e6/rdata['R'], bins=8192, density=True)
    cdf = np.cumsum(counts)
    plt.plot(bin_edges[1:], cdf/cdf[-1]*100)
plt.xlabel('Conductance (uS)')
plt.ylabel('CDF (%)')
plt.tight_layout()
plt.savefig('test-prog-g-cdf.pdf')



# Load target output as dataframe
cols = ['addr', 'V', 'I', 'R']
dtypes = {
    'addr': np.int32,
    'V': np.float64,
    'I': np.float64,
    'R': np.float64
}
data = pd.read_csv(f'../data/read_target_chip{CHIP}.csv', names=cols, sep='\t', dtype=dtypes, index_col='addr')[8192*ITER:8192*(ITER+1)]
data['bin'] = bs[:len(data)]

# Create matrices
r_mat = np.pad(data['R'].values, (0, 8192-len(data)), 'mean').reshape(256, 32)

# Programmed resistance
mat = plt.matshow(r_mat, vmin=0, vmax=150000)
plt.colorbar(mat)
plt.title('Post-Prog. READ Resistance (ohm)')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('test-progread-res.pdf')

# CDF curves
plt.figure(figsize=(4,3))
plt.xlim(5, 1e3)
plt.xscale('log')
plt.title('Post-Prog. READ Resistance Dist.')
for i in range(2):
    rdata = data[data['bin'] == i]
    counts, bin_edges = np.histogram(rdata['R']/1000, bins=8192, density=True)
    cdf = np.cumsum(counts)
    plt.plot(bin_edges[1:], cdf/cdf[-1]*100)
plt.xlabel('Resistance (kOhm)')
plt.ylabel('CDF (%)')
plt.tight_layout()
plt.savefig('test-progread-cdf.pdf')

plt.figure(figsize=(4,3))
plt.xlim(0, 150)
plt.title('Post-Prog. READ Conductance Dist.')
for i in range(2):
    rdata = data[data['bin'] == i]
    counts, bin_edges = np.histogram(1e6/rdata['R'], bins=8192, density=True)
    cdf = np.cumsum(counts)
    plt.plot(bin_edges[1:], cdf/cdf[-1]*100)
plt.xlabel('Conductance (uS)')
plt.ylabel('CDF (%)')
plt.tight_layout()
plt.savefig('test-progread-g-cdf.pdf')



### CAMERA READY FIGURES BELOW

