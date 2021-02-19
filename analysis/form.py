# Import libraries
import matplotlib.pyplot as plt, numpy as np, pandas as pd

# Chip number
CHIP = 9

# Load FORMing data
cols = ['addr', 'VWL', 'VBL', 'R', 'success']
dtypes = {
    'addr': np.int32,
    'VWL': np.float64,
    'VBL': np.float64,
    'R': np.float64,
    'success': np.int32
}
data = pd.read_csv(f'../data/form_chip{CHIP}.csv', names=cols, sep='\t', dtype=dtypes, index_col='addr')

# Replace failed data
#data_failed = pd.read_csv('../data/form_failed_chip3.csv', names=cols, sep='\t', dtype=dtypes, index_col='addr')
#data_failed2 = pd.read_csv('../data/form_failed2_chip3.csv', names=cols, sep='\t', dtype=dtypes, index_col='addr')
#data.update(data_failed)
#data.update(data_failed2)

# Hack to prevent unFORMed cells from messing up resistance distribution
data.loc[(data['success'] == 0), 'R'] = 20000

# Show number of successes
print(data['success'].value_counts())

# Save failures
np.savetxt('output/form-fails.csv', data.index[data['success'] == 0].values, fmt='%d')

# Create matrices
success_mat = data['success'].values.reshape(256, 256)
vwl_mat = data['VWL'].values.reshape(256, 256)
r_mat = data['R'].values.reshape(256, 256)

# VWL Distribution
data['VWL'].hist(bins=np.arange(0.875, 1.525, 0.05))
plt.title('VWL Distribution')
plt.xlabel('VWL (V)')
plt.ylabel('Frequency')
plt.savefig('figs/form-vwl-dist.pdf')

# FORMed Resistance Distribution
data['R'].hist(bins=15)
plt.title('FORMed Resistance Distribution')
plt.xlabel('Resistance (ohm)')
plt.ylabel('Frequency')
plt.savefig('figs/form-res-dist.pdf')

# FORMing success/yield
mat = plt.matshow(success_mat)
plt.colorbar(mat)
plt.title('Full Array FORM Sucesss')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('figs/form-success.pdf')

# FORMing VWL
mat = plt.matshow(vwl_mat)
plt.colorbar(mat)
plt.title('Full Array FORM VWL (V)')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('figs/form-vwl.pdf')

# FORMed resistance
mat = plt.matshow(r_mat)
plt.colorbar(mat)
plt.title('Full Array FORM Resistance (ohm)')
plt.xlabel('BL/SL #')
plt.ylabel('WL #')
plt.savefig('figs/form-res.pdf')
