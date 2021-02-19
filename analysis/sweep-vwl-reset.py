# Import libraries
import matplotlib.pyplot as plt, numpy as np, pandas as pd

# Chip number
CHIP = 9

# Load sweep data
cols = ['addr', 'VWL', 'VSL', 'VBL', 'PW', 'Ri', 'Rf']
dtypes = {
    'addr': np.int32,
    'VWL': np.float64,
    'VBL': np.float64,
    'VSL': np.float64,
    'PW': np.int32,
    'Ri': np.float64,
    'Rf': np.float64,
}
data = pd.read_csv(f"../data/sweep_vwl_reset_chip{CHIP}.csv", names=cols, sep="\t", dtype=dtypes)

# Convert units
data['Ri'] = data['Ri']/1000 # kOhm
data['Rf'] = data['Rf']/1000 # kOhm
data['Gi'] = 1/data['Ri']*1000 # uS
data['Gf'] = 1/data['Rf']*1000 # uS

# Iterate, plot, and save
for PW in [50, 10, 5, 1]:
    # Select pulse width
    gdata0 = data[data['PW'] == PW]
    for VSL in [4, 3, 2, 1]:
        # Select SL voltage and group by address for individual lines
        gdata = gdata0[gdata0['VSL'] == VSL]
        gdata = gdata.groupby('addr')

        # Plot resistance
        plt.figure(figsize=(4,3))
        plt.title(f'Rf @ PW={PW}us, VSL={VSL}V')
        gdata.plot(x='VWL', y='Rf', ax=plt.gca(), legend=False)
        plt.xlabel('VWL (V)')
        plt.ylabel('Final Resistance (kOhm)')
        plt.ylim(0, 100)
        plt.tight_layout()
        plt.savefig(f'figs/sweeps/sweep-vwl-reset-Rf-pw{PW}-vsl{VSL}.pdf')

        # Plot conductance
        plt.figure(figsize=(4,3))
        plt.title(f'Gf @ PW={PW}us, VSL={VSL}V')
        gdata.plot(x='VWL', y='Gf', ax=plt.gca(), legend=False)
        plt.xlabel('VWL (V)')
        plt.ylabel('Final Conductance (uS)')
        plt.ylim(0, 200)
        plt.tight_layout()
        plt.savefig(f'figs/sweeps/sweep-vwl-reset-Gf-pw{PW}-vsl{VSL}.pdf')

