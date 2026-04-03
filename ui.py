#This file made for all of our tkinter info/code 
import tkinter as tk
from tkinter import messagebox
from storage import load_data, save_data
import os
from sys import platform
import customtkinter

# Creating our opening window
width = 700 
height = 400

root = customtkinter.CTk()
root.title("Login System")

x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 3) - (width // 3)
root.geometry("{}x{}+{}+{}".format(width, height, x, y))
root.resizable(False, False)


root.mainloop() # Activate the app 