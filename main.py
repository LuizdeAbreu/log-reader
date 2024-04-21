import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/welldata.csv')
df.head()

df['BS'] = 6

fig, axes = plt.subplots(1, 3, figsize=(12, 8), sharey=True)

axes[0].plot(df['CALI'], df['DEPT'], color='gray')
axes[0].set_xlabel('CALI')
axes[0].set_xlim(4,14)
axes[0].tick_params(axis='x', colors='gray')
axes[0].xaxis.set_major_locator(plt.MaxNLocator(11))

bs = axes[0].twiny()
bs.plot(df['BS'], df['DEPT'], color='black')
bs.set_xlabel('BS')
bs.set_xlim(4,14)
bs.xaxis.set_major_locator(plt.MaxNLocator(11))
bs.tick_params(axis='x', colors='black')

gr = axes[0].twiny()
gr.plot(df['SGR'], df['DEPT'], color='green')
gr.set_xlabel('SGR')
gr.set_xlim(0,150)
gr.xaxis.set_major_locator(plt.MaxNLocator(11))
gr.tick_params(axis='x', colors='green')

axes[1].plot(df['ILD'], df['DEPT'], color='blue')
axes[1].set_xlabel('ILD')
axes[1].set_xscale('log')
axes[1].set_xlim(0.2,2000)
axes[1].xaxis.set_major_locator(plt.MaxNLocator(6))
axes[1].tick_params(axis='x', colors='blue')

ils = axes[1].twiny()
ils.plot(df['ILM'], df['DEPT'], color='red')
ils.set_xlabel('ILM')
ils.set_xscale('log')
ils.set_xlim(0.2,2000)
ils.xaxis.set_major_locator(plt.MaxNLocator(6))
ils.tick_params(axis='x', colors='red') #rotation 90

sflu = axes[1].twiny()
sflu.plot(df['SFLU'], df['DEPT'], color='black')
sflu.set_xlabel('SFLU')
sflu.set_xscale('log')
sflu.set_xlim(0.2,2000)
sflu.xaxis.set_major_locator(plt.MaxNLocator(6))
sflu.tick_params(axis='x', colors='black')

axes[2].plot(df['NPHI'], df['DEPT'], color='blue')
axes[2].set_xlabel('NPHI')
axes[2].set_xlim(45,-15)
axes[2].xaxis.set_major_locator(plt.MaxNLocator(11))
axes[2].tick_params(axis='x', colors='blue')

rhob = axes[2].twiny()
rhob.plot(df['RHOB'], df['DEPT'], color='red')
rhob.set_xlabel('RHOB')
rhob.set_xlim(1.95,2.95)
rhob.xaxis.set_major_locator(plt.MaxNLocator(11))
rhob.tick_params(axis='x', colors='red')

pef = axes[2].twiny()
pef.plot(df['PEF'], df['DEPT'], color='black')
pef.set_xlabel('PEF')
pef.set_xlim(0,10)
pef.tick_params(axis='x', colors='black')

for i, ax in enumerate(axes):
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.set_ylabel('Depth (m)')
    ax.grid(True)

bs.spines['top'].set_position(('outward', 80))
gr.spines['top'].set_position(('outward', 40))

ils.spines['top'].set_position(('outward', 80))
sflu.spines['top'].set_position(('outward', 40))

rhob.spines['top'].set_position(('outward', 80))
pef.spines['top'].set_position(('outward', 40))

plt.tight_layout()
plt.show()