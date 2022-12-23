from tkinter import *
from tkinter import messagebox

class Login:
    #main page
    def __init__(self, root, main):
        self.frame = Frame(root, width=150, height=200, bg="white")
        self.main = main
        self.root = root


        #login_page
        self.welcome_text = Label(self.frame, text="Welcome! Please Login", font=('arial', 13), bg="white")
        self.welcome_text.pack(pady=5)

        #Username
        self.username_text = Label(self.frame, text="Username :", fg="black", font=('arial', 13, 'bold'), bg='white')
        self.username_text.pack(pady=5)

        #username entry
        self.user_entry = Entry(self.frame, width=25, bg='white', font=('arial', 13, 'bold'))
        self.user_entry.pack(pady=5)

        #Password
        self.password_text = Label(self.frame, text="Password :", fg="black", font=('arial', 13, 'bold'), bg='white')
        self.password_text.pack(pady=5)
        
        #pasword entry
        self.pass_entry = Entry(self.frame, show='*', width=25, bg='white', font=('', 13))
        self.pass_entry.pack(pady=5)
        
        #Login_verfy_button
        self.login_button = Button(self.frame, text="Login",fg="black", font=('arial', 13, 'bold'),command=self.login_verfy)
        self.login_button.pack(pady=5)


    def login_verfy(self):
        if self.user_entry.get() == "admin" and self.pass_entry.get() == "admin":
            messagebox.showinfo("Login", "You have logged in successfully")
            self.frame.pack_forget()
            self.main.frame.pack()
            self.root.title("Library System")
            
        else:
            messagebox.showerror("Error", "Login failed")
            
