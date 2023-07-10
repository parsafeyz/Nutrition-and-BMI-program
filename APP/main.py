from tkinter import *
from tkinter import ttk
import customtkinter

def bmi(weight, height):
	return weight / (height/100)**2

def calculate():
    try:
        height = float(height_entry.get())
    except ValueError:
        clear_frame(frame2)
        Label(frame2, text="missing requst", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()
    try:
        weight = float(weight_entry.get())
    except ValueError:
        clear_frame(frame2)
        Label(frame2, text="missing requst", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()

    abmi = round(bmi(weight, height), 2)
    clear_frame(frame2)
    if 16 <= abmi < 18.5:
        Label(frame2, text="you are Underweight", font=("Cascadia Code Light", 25), fg="#0784b5", bg="#212121").pack()
        Label(frame2, text=abmi, font=("Cascadia Code Light", 25), fg="#0784b5", bg="#212121").pack()
    elif 18.5 <= abmi < 25:
        Label(frame2, text="you are Normal", font=("Cascadia Code Light", 25), fg="#6fff84", bg="#212121").pack()
        Label(frame2, text=abmi, font=("Cascadia Code Light", 25), fg="#6fff84", bg="#212121").pack()
    elif 25 <= abmi < 40:
        Label(frame2, text="you are Overweight", font=("Cascadia Code Light", 25), fg="#ef3352", bg="#212121").pack()
        Label(frame2, text=abmi, font=("Cascadia Code Light", 25), fg="#ef3352", bg="#212121").pack()
    elif abmi > 40 or abmi < 16:
        Label(frame2, text="your data is invalid but", font=("Cascadia Code Light", 25), fg="#ef3352",
              bg="#212121").pack()
        Label(frame2, text=abmi, font=("Cascadia Code Light", 25), fg="#ef3352", bg="#212121").pack()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def lose():
    global user_weight
    global user_height
    global user_age
    clear_frame(frame4)

    try:
        weight1 = float(user_weight.get())
        height1 = float(user_height.get())
        age1 = float(user_age.get())
    except:
        clear_frame(frame4)
        Label(frame4, text="missing requst", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()
    
    BMR = 10 * weight1 + 6.25 * height1 - 5 * age1 + 5  
    caloric_intake = BMR * 1.2 


    caloric_deficit = 500
    caloric_intake -= caloric_deficit

    protein_ratio = 0.3
    fat_ratio = 0.3
    carb_ratio = 0.4

    protein_intake = caloric_intake * protein_ratio / 4  
    fat_intake = caloric_intake * fat_ratio / 9 
    carb_intake = caloric_intake * carb_ratio / 4

    Label(frame4, text="your diet to lose weight", font=("Cascadia Code Light", 18), fg="#ef3352", bg="#212121").pack()
    Label(frame4, text=f"Daily calorie intake {round(caloric_intake, 1)}", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Daily protein intake {round(protein_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Amount of fat consumed daily {round(fat_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Amount of carbohydrates consumed daily {round(carb_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()

def get():
    global user_weight
    global user_height
    global user_age
    clear_frame(frame4)

    try:
        weight1 = float(user_weight.get())
        height1 = float(user_height.get())
        age1 = float(user_age.get())
    except:
        clear_frame(frame4)
        Label(frame4, text="missing requst", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()

    BMR = 10 * weight1 + 6.25 * height1 - 5 * age1 + 5  # نرخ متابولیسم پایه (Basal Metabolic Rate)
    caloric_intake = BMR * 1.2 


    caloric_surplus = 500
    caloric_intake += caloric_surplus

    protein_ratio = 0.3
    fat_ratio = 0.3
    carb_ratio = 0.4

    protein_intake = caloric_intake * protein_ratio / 4  
    fat_intake = caloric_intake * fat_ratio / 9 
    carb_intake = caloric_intake * carb_ratio / 4

    Label(frame4, text="your diet to get weight", font=("Cascadia Code Light", 18), fg="#ef3352", bg="#212121").pack()
    Label(frame4, text=f"Daily calorie intake {round(caloric_intake, 1)}", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Daily protein intake {round(protein_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Amount of fat consumed daily {round(fat_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Amount of carbohydrates consumed daily {round(carb_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()

def stable():  
    global user_weight
    global user_height
    global user_age
    clear_frame(frame4)

    try:
        weight1 = float(user_weight.get())
        height1 = float(user_height.get())
        age1 = float(user_age.get())
    except:
        clear_frame(frame4)
        Label(frame4, text="missing requst", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()

    BMR = 10 * weight1 + 6.25 * height1 - 5 * age1 + 5 
    caloric_intake = BMR * 1.2

    protein_ratio = 0.3
    fat_ratio = 0.3
    carb_ratio = 0.4

    protein_intake = caloric_intake * protein_ratio / 4  
    fat_intake = caloric_intake * fat_ratio / 9 
    carb_intake = caloric_intake * carb_ratio / 4

    Label(frame4, text="your diet to stable weight", font=("Cascadia Code Light", 18), fg="#ef3352", bg="#212121").pack()
    Label(frame4, text=f"Daily calorie intake {round(caloric_intake, 1)}", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Daily protein intake {round(protein_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Amount of fat consumed daily {round(fat_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()
    Label(frame4, text=f"Amount of carbohydrates consumed daily {round(carb_intake, 1)} gr", font=("Cascadia Code Light", 18), fg="#fedc6e", bg="#212121").pack()


# Setup_________________________________
root = customtkinter.CTk()
root.title("BMI")
root.geometry("700x700")
root.resizable(False,False)

# Tab creation__________________________
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# First tab___________________________
frame1 = Frame(notebook, bg="#212121")
frame1.pack(fill="both", expand=True)
notebook.add(frame1, text="BMI Calculator")

Label(frame1, text="hight (cm)", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()
height_entry = Entry(frame1, font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#706d6d")
height_entry.pack()

Label(frame1, text="Weight (kg)", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()
weight_entry = Entry(frame1, font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#706d6d")
weight_entry.pack()

Label(frame1, text="", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()

calculate_button = customtkinter.CTkButton(frame1, text="calculate", font=("Tahoma", 25), command=calculate)
calculate_button.pack()

Label(frame1, text="", font=("Cascadia Code Light", 18), fg="#03DAC6", bg="#212121").pack()

frame2 = Frame(frame1, height=150, width=150, bg="#212121")
frame2.pack(fill="both", expand=True)


# Second tab_________________________________________


frame3 = Frame(notebook, bg="#212121")
frame3.pack(fill="both", expand=True, )
notebook.add(frame3, text="Diet")

Label(frame3, text="age", font= ("Cascadia Code Light",18),fg= "#03DAC6", bg="#212121").pack()
user_age = Entry(frame3, font= ("Cascadia Code Light",18),fg= "#03DAC6", bg="#706d6d")
user_age.pack()


Label(frame3, text="hight (cm)", font= ("Cascadia Code Light",18),fg= "#03DAC6", bg="#212121").pack()
user_height = Entry(frame3, font= ("Cascadia Code Light",18),fg= "#03DAC6", bg="#706d6d")
user_height.pack()


Label(frame3, text="Weight (kg)", font= ("Cascadia Code Light",18),fg= "#03DAC6", bg="#212121").pack()
user_weight = Entry(frame3, font= ("Cascadia Code Light",18),fg= "#03DAC6", bg="#706d6d")
user_weight.pack()


Label(frame3, text="", font= ("Cascadia Code Light",18),fg= "#03DAC6", bg="#212121").pack()
v=IntVar()

lose_button = customtkinter.CTkButton(frame3, text="Weight loss", font=("Tahoma", 25), command=lose)
lose_button.pack(side="top")

Label(frame3, text=" ", font= ("Cascadia Code Light",2),fg= "#03DAC6", bg="#212121").pack()

get_button = customtkinter.CTkButton(frame3, text="Weight gain", font=("Tahoma", 25), command=get)
get_button.pack(side="top")

Label(frame3, text=" ", font= ("Cascadia Code Light",2),fg= "#03DAC6", bg="#212121").pack()

stable_button = customtkinter.CTkButton(frame3, text="Weight constant", font=("Tahoma", 25), command=stable)
stable_button.pack(side="top")

frame4 = Frame(frame3, height=150, width=150, bg="#212121")
frame4.pack(fill="both", expand=True)
root.mainloop()
