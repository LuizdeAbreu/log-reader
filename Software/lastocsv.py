# lastocsv

import os
import lasio
import pandas as pd
from sys import stdout

def lastocsv(file):
    # Read the LAS file
    las = lasio.read(file)
    lasCSV = las.to_csv('file_orig.csv')

    # Load the CSV file
    df = pd.read_csv('file_orig.csv', header=None)

    # Select the first two rows
    row1 = df.iloc[0]
    row2 = df.iloc[1]

    # Combine the two rows
    combined_row = [f"{a} [{b}]" for a, b in zip(row1, row2)]

    # Update the first row with the combined row
    df.iloc[0] = combined_row

    # Remove the second row
    df = df.drop(1).reset_index(drop=True)

    # Save the modified file
    df.to_csv('file_modified.csv', index=False, header=False)


