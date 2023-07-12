from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
import time


def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)


def toggle_mode():
    global is_day_mode
    is_day_mode = not is_day_mode

    if is_day_mode:
        # Switch to day mode
        label.config(bg="white", fg="black")
        heading_label.config(bg="white", fg="black")
        toggle_button.config(image=moon_img_resized, bg="#f0f0f0",
                             activebackground="#f0f0f0")  # Moon image for night mode
    else:
        # Switch to night mode
        label.config(bg="black", fg="white")
        heading_label.config(bg="black", fg="white")
        toggle_button.config(image=sun_img_resized, bg="#333333",
                             activebackground="#333333")  # Sun image for day mode


root = Tk()
root.title("Internpe - Digital Clock")
root.geometry("450x370")
root.config(bg="#e9aebc")
root.resizable(False, False)  # Disable the maximize option
root.attributes("-topmost", True)  # Keep the window always on top

frame = Frame(root, bg="white", padx=20, pady=20)
frame.pack(expand=True)

heading = Label(frame, text=" INTERNPE VIRTUAL INTERNSHIP",
                      font=("Arial", 16), bg="white", fg="black")
heading.pack(ipadx=10, ipady=10)


heading_label = Label(frame, text=" Task-2 > Digital Clock ",
                      font=("Arial", 16), bg="white", fg="black")
heading_label.pack(padx= 10,pady=10,ipadx=10,ipady=10)

timer_frame = Frame(frame, padx=7, pady=10,borderwidth=2, relief="sunken")
timer_frame.pack()

label = Label(timer_frame, font=("Arial", 30), bg="white", fg="black")
label.pack()

button_frame = Frame(frame, bg="white")
button_frame.pack()

sun_img = Image.open("sun.png")
sun_img_resized = sun_img.resize((40, 40), Image.LANCZOS)
sun_img_resized = ImageTk.PhotoImage(sun_img_resized)

moon_img = Image.open("moon.png")
moon_img_resized = moon_img.resize((40, 40), Image.LANCZOS)
moon_img_resized = ImageTk.PhotoImage(moon_img_resized)

toggle_button = Button(button_frame, image=sun_img_resized,
                       command=toggle_mode, bd=0, bg="#f0f0f0", activebackground="#f0f0f0")
toggle_button.pack(padx=10, pady=10,ipadx=5,ipady=5)

is_day_mode = True  # Initially set to day mode

update_time()

root.mainloop()
