# ToDo list in Python
from tkinter import *
from tkinter import messagebox

root = Tk()             # Initialize root widget

task_list = []			# Empty List to enter tasks

def CreateTask():		# Function to create a task
    task = entry.get()
    if task != "":
        lb.insert(END, task)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("*WARNING*", "Please enter a task.")
    return

def DeleteTask():		# Function to delete a task
    lb.delete(ANCHOR)		
    return

def EditTask():         # Function to edit a task
    selected_task = lb.curselection()  # Fetching value of selected task with curselection()
    if selected_task:
        selected_task_index = selected_task[0]
        edited_task = entry.get()
        if edited_task != "":
            lb.delete(selected_task_index)  # Remove the selected task
            lb.insert(selected_task_index, edited_task)  # Insert edited task at same index
            entry.delete(0, "end")  # Clear the entry widget
        else:
            messagebox.showwarning("*WARNING*", "Please enter a task.")
    else:
        messagebox.showwarning("*WARNING*", "Please select a task to edit.")
    return

def exitf():            # Exit Function
	exit()
	return


root.geometry('600x500')    # Setting the window size
root.title('To Do List')    

root.config(bg='sky blue')  # Set bgcolor
root.resizable(width=False, height=False)   

frame = Frame(root)         # Creating frame widget
frame.pack()

heading = Label(frame, 
                text = 'ToDo List', 
                font=('Arial', '14'),
                pady='10')  # Heading 
heading.pack()

lb = Listbox(frame, 
             width='30',
             height='7',
             font=('Times New Roman', '9'),
             fg='black',
             bd='1')    # Creating listbox
lb.pack(fill=BOTH)


for task in task_list: 
	lb.insert(END, task)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

entry = Entry(root, font=('Times New Roman', 15))   # Creating entry box
entry.pack(pady=20)

button_frame = Frame(root)  # Creating button frame 
button_frame.pack(pady=20)

AddTask = Button(button_frame,
                text='Add Task',
                font=('Arial', '14'),
                bg='Light Green', padx=20, pady=10, 
                command=CreateTask)             # AddTask Button

AddTask.pack(fill=BOTH, expand=True, side=LEFT)

EditTask = Button(button_frame, 
                  text='Edit Task', 
                  font=('Arial', '14'), 
                  bg='Yellow', padx=20, 
                  pady=10, command=EditTask)    # EditTask Button

EditTask.pack(fill=BOTH, expand=True, side=LEFT)

DelTask = Button(button_frame, 
                 text='Delete Task',
                 font=('Arial', '14'), 
                 bg='Red',
                 padx=20, 
                 pady=10, 
                 command=DeleteTask)            # DeleteTask Button

DelTask.pack(fill=BOTH, expand=True, side=LEFT)

Exit = Button(button_frame,
              text='Exit', 
              font=('Arial', '14'), 
              bg='gray',
              padx=20,
              pady=10,
              command=exitf)                  # Exit Button

Exit.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()


