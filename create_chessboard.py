
#! create a 1-65 chessboard using the below modules and display it 8 x 8 
import tkinter as tk
import pandas as pd
import numpy as np

# Step 1: Create an 8x8 grid using NumPy (representing a chessboard with values from 1 to 64)
chessboard_array = np.arange(1, 65).reshape(8, 8)

# Step 2: Convert the NumPy array to a Pandas DataFrame
chessboard_df = pd.DataFrame(chessboard_array)

# Step 3: Create a Tkinter window to display the chessboard
def show_chessboard():
    root = tk.Tk()
    root.title("8x8 Chessboard")

    # Step 4: Create labels for each cell in the grid
    for i in range(8):
        for j in range(8):
            cell_value = chessboard_df.iloc[i, j]
            # Alternate the colors for the chessboard cells
            bg_color = "white" if (i + j) % 2 == 0 else "black"
            cell = tk.Label(root, text=cell_value, borderwidth=2, relief="solid", width=5, height=3, bg=bg_color, fg="red" if bg_color == "white" else "white")
            cell.grid(row=i, column=j)

    root.mainloop()

# Display the chessboard GUI
show_chessboard()