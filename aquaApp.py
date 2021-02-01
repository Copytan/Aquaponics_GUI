import tkinter as tk
from tkinter import filedialog, Text
from aquaFunctions import *
import os



# You can attack buttons to root or frame
root = tk.Tk()

# Creates the dimensions of the application and meshes with root (Canvas Widget)
canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

# Create a frame widget inside our canvas
frame = tk.Frame(root, bg="blue")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Buttons
submitButton = tk.Button(root, text="Submit", padx=10, pady=5, command=firstApp)
submitButton.pack()

# Executes the root
root.mainloop()