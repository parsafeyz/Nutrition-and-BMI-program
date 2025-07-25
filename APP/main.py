import tkinter as tk
from tkinter import ttk
import customtkinter

root = customtkinter.CTk()

# --- Window Size ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width * 0.5)   # 50% screen width
window_height = int(screen_height * 0.6)  # 60% screen height
root.geometry(f"{window_width}x{window_height}+{screen_width//4}+{screen_height//5}")  # center on screen
root.title("BMI & Diet App")

# --- Fonts & Sizes ---
LABEL_FONT = ("Cascadia Code Light", 20)
ENTRY_FONT = ("Cascadia Code Light", 20)
BUTTON_FONT = ("Tahoma", 20)
ENTRY_WIDTH = 20  # fixed width
ENTRY_HEIGHT = 40

# --- Helper ---
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def bmi(weight, height):
    return weight / (height / 100) ** 2

# --- BMI Calculate ---
def calculate():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        abmi = round(bmi(weight, height), 2)
    except ValueError:
        clear_frame(frame2)
        tk.Label(frame2, text="Missing input", font=LABEL_FONT, fg="#03DAC6", bg="#212121").pack()
        return

    clear_frame(frame2)
    if 16 <= abmi < 18.5:
        msg, color = "You are Underweight", "#0784b5"
    elif 18.5 <= abmi < 25:
        msg, color = "You are Normal", "#6fff84"
    elif 25 <= abmi < 40:
        msg, color = "You are Overweight", "#ef3352"
    else:
        msg, color = "Your data is invalid but", "#ef3352"

    tk.Label(frame2, text=msg, font=("Cascadia Code Light", 24), fg=color, bg="#212121").pack()
    tk.Label(frame2, text=abmi, font=("Cascadia Code Light", 24), fg=color, bg="#212121").pack()

def get_user_data():
    try:
        return float(user_weight.get()), float(user_height.get()), float(user_age.get())
    except ValueError:
        clear_frame(frame4)
        tk.Label(frame4, text="Missing input", font=LABEL_FONT, fg="#03DAC6", bg="#212121").pack()
        return None, None, None

def diet_result(cal, title):
    p, f, c = cal*0.3/4, cal*0.3/9, cal*0.4/4
    clear_frame(frame4)
    for line in [
        title,
        f"Calories: {round(cal, 1)} kcal",
        f"Protein: {round(p, 1)} g",
        f"Fat: {round(f, 1)} g",
        f"Carbs: {round(c, 1)} g"
    ]:
        tk.Label(frame4, text=line, font=LABEL_FONT, fg="#fedc6e", bg="#212121").pack(pady=3)

def lose():
    w, h, a = get_user_data()
    if w: diet_result((10*w + 6.25*h - 5*a + 5)*1.2 - 500, "Lose Weight Plan")

def gain():
    w, h, a = get_user_data()
    if w: diet_result((10*w + 6.25*h - 5*a + 5)*1.2 + 500, "Gain Weight Plan")

def maintain():
    w, h, a = get_user_data()
    if w: diet_result((10*w + 6.25*h - 5*a + 5)*1.2, "Maintain Weight Plan")

# --- Notebook ---
style = ttk.Style()
style.configure("TNotebook.Tab", font=("Arial", 16), padding=[20, 10])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, pady=20)

# --- BMI Tab ---
frame1 = tk.Frame(notebook, bg="#212121")
notebook.add(frame1, text="BMI Calculator")

container1 = tk.Frame(frame1, bg="#212121")
container1.pack(expand=True)  # center all

tk.Label(container1, text="Height (cm)", font=LABEL_FONT, fg="#03DAC6", bg="#212121").pack(pady=10)
height_entry = tk.Entry(container1, font=ENTRY_FONT, fg="#03DAC6", bg="#706d6d", width=ENTRY_WIDTH)
height_entry.pack(ipady=8, pady=5)

tk.Label(container1, text="Weight (kg)", font=LABEL_FONT, fg="#03DAC6", bg="#212121").pack(pady=10)
weight_entry = tk.Entry(container1, font=ENTRY_FONT, fg="#03DAC6", bg="#706d6d", width=ENTRY_WIDTH)
weight_entry.pack(ipady=8, pady=5)

customtkinter.CTkButton(container1, text="Calculate", font=BUTTON_FONT, height=45, command=calculate).pack(pady=20)

frame2 = tk.Frame(container1, bg="#212121")
frame2.pack(fill="both", expand=True)

# --- Diet Tab ---
frame3 = tk.Frame(notebook, bg="#212121")
notebook.add(frame3, text="Diet Planner")

container2 = tk.Frame(frame3, bg="#212121")
container2.pack(expand=True)

for label, var in [("Age", 'user_age'), ("Height (cm)", 'user_height'), ("Weight (kg)", 'user_weight')]:
    tk.Label(container2, text=label, font=LABEL_FONT, fg="#03DAC6", bg="#212121").pack(pady=5)
    entry = tk.Entry(container2, font=ENTRY_FONT, fg="#03DAC6", bg="#706d6d", width=ENTRY_WIDTH)
    entry.pack(ipady=8, pady=5)
    globals()[var] = entry

button_frame = tk.Frame(container2, bg="#212121")
button_frame.pack(pady=20)
customtkinter.CTkButton(button_frame, text="Lose", font=BUTTON_FONT, width=150, height=45, command=lose).pack(side="left", padx=15)
customtkinter.CTkButton(button_frame, text="Gain", font=BUTTON_FONT, width=150, height=45, command=gain).pack(side="left", padx=15)
customtkinter.CTkButton(button_frame, text="Maintain", font=BUTTON_FONT, width=150, height=45, command=maintain).pack(side="left", padx=15)

frame4 = tk.Frame(container2, bg="#212121")
frame4.pack(fill="both", expand=True)

root.mainloop()
