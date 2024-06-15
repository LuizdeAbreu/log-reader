import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import lasio
import pandas as pd
from sys import stdout
import pandas as pd
import tkinter as tk
from tkinter import ttk

from select_file import select_file
from lastocsv import lastocsv
from plot_curves import plot_curves
from show_metrics import show_metrics

def main():
    selected_file = select_file()
    lastocsv(selected_file)
    plot_curves()
    show_metrics()

if __name__ == "__main__":
    main()