from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Function selected
def selected(event):
    for i in range(0, len(p_name)):
        if clicked.get() == p_name[i]:
            myLabel = Label(root, text = xlsname[i]).pack()
            break



# Width X Height
root.geometry("1920x1080")

# Displaying the Image
photo = PhotoImage(file = "cricket-stats.png")
label1 = Label(image = photo)
label1.pack()


#width, height
root.minsize(300, 100)
root.maxsize(1200, 988)

"""
myLabel = Label(text = "This is a Label")
myLabel.pack()
"""

p_name = [
    "MS Dhoni",
    "Rohit Shama",
    "Virat Kohli",
    "Shikhar Dhawan",
    "Rahul Dravid",
    "KL Rahul",
    "Sachin Tendulkar",
    "Yuvraj Singh",
    "Virendar Sehwag",
    "Gautam Gambhir",
    "Sourav Ganguly",
    "Ambati Rayudu"
]

xlsname = [
    "MS_Dhoni_ODI_record",
    "Rohit_Sharma_ODI_record",
    "Virat_Kohli_ODI_record",
    "Shikhar_Dhawan_ODI_record",
    "Rahul_Dravid_ODI_record",
    "KL_Rahul_ODI_record",
    "Sachin_Tendulkar_ODI_record",
    "Yuvraj_Singh_ODI_record",
    "Virendar_Sehwag_ODI_record",
    "Gautam_Gambhir_ODI_record",
    "Sourav_Ganguly_ODI_record",
    "Ambati_Rayudu_ODI_record"    
]

# Storing value of clicked Name
clicked = StringVar()

# Default placeholder for Dropdown Box
clicked.set("Select a Player")

# Dropdown Box
drop = OptionMenu(root, clicked, *p_name, command = selected)
drop.pack()

root.mainloop() 
