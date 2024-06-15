# select_file

import tkinter as tk
from tkinter import filedialog
import lasio

#selected_file = None  # Variável global para armazenar o caminho do arquivo selecionado

def select_file():
    # Function to open file dialog and return the selected file path
    def open_file():
        global selected_file
        
        # Open file dialog window
        filepath = filedialog.askopenfilename(filetypes=[("LAS Files", "*.las")])
        
        if filepath:
            try:
                # Read the selected LAS file to ensure it's valid (optional)
                las = lasio.read(filepath)

                # Update label with file path
                filepath_label.config(text=f"Selected LAS file: {filepath}")

                # Hide the open_button
                open_button.pack_forget()

                # Create Analyze button
                analyze_button = tk.Button(root, text="Analyze", command=analyze_file)
                analyze_button.pack(pady=10)

                # Set selected_file to the chosen filepath
                selected_file = filepath
                
            except Exception as e:
                filepath_label.config(text=f"Error reading LAS file: {str(e)}")

    # Function to analyze the selected file and close the window
    def analyze_file():
        root.destroy()  # Close the main window
        print(f"The selected file is: {selected_file}")  # Print selected file path (optional)

    # Create the main window
    root = tk.Tk()
    root.title("LAS File Selection")

    # Set dimensions of the main window
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Label to display information about the selected file
    filepath_label = tk.Label(root, text="No LAS file selected.")
    filepath_label.pack(pady=20)

    # Button to open the file dialog
    open_button = tk.Button(root, text="Select LAS File", command=open_file)
    open_button.pack(pady=10)

    # Start the GUI main loop
    root.mainloop()

    return selected_file









