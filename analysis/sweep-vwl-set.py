# Import libraries
import matplotlib.pyplot as plt, numpy as np, pandas as pd

# Chip number
CHIP = 9

# Load sweep data
cols = ['addr', 'VWL', 'VBL', 'VSL', 'PW', 'Ri', 'Rf']
dtypes = {
    'addr': np.int32,
    'VWL': np.float64,
    'VBL': np.float64,
    'VSL': np.float64,
    'PW': np.int32,
    'Ri': np.float64,
    'Rf': np.float64,
}
data = pd.read_csv(f"../data/sweep_vwl_set_chip{CHIP}.csv", names=cols, sep="\t", dtype=dtypes)

# Convert units
data['Ri'] = data['Ri']/1000 # kOhm
data['Rf'] = data['Rf']/1000 # kOhm
data['Gi'] = 1/data['Ri']*1000 # uS
data['Gf'] = 1/data['Rf']*1000 # uS

# Iterate, plot, and save
for PW in [50, 10, 5, 1]:
    # Select pulse width
    gdata0 = data[data['PW'] == PW]
    for VBL in [2.5, 2, 1.5, 1]:
        # Select bitline voltage and group by address for individual lines
        gdata = gdata0[gdata0['VBL'] == VBL]
        gdata = gdata.groupby('addr')

        # Plot resistance
        plt.figure(figsize=(4,3))
        plt.title(f'Rf @ PW={PW}us, VBL={VBL}V')
        gdata.plot(x='VWL', y='Rf', ax=plt.gca(), legend=False)
        plt.xlabel('VWL (V)')
        plt.ylabel('Final Resistance (kOhm)')
        plt.ylim(0, 100)
        plt.tight_layout()
        plt.savefig(f'figs/sweeps/sweep-vwl-set-Rf-pw{PW}-vbl{VBL}.pdf')

        # Plot conductance
        plt.figure(figsize=(4,3))
        plt.title(f'Gf @ PW={PW}us, VBL={VBL}V')
        gdata.plot(x='VWL', y='Gf', ax=plt.gca(), legend=False)
        plt.xlabel('VWL (V)')
        plt.ylabel('Final Conductance (uS)')
        plt.ylim(0, 200)
        plt.tight_layout()
        plt.savefig(f'figs/sweeps/sweep-vwl-set-Gf-pw{PW}-vbl{VBL}.pdf')

