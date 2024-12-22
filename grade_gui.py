import tkinter as tk
from tkinter import messagebox

def calculate_grades():
    try:
        total_marks = 0
        num_subjects = len(entries)
        for entry in entries:
            marks = float(entry.get())
            total_marks += marks
        
        average_marks = total_marks / num_subjects
        gpa = average_marks / 10  # Assuming marks are out of 100 and GPA is on a scale of 10

        if average_marks>=90:
            letter_grade = 'A+'
        elif average_marks <= 90:
            letter_grade = 'A'
        elif average_marks <= 80:
            letter_grade = 'B'
        elif average_marks <= 70:
            letter_grade = 'C'
        elif average_marks <= 60:
            letter_grade = 'D'
        elif average_marks <= 50:
            letter_grade = 'E'
        else:
            letter_grade = 'F'

        result = f"Average Marks: {average_marks:.2f}\nGPA: {gpa:.2f}\nLetter Grade: {letter_grade}"
        label_result.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def create_subject_entries():
    global entries
    num_subjects = int(entry_num_subjects.get())
    entries = []
    
    for i in range(num_subjects):
        label = tk.Label(root, text=f"Subject {i+1} Marks:")
        label.pack()
        entry = tk.Entry(root)
        entry.pack()
        entries.append(entry)

# Create the main window
root = tk.Tk()
root.title("Student Grade Tracker")

label_num_subjects = tk.Label(root, text="Enter the number of subjects:")
label_num_subjects.pack()
entry_num_subjects = tk.Entry(root)
entry_num_subjects.pack()

button_create_entries = tk.Button(root, text="Create Entries", command=create_subject_entries)
button_create_entries.pack()

label_placeholder = tk.Label(root, text="")  # Placeholder for spacing
label_placeholder.pack()

button_calculate = tk.Button(root, text="Calculate Grades", command=calculate_grades)
button_calculate.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

# Start the main event loop
root.mainloop()
