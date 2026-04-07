import tkinter as tk
from ui import ATM_app

def main(): 
    
    root = tk.Tk() # Creating the main or origin window of root
    
    app = ATM_app(root) # Starting the app
    
    root.mainloop() # Main loop
    
if __name__ == "__main__":
    main()