import tkinter as tk
import pandas as pd
import numpy as np


#! Sample menu data (data can be fed using the api in a dict format ala JSON)
data = {
    'Food': ['Burger', 'Salad', 'Pizza', 'Pasta', 'Sushi'],
    'Price ($)': [8.99, 7.50, 12.00, 10.50, 15.00],
    'Vegan': [False, True, False, False, True],
    'Calories': [800, 300, 900, 700, 500]
}

# Create a DataFrame using Pandas
menu_df = pd.DataFrame(data)

# Function to display the menu in a tkinter window
def show_menu():
    root = tk.Tk()
    root.title("Restaurant Menu")
    
    # Set up the labels for the DataFrame
    for i, col in enumerate(menu_df.columns):
        header = tk.Label(root, text=col, borderwidth=2, relief="solid", width=15)
        header.grid(row=0, column=i)
    
    # Display each row of the DataFrame
    for i in range(len(menu_df)):
        for j in range(len(menu_df.columns)):
            cell = tk.Label(root, text=str(menu_df.iloc[i, j]), borderwidth=2, relief="solid", width=15)
            cell.grid(row=i+1, column=j)
    
    root.mainloop()

# Show the menu using tkinter GUI
show_menu()