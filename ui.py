#====================================
# All of features we need to make our app great
import tkinter as tk
from tkinter import messagebox
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
        self.pin_entry.pack(pady=5)
        
        # Normal user login button
        tk.Button(self.root, text="Login", command=self.normal_login, bg="blue").pack(pady=15)
        
        # Admin login button
        tk.Button(self.root, text="Admin Access", command=self.admin_screen, bg="lightblue").pack(pady=5)
        
    def normal_login(self): # Taking data from GUI fild
        accout_id = self.account_entry.get()
        pin = self.pin_entry.get()
        
        user, message = self.bank.login_account(accout_id, pin)
        
        if user:
            self.current_user = user
        
        
        else:
            messagebox.showerror("Login Failed", message)
            messagebox.showinfo("Success", message)
            self.show_menu_user()

    # Admin screet creation
    def admin_screen(self):
        messagebox.showinfo("Admin", "Loading... Please wait")
        
    # User screen creation
    def user_screen(self):
        self.cleaning_screen()
        tk.Label(self.root, tex=f"Welcome back, \n{self.current_user.full_name}", font=("Ariel", 13)).pack(pady=15)
        
if __name__ == "__main__": #! This will run our app evertime we run the code
    root = tk.Tk()
    app = ATM_app(root)
    root.mainloop() 