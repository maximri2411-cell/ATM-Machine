#===================================
# All of features we need to make our app great
import tkinter as tk
from tkinter import messagebox
from storage import load_data, save_data #! Do not delete it, important for our function to use

# =======================================================
#================ opening screen of the app =============
#========================================================

class ATM_app: # Creating the class for the app
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine") # The title
        self.root.geometry("800x600") # Size of ther title
        self.root.configure(bg="midnight blue") # bg color
        self.bank = load_data() # Here we use all the function we created in the other files
        self.current_user = None 
        self.create_login_screen()
        
    def cleaning_screen(self): # Its important to clean the text after the user use or press the button
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def create_login_screen(self):
        self.cleaning_screen()
        
        # Simple window just to see if its work with some feature like the type of language
        tk.Label(self.root, text="Welcome To X ATM", font=("Arial", 36, "bold"), bg="midnight blue", fg="ivory").pack(pady=50)
        
        # Adding fild to enter his ID number
        tk.Label(self.root, text="Account ID: ",font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack()
        self.account_entry = tk.Entry(self.root, width=25, font=("Arial",16), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71" )
        self.account_entry.pack(pady=10, ipady=8)

        # Adding the pin fild
        tk.Label(self.root, text="Enter PIN: ", font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack()
        self.pin_entry = tk.Entry(self.root, show="*", width=25, font=("Arial",16), justify="center", bg="slate gray",fg="white",insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71")
        self.pin_entry.pack(pady=10, ipady=8)
        
        # Normal user login button
        tk.Button(self.root, text="Login", command=self.normal_login,font=("Arial", 11 , "bold"), width=15, activebackground="#b8962e", cursor="hand2" , bg="gold", fg="midnight blue" ).pack(pady=(25, 10))
    
        # Admin login button
        tk.Button(self.root, text="Admin Access", command=self.admin_screen,font=("Arial", 11, "bold"), bg="#2d3e50", fg="white", borderwidth=0, cursor="hand2"  ).pack(pady=5)
  


#=======================================================
#================== Login and menu of user =============
#=======================================================

    def normal_login(self): # Taking data from GUI fild
        accout_id = self.account_entry.get()
        pin = self.pin_entry.get()
        
        user, message = self.bank.login_account(accout_id, pin)
        
        if user:
            self.current_user = user
            messagebox.showinfo("Success", message)# Line up that every success entry must be like this
            self.user_screen() # Moving to the user screen
        else:
            messagebox.showerror("Login Failed", message) # Line up thst every fail entry must be like this
            
    
    def user_screen(self): # User screen creation
        self.cleaning_screen()
        tk.Label(self.root, text=f"Welcome back,{self.current_user.full_name}", font=("Arial", 20, "bold"), bg="midnight blue", fg="ivory").pack(pady=15)
        tk.Button(self.root, text="Withdraw", width=25, font=("Arial", 18), bg="#2d3e50", fg="white").pack(pady=20)
        tk.Button(self.root, text="Deposit", width=25, font=("Arial", 18), bg="#2d3e50", fg="white").pack(pady=20)
        tk.Button(self.root, text="Balance", width=25, font=("Arial", 18), bg="#2d3e50", fg="white").pack(pady=20)
        tk.Button(self.root, text="Logout", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=40)
              
      
#=======================================================
#================== Balance page =======================
#======================================================= 
      
    def check_balance_action(self):
        self.cleaning_screen()
        tk.Label(self.root, text="YOUR BALANCE:", font=("Arial", 28, "bold"), bg="midnight blue", fg="gold").pack(pady=(40, 10))
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"₪ {current_balance:,.2f}", font=("Arial", 32, "bold"), bg="midnight blue", fg="white").pack(pady=20)
        tk.Label(self.root, text="Transaction History:", font=("Arial", 14), bg="midnight blue", fg="ivory").pack(pady=(20, 5))
                 
        history_list = tk.Listbox(self.root, width=70, height=10, font=("Arial", 10), bg="slate gray", fg="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71", justify="center").pack(pady=10)  
        user_history = self.current_user.see_history()
        if not user_history:
            history_list.insert("end", "No operations yet")
        else:
            for entry in reversed(user_history): 
                text = f"{entry['date']} | {entry['operation']}: {entry['amount']} NIS | After: {entry['amount_after']}"
                history_list.insert("end", text)
                
        tk.Button(self.root, text="Balance", width=25, font=("Arial", 18), bg="#2d3e50", fg="white", command=self.check_balance_action).pack(pady=20)
                  
          

#=======================================================
#================ Login and menu of manager ============
#=======================================================

    # Admin screet creation
    def admin_screen(self):
        messagebox.showinfo("Admin", "Loading... Please wait")
        
        
if __name__ == "__main__": #! This will run our app evertime we run the code
    root = tk.Tk()
    app = ATM_app(root)
    root.mainloop() 
    
    
    
    
    
    
    