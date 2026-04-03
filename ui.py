#====================================
# All of features we need to make our app great
import tkinter as tk
from storage import load_data, save_data #! Do not delete it, important for our function to use
#====================================

class ATM_app: # Creating the class for the app
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine") # The title
        self.root.geometry("400x500") # Size of ther title
#====================================
        
        self.bank = load_data # Here we use all the function we created in the other files
        
        self.current_user = None # Here we save the Accounts after the log
        
        # Simple window just to see if its work with some feature like the type of language
        tk.Label(self.root, text="Bank", font=("Ariel", 18)).pack(pady=20)
        
        # Creating a button
        tk.button(self.root, text="Check", command=self.test_data).pack()

    def test_data(self):
        print("Another check")
        
if __name__ == "__main__": #! This will run our app evertime we run the code
    root = tk.Tk()
    app = ATM_app(root)
    root.mainloop() 