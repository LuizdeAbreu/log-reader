# show_metrics

import pandas as pd
import tkinter as tk
from tkinter import ttk

# Function to display the table in a tkinter window
def show_table(df):
    # Create the main window
    root = tk.Tk()
    root.title("Metrics Table")

    # Add the DataFrame index as a column
    df = df.reset_index()

    # Create a style to center the text
    style = ttk.Style()
    style.configure("Treeview.Heading", anchor="center")
    style.configure("Treeview", rowheight=25)
    style.configure("Treeview.Cell", anchor="center")

    # Create a Treeview widget to display the table
    cols = list(df.columns)
    tree = ttk.Treeview(root, columns=cols, show='headings', style="Treeview")

    # Set the column headers
    for col in cols:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, width=100, anchor="center")

    # Add data to the table
    for index, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))

    # Place the table in the window
    tree.pack(expand=True, fill='both')

    # Start the main loop
    root.mainloop()


def show_metrics():
    df = pd.read_csv('file_modified.csv')

    # Generate the descriptive table
    df_describe = df.describe().T.round(1)

    # Display the descriptive table in a tkinter window
    show_table(df_describe)

