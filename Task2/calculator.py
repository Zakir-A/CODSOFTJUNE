#Calculator in Python
from tkinter import *
import math

calculator = Tk()
calculator.geometry('300x330')
calculator.title("Calculator")
calculator.resizable(width=False, height=False)

#colours
calculator.configure(bg="#333333")
num_color = "#CCCCCC"
op_color = "#FF9900" 

main = Label(calculator, font=("Times New Roman", "30"), width = 12)
#Label where content is displayed
main.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

expression = "" # Variable to store expression
input_dig_limit = 12
output_digit_limit = 12
negative_flag = False

def button_click(number): 
# button input function
    global expression

    if number == "<--":
        backspace()

    elif number == "-":
        if not expression or expression[-1] in ["+", "-", "*", "/"]:
            negative_flag = True   # Handling errors with negative nos.
            main.config(text=expression+"-")

        else:
            expression += "-"
            main.config(text=expression)

    elif(len(expression)<input_dig_limit):
        expression += str(number)
        #negative_flag = False
        main.config(text=expression)

def clear_output(): 
# Clear button function
    global expression
    expression = ""
    main.config(text="")

def evaluate_expression(): 
# expression evaluation function
    global expression

    try:
        if negative_flag:
            expression += "-"

        result = eval(expression)
        result_str = str(result)

        operators = ["+", "-", "/", "*"]

        """Converting result to int if output
           is whole number and not float"""

        for operator in operators:
            if operator in expression and isinstance(result, float):
                if result.is_integer():
                    result_str = str(int(result))
                break

        if len(result_str) > output_digit_limit:
            rounded_result = format(result, f".{output_digit_limit-5}f")
            main.config(text=str(rounded_result))
            expression = str(rounded_result)

        else:
            main.config(text=result_str)
            expression = result_str

    except Exception as e:
        main.config(text="Error")
        print(e)
        expression = ""

def factorial(): # factorial function
    global expression

    try:
        result = math.factorial(eval(expression))
        main.config(text=str(result))
        expression = str(result)

    except Exception as e:
        main.config(text="Error")
        print(e)
        expression = ""

def square_root(): # square root function
    global expression
    try:
        result = math.sqrt(eval(expression))
        result_str = str(result)

        if len(str(result)) > output_digit_limit:
            rounded_result = format(result, f".{output_digit_limit-5}f")
            main.config(text=str(rounded_result))
            expression = str(rounded_result)

        elif result.is_integer():  # Check if result is a whole number
            main.config(text=str(int(result)))  # Display as integer
            expression = str(int(result))

        else:
            main.config(text=result_str)
            expression = result_str
    except Exception as e:
        main.config(text="Error")
        print(e)
        expression = ""

def backspace(): # backspace function
    global expression
    if len(expression) > 0:
        expression = expression[:-1]
        main.config(text=expression)


#Following is the creation of all buttons 

clear = Button(calculator, 
               text="C",
               width=5, 
               font=("Arial","14"), 
               command=clear_output, 
               bg=op_color)
clear.grid(row=1, column=0, padx=5, pady=5)

sqrt = Button(calculator, 
              text="√",
              width=5, 
              font=("Arial", "14"), 
              command=square_root, 
              bg=op_color)
sqrt.grid(row=1, column=1, padx=5, pady=5)

slash = Button(calculator, 
               text="/", 
               width=5, 
               font=("Arial", "14"), 
               command=lambda: button_click("/"), 
               bg=op_color)
slash.grid(row=1, column=2, padx=5, pady=5)

backspace = Button(calculator, 
                   text="<--", 
                   width=5, 
                   font=("Arial", "14"), 
                   command=backspace, 
                   bg=op_color)
backspace.grid(row=1, column=3, pady=5)

seven = Button(calculator, 
               text="7", 
               width=5, 
               font=("Arial","14"), 
               command=lambda: button_click(7),
               bg=num_color)
seven.grid(row=2, column=0, padx=5, pady=5)

eight = Button(calculator, 
               text="8", 
               width=5, 
               font=("Arial","14"), 
               command=lambda: button_click(8), 
               bg=num_color)
eight.grid(row=2, column=1, padx=5, pady=5)

nine = Button(calculator, 
              text="9", 
              width=5, 
              font=("Arial","14"), 
              command=lambda: button_click(9), 
              bg=num_color)
nine.grid(row=2, column=2, padx=5, pady=5)

star = Button(calculator, 
              text="*", 
              width=5,
              font=("Arial", "14"),
              command=lambda: button_click("*"),
              bg=op_color)
star.grid(row=2, column=3, pady=5)

four = Button(calculator, 
              text="4", 
              width=5, 
              font=("Arial","14"), 
              command=lambda: button_click(4), 
              bg=num_color)
four.grid(row=3, column=0, padx=5, pady=5)

five = Button(calculator, 
              text="5", 
              width=5, 
              font=("Arial","14"), 
              command=lambda: button_click(5), 
              bg=num_color)
five.grid(row=3, column=1, padx=5, pady=5)

six = Button(calculator, 
             text="6", 
             width=5, font=("Arial","14"), command=lambda: button_click(6), bg=num_color)
six.grid(row=3, column=2, padx=5, pady=5)

minus = Button(calculator, 
               text="-", 
               width=5, 
               font=("Arial", "14"), 
               command=lambda: button_click("-"), 
               bg=op_color) 
minus.grid(row=3, column=3, pady=5)

one = Button(calculator, 
             text="1", 
             width=5, 
             font=("Arial","14"),
             command=lambda: button_click(1),
             bg=num_color)
one.grid(row=4, column=0, padx=5, pady=5)

two = Button(calculator, 
             text="2", 
             width=5, 
             font=("Arial","14"),
             command=lambda: button_click(2),
             bg=num_color)
two.grid(row=4, column=1, padx=5, pady=5)

three = Button(calculator, 
               text="3", 
               width=5, 
               font=("Arial","14"), 
               command=lambda: button_click(3), 
               bg=num_color)
three.grid(row=4, column=2, padx=5, pady=5)

plus = Button(calculator, 
              text="+", 
              width=5, 
              font=("Arial", "14"), 
              command=lambda: button_click("+"),
              bg=op_color)
plus.grid(row=4, column=3, pady=5)

factorial = Button(calculator, 
                   text="!", 
                   width=5, 
                   font=("Arial","14"), 
                   command=factorial, 
                   bg=op_color)
factorial.grid(row=5, column=0, padx=5, pady=5)

zero = Button(calculator,
              text="0", 
              width=5, 
              font=("Arial","14"), 
              command=lambda: button_click(0),
              bg=num_color)
zero.grid(row=5, column=1, padx=5, pady=5)

decimal = Button(calculator, 
                 text=".", 
                 width=5, 
                 font=("Arial","14"), 
                 command=lambda: button_click("."), 
                 bg=num_color)
decimal.grid(row=5, column=2, padx=5, pady=5)

equals = Button(calculator, 
                text="=", 
                width=5, 
                font=("Arial", "14"), 
                command=evaluate_expression, 
                bg=op_color)
equals.grid(row=5, column=3, pady=5)

calculator.mainloop()
