# Password Generator in Python 

from tkinter import *
import secrets
import string
import tkinter.messagebox

passwordgen = Tk()
passwordgen.title("Password Generator")
passwordgen.geometry('550x350')
passwordgen.resizable(width=False, height=False)


main = Label(passwordgen, # Header
             text="Password Generator", 
             font=("Times New Roman", "20"), 
             pady=20)
main.grid(row=0, column=0, columnspan=3)

length_label = Label(passwordgen,  
                     text="Enter password length (8-50):", 
                     font=("Times New Roman", "15"))
length_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

input_length = Entry(passwordgen, font=("Times New Roman", "15"))
input_length.grid(row=1, column=1, padx=10, pady=10)

include_special = IntVar() # special char checkbox
special_check = Checkbutton(passwordgen, 
                            text="Include special characters", 
                            font=("Times New Roman", "15"),
                            variable=include_special)
special_check.grid(row=2, column=1, padx=10, pady=10)


def generate_password(): # password gen function
    length = input_length.get()
    if not length.isdigit():
        tkinter.messagebox.showerror("Error", "Length must be a positive integer.")
    else:
        length = int(length)
        if length < 8 or length > 50:
            tkinter.messagebox.showerror("Error", "Length should be between 8 and 50.")
        else:
            characters = string.ascii_letters + string.digits
            if include_special.get():
                characters += string.punctuation
            password = ''.join(secrets.choice(characters) for _ in range(length))
            display_password(password)

def display_password(password): # display function
    generated_password_entry.delete(0, END)
    generated_password_entry.insert(0, password)

def reset():
	generated_password_entry.delete(0, END)
	input_length.delete(0, END)

def copy_to_clipboard(): #copy-to-clipboard
    password = generated_password_entry.get()
    passwordgen.clipboard_clear()
    passwordgen.clipboard_append(password)


generated_password = Label(passwordgen, 
                           text="Generated Password:", 
                           font=("Times New Roman", "15"))
generated_password.grid(row=3, column=0, padx=10, pady=10, sticky="e")

generated_password_entry = Entry(passwordgen, 
                           font=("Times New Roman", "15"), 
                           fg="green")
generated_password_entry.grid(row=3, column=1, padx=10, pady=10)

generate_password_button = Button(passwordgen, 
                                  text="Generate Password", 
                                  font=("Times New Roman", "15"),
                                  command=generate_password, 
                                  bg="lawn green", 
                                  fg="black")
generate_password_button.grid(row=4, column=0, padx=10, pady=10)

copy_button = Button(passwordgen, 
                     text="Copy to Clipboard", 
                     font=("Times New Roman", "15"),
                     command=copy_to_clipboard, 
                     bg="royal blue",
                     fg="white",
                     width=15)
copy_button.grid(row=4, column=1, padx=10, pady=10)

reset_button = Button(passwordgen,
					  text="Reset",
					  font=("Times New Roman", "15"),
					  width=15,
					  command=reset,
					  bg="gold")
reset_button.grid(row = 5, column=0, padx=10, pady=10)

exit_button = Button(passwordgen,
					 text="Exit",
					 font=("Times New Roman", "15"),
					 width=15,
					 command=exit,
					 bg="indian red")
exit_button.grid(row=5,column=1,padx=10,pady=10)

passwordgen.mainloop()
