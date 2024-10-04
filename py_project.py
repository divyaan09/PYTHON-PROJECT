<<<------------------------ LOVE CALCULATOR ---------------------------->>>

import tkinter as tk
from tkinter import messagebox

def calculate_love_score():
    name1 = entry_name1.get()
    name2 = entry_name2.get()
    zodiac1 = zodiac_var1.get().lower()
    zodiac2 = zodiac_var2.get().lower()

    if not name1 or not name2 or not zodiac1 or not zodiac2:
        messagebox.showerror("Input Error", "Please fill in all the fields!")
        return

    combine_string = name1 + name2
    lower_case_string = combine_string.lower()

    t = lower_case_string.count('t')
    r = lower_case_string.count('r')
    u = lower_case_string.count('u')
    e = lower_case_string.count('e')
    true = t + r + u + e

    l = lower_case_string.count('l')
    o = lower_case_string.count('o')
    v = lower_case_string.count('v')
    e = lower_case_string.count('e')
    love = l + o + v + e

    love_score = str(true) + str(love)
    love_score_int = int(love_score)

    compatible_zodiacs = {
        'aries': ['leo', 'sagittarius'],
        'taurus': ['virgo', 'capricorn'],
        'gemini': ['libra', 'aquarius'],
        'cancer': ['scorpio', 'pisces'],
        'leo': ['aries', 'sagittarius'],
        'virgo': ['taurus', 'capricorn'],
        'libra': ['gemini', 'aquarius'],
        'scorpio': ['cancer', 'pisces'],
        'sagittarius': ['aries', 'leo'],
        'capricorn': ['taurus', 'virgo'],
        'aquarius': ['gemini', 'libra'],
        'pisces': ['cancer', 'scorpio']
    }

    compatible_signs = compatible_zodiacs.get(zodiac2, [])
    if zodiac1 in compatible_signs:
        compatibility = "Your Zodiac signs are compatible!"
    else:
        compatibility = "Your Zodiac signs are not compatible."

    if love_score_int <= 20:
        stage_of_love = "1st stage: 'Attraction' (Dilkashi)"
    elif love_score_int > 20 and love_score_int <= 40:
        stage_of_love = "2nd stage: 'Attachment' (Oons)"
    elif love_score_int > 40 and love_score_int <= 60:
        stage_of_love = "3rd stage: 'Love' (Mohabbat)"
    elif love_score_int > 60 and love_score_int <= 75:
        stage_of_love = "4th stage: 'Trust' (Akidat)"
    elif love_score_int > 75 and love_score_int <= 85:
        stage_of_love = "5th stage: 'Worship' (Ibadat)"
    elif love_score_int > 85 and love_score_int <= 95:
        stage_of_love = "6th stage: 'Obsession' (Junoon)"
    else:
        stage_of_love = "LAST stage: 'Death' (Maut)"

    result_message = f"Love Score: {love_score}%\n{compatibility}\nYou are on the {stage_of_love}."
    messagebox.showinfo("Love Calculator Result", result_message)

root = tk.Tk()
root.title("Love Calculator")
root.geometry("400x500")
root.configure(bg='#FFDEE9')

label_title = tk.Label(root, text="💖 Love Calculator 💖", font=("Arial", 18), bg="#FFDEE9", fg="black")
label_title.pack(pady=20)

label_name1 = tk.Label(root, text="Enter His Name:", font=("Arial", 12), bg="#FFDEE9", fg="black")
label_name1.pack(pady=10)
entry_name1 = tk.Entry(root, width=30, font=("Arial", 12))
entry_name1.pack(pady=5)

label_name2 = tk.Label(root, text="Enter Her Name:", font=("Arial", 12), bg="#FFDEE9", fg="black")
label_name2.pack(pady=10)
entry_name2 = tk.Entry(root, width=30, font=("Arial", 12))
entry_name2.pack(pady=5)

label_zodiac1 = tk.Label(root, text="Select His Zodiac Sign:", font=("Arial", 12), bg="#FFDEE9", fg="black")
label_zodiac1.pack(pady=10)

zodiac_var1 = tk.StringVar()
zodiac_options = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
dropdown_zodiac1 = tk.OptionMenu(root, zodiac_var1, *zodiac_options)
dropdown_zodiac1.pack(pady=5)

label_zodiac2 = tk.Label(root, text="Select Her Zodiac Sign:", font=("Arial", 12), bg="#FFDEE9", fg="black")
label_zodiac2.pack(pady=10)

zodiac_var2 = tk.StringVar()
dropdown_zodiac2 = tk.OptionMenu(root, zodiac_var2, *zodiac_options)
dropdown_zodiac2.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Love Score", command=calculate_love_score, font=("Arial", 14), bg="pink", fg="black")
calculate_button.pack(pady=20)

root.mainloop()
