#Quiz Game in Python
import json
from tkinter import *
import random

# Global variables
current_question = 0
score = 0
num_questions = 5
shuffled_questions = []

def load_questions(file_path):
    try:
        with open(file_path, "r") as file:
            questions = json.load(file)
            return questions
    except FileNotFoundError as e:
        print(f"Failed to load questions from file: {e}")
        return []

def format_question(question):
    options = question["options"]
    random.shuffle(options)
    return {
        "question": question["question"],
        "options": options,
        "answer": question["answer"]
    }

def initialize_quiz():
    global shuffled_questions

    questions = load_questions("questions.json")
    if len(questions) < num_questions:
        print("Insufficient questions in the file.")
        return

    shuffled_questions = random.sample(questions, num_questions)
    shuffled_questions = [format_question(question) for question in shuffled_questions]
    display_question()

def check_answer(answer):
    global current_question, score

    selected_option = answer
    if selected_option == shuffled_questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question == num_questions:
        display_final_results()
    else:
        display_question()

def display_question():
    global current_question

    question_text.set(shuffled_questions[current_question]["question"])
    for i in range(4):
        option_buttons[i].configure(text=shuffled_questions[current_question]["options"][i])

def display_final_results():
    global score, current_question

    question_text.set("Quiz completed!")
    final_result_text = f"You scored {score} out of {num_questions}.\n"
    if score == num_questions:
        final_result_text += "Congratulations! You got all the answers correct!"
    elif score == 0:
        final_result_text += "Oops! You didn't get any answer correct."
    else:
        final_result_text += f"Nice job! You got {score} answers correct."

    for button in option_buttons:
        button.configure(state=DISABLED)

    final_result_label.configure(text=final_result_text)
    play_again_button.pack(side=TOP)  # Show the "Play Again" button

def play_again():
    global current_question, score, shuffled_questions

    current_question = 0
    score = 0
    shuffled_questions = []

    for button in option_buttons:
        button.configure(state=NORMAL)

    initialize_quiz()
    final_result_label.configure(text="")
    play_again_button.pack_forget()  # Hide the "Play Again" button

# Create the quiz window
quiz = Tk()
quiz.geometry('600x500')
quiz.title("Quiz Game")
quiz.configure(bg='#E8F0FE')

# Create header label
header = Label(quiz, 
         text="Quiz Game", 
         font=('Arial', 20), 
         pady=20, 
         bg='#3F51B5', 
         fg='white', 
         width=40)
header.pack()

# Create question label
question_text = StringVar()
question_label = Label(quiz, 
                 textvariable=question_text, 
                 font=('Arial', 16), 
                 wraplength=500, 
                 bg='#E8F0FE', 
                 fg='#333333')
question_label.pack()

# Create answer option buttons
option_buttons = []
for i in range(4):
    option_buttons.append(Button(quiz, 
                                 text="", 
                                 width=20, 
                                 font=('Arial', 14), 
                                 bg='#3F51B5', 
                                 fg='white',
                                 command=lambda i=i: check_answer(shuffled_questions[current_question]["options"][i])))
    option_buttons[i].pack(pady=5)

# Create final result label
final_result_label = Label(quiz, 
                     font=('Arial', 14), 
                     pady=20,
                     bg='#E8F0FE', 
                     fg='#333333')
final_result_label.pack()

# Initialize the quiz
initialize_quiz()

# Create play again button
play_again_button = Button(quiz, 
                           text="Play Again", 
                           font=('Arial', 14), 
                           command=play_again, 
                           bg='#FF7F50')
play_again_button.pack_forget()  # Hide the "Play Again" button initially

exit_button = Button(quiz, 
                     text="Exit", 
                     font=('Arial', 14), 
                     command=exit)
exit_button.pack(side=BOTTOM)

quiz.mainloop()
