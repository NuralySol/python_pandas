
#! import pandas and numpy 
import tkinter as tk
import pandas as pd
import numpy as np

num_list = [105, 210, 315, 420, 525, 630, 735, 840, 945]

print(
    "\nnum_list: ", num_list[2:7]
)  # range of items from the index of 3 till 5 Output: [420, 525]

array = np.array(num_list)
print(
    "numpy array from a num_list: ", array
)  # [105 210 315 420 525 630 735 840 945] no commas notice that
print("\n", array.shape)  # as a tuple (9,) sideways
print("\n", array.ndim)  # 1 dimensional vector no-columns

# reshape method on.array you can twist and turn (matrices) i.e. tic-tac-toe

tic_tac_toe_array = array.reshape(3, 3)
# print and methods of array using .shape and .ndim
print("\n", tic_tac_toe_array.shape)
print("\n", tic_tac_toe_array.ndim)
print("\n", tic_tac_toe_array)
# get the rows instead of columns [0:1] for traversing the rows
print("\n first row: ", tic_tac_toe_array[0:1])
print("\n last row: ", tic_tac_toe_array[-1:])
print("\n first column:", tic_tac_toe_array[:, 0])  # get the first column [:,0])
print(
    "\n last column, last 2 rows: ", tic_tac_toe_array[-2:, -1]
)  # last column, last 2 rows [-2:, -1])
print(
    "\n first 2 rows of first 2 columns: ", tic_tac_toe_array[:2, :2]
)  # first 2 rows of first 2 columns [:2, :2])


# Original NumPy array with numbers
num_list = [105, 210, 315, 420, 525, 630, 735, 840, 945]
array = np.array(num_list)

# Reshape the array into a 3x3 Tic-Tac-Toe grid
tic_tac_toe_array = array.reshape(3, 3)

# Convert the NumPy array to a Pandas DataFrame
tic_tac_toe_df = pd.DataFrame(tic_tac_toe_array)

# Step 3: Create a Tkinter window to display the Tic-Tac-Toe grid
def show_tic_tac_toe_grid():
    root = tk.Tk()
    root.title("Tic-Tac-Toe Grid")

    # Step 4: Create labels for each cell in the grid
    for i in range(3):
        for j in range(3):
            cell_value = str(tic_tac_toe_df.iloc[i, j])  # Convert the value to string for display
            cell = tk.Label(root, text=cell_value, borderwidth=2, relief="solid", width=10, height=5)
            cell.grid(row=i, column=j)

    root.mainloop()

# Show the GUI with numbers in the Tic-Tac-Toe grid
show_tic_tac_toe_grid()