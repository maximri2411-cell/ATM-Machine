#====================================
# All of features we need to make our app great
import tkinter as tk
from storage import load_data, save_data #! Do not delete it, important for our function to use
#====================================

class ATM_app: # Creating the class for the app
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine") # The title
        self.root.geometry("800x600") # Size of ther title
        self.bank = load_data # Here we use all the function we created in the other files
        self.current_user = None 
        self.create_login_screen()
        
    def cleaning_screen(self): # Its important to clean the text after the user use or press the button
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def create_login_screen(self):
        self.cleaning_screen()
        
        # Simple window just to see if its work with some feature like the type of language
        tk.Label(self.root, text="Welcome To X ATM", font=("Ariel", 23, "bold")).pack(pady=200)
        
        # Adding fild to enter his ID number
        tk.Label(self.root, text="Account ID: ").pack()
        self.account_entry = tk.Entry(self.root)
        self.account_entry.pack(pady=5)
        
        # Adding the pin fild
        tk.Label(self.root, text="Enter PIN: ").pack()
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(paddy=5)
        
        
        # Creating a button
        tk.Button(self.root, text="Check", command=self.test_data).pack()

    def test_data(self):
        print("Another check")
        
if __name__ == "__main__": #! This will run our app evertime we run the code
    root = tk.Tk()
    app = ATM_app(root)
    root.mainloop() 