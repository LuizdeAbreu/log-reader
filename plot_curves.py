# plot_curves

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_curves():

    df = pd.read_csv('file_modified.csv')

    df['BS'] = 6

    fig, axes = plt.subplots(1, 3, figsize=(12, 8), sharey=True)

    axes[0].plot(df[list(df.columns)[1]], df[list(df.columns)[0]], color='gray')
    axes[0].set_xlabel(list(df.columns)[1])
    axes[0].set_xlim(4,14)
    axes[0].tick_params(axis='x', colors='gray')
    axes[0].xaxis.set_major_locator(plt.MaxNLocator(11))

    bs = axes[0].twiny()
    bs.plot(df['BS'], df[list(df.columns)[0]], color='black')
    bs.set_xlabel('BS')
    bs.set_xlim(4,14)
    bs.xaxis.set_major_locator(plt.MaxNLocator(11))
    bs.tick_params(axis='x', colors='black')

    gr = axes[0].twiny()
    gr.plot(df[list(df.columns)[2]], df[list(df.columns)[0]], color='green')
    gr.set_xlabel(list(df.columns)[2])
    gr.set_xlim(0,150)
    gr.xaxis.set_major_locator(plt.MaxNLocator(11))
    gr.tick_params(axis='x', colors='green')

    axes[1].plot(df[list(df.columns)[7]], df[list(df.columns)[0]], color='blue')
    axes[1].set_xlabel(list(df.columns)[7])
    axes[1].set_xscale('log')
    axes[1].set_xlim(0.2,2000)
    axes[1].xaxis.set_major_locator(plt.MaxNLocator(6))
    axes[1].tick_params(axis='x', colors='blue')

    ils = axes[1].twiny()
    ils.plot(df[list(df.columns)[8]], df[list(df.columns)[0]], color='red')
    ils.set_xlabel(list(df.columns)[8])
    ils.set_xscale('log')
    ils.set_xlim(0.2,2000)
    ils.xaxis.set_major_locator(plt.MaxNLocator(6))
    ils.tick_params(axis='x', colors='red') #rotation 90

    sflu = axes[1].twiny()
    sflu.plot(df[list(df.columns)[9]], df[list(df.columns)[0]], color='black')
    sflu.set_xlabel(list(df.columns)[9])
    sflu.set_xscale('log')
    sflu.set_xlim(0.2,2000)
    sflu.xaxis.set_major_locator(plt.MaxNLocator(6))
    sflu.tick_params(axis='x', colors='black')

    axes[2].plot(df[list(df.columns)[11]], df[list(df.columns)[0]], color='blue')
    axes[2].set_xlabel(list(df.columns)[11])
    axes[2].set_xlim(45,-15)
    axes[2].xaxis.set_major_locator(plt.MaxNLocator(11))
    axes[2].tick_params(axis='x', colors='blue')

    rhob = axes[2].twiny()
    rhob.plot(df[list(df.columns)[12]], df[list(df.columns)[0]], color='red')
    rhob.set_xlabel(list(df.columns)[12])
    rhob.set_xlim(1.95,2.95)
    rhob.xaxis.set_major_locator(plt.MaxNLocator(11))
    rhob.tick_params(axis='x', colors='red')

    pef = axes[2].twiny()
    pef.plot(df[list(df.columns)[10]], df[list(df.columns)[0]], color='black')
    pef.set_xlabel(list(df.columns)[10])
    pef.set_xlim(0,10)
    pef.tick_params(axis='x', colors='black')

    for i, ax in enumerate(axes):
        ax.invert_yaxis()
        ax.xaxis.tick_top()
        ax.xaxis.set_label_position('top')
        ax.set_ylabel(list(df.columns)[0])
        ax.grid(True)

    bs.spines['top'].set_position(('outward', 80))
    gr.spines['top'].set_position(('outward', 40))

    ils.spines['top'].set_position(('outward', 80))
    sflu.spines['top'].set_position(('outward', 40))

    rhob.spines['top'].set_position(('outward', 80))
    pef.spines['top'].set_position(('outward', 40))

    plt.tight_layout()
    plt.show(block=False)