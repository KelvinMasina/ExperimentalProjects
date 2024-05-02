from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\u\Documents\PyCharmProjects\Tkinter\SignUp\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title('Smart Gate System')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
height = 540
width = 613
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# window.geometry("613x540")
window.configure(bg = "#1E1E1E")


canvas = Canvas(
    window,
    bg = "#1E1E1E",
    height = 532,
    width = 613,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    238.0,
    456.0,
    anchor="nw",
    text="Already have account?  ",
    fill="#FFFFFF",
    font=("yu gothic ui Regular", 16 * -1)
)

canvas.create_text(
    61.0,
    180.0,
    anchor="nw",
    text="First name",
    fill="#FFFFFF",
    font=("yu gothic ui Regular", 18 * -1)
)

canvas.create_text(
    61.0,
    332.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("yu gothic ui Regular", 18 * -1)
)

canvas.create_text(
    334.0,
    180.0,
    anchor="nw",
    text="Last name",
    fill="#FFFFFF",
    font=("yu gothic ui Regular", 18 * -1)
)

canvas.create_text(
    334.0,
    332.0,
    anchor="nw",
    text="Confirm Password",
    fill="#FFFFFF",
    font=("yu gothic ui Regular", 18 * -1)
)

canvas.create_text(
    61.0,
    256.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("yu gothic ui Regular", 18 * -1)
)

canvas.create_text(
    221.0,
    117.0,
    anchor="nw",
    text="CADECOM BLANTYRE",
    fill="#FFFFFF",
    font=("yu gothic ui Bold", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    169.0,
    221.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=61.0,
    y=205.0,
    width=216.0,
    height=31.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    169.0,
    373.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=61.0,
    y=357.0,
    width=216.0,
    height=31.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    442.0,
    221.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=334.0,
    y=205.0,
    width=216.0,
    height=31.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    442.0,
    373.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=334.0,
    y=357.0,
    width=216.0,
    height=31.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    305.5,
    297.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=61.0,
    y=281.0,
    width=489.0,
    height=31.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    cursor="hand2",
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=243.0,
    y=412.0,
    width=146.0,
    height=36.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    cursor="hand2",
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=243.0,
    y=486.0,
    width=146.0,
    height=36.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    306.0,
    61.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
