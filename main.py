from PyWatermark import waterMarkImages, getAvailableFonts
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox, HORIZONTAL


def select_file():
    """This is the function of the open file dialog box"""
    filetypes = (
        ('Image files', '*.png *.jpg *.jpeg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    file_path_in.delete(0, "end")
    file_path_in.insert(0, filename)


def output_path():
    """This is the function of the select output dictionary dialog box"""
    path_out = fd.askdirectory()
    output_loc.delete(0, "end")
    output_loc.insert(0, path_out + "/")


def create_watermark():
    """The main function of the app."""
    scale_percent = scale.get()
    opacity_value = round(scale_percent * 2.55)  # Converting percentage to opacity value (0-255)
    output_file = waterMarkImages(
        imageFile=file_path_in.get(),
        imageOutputPath=output_loc.get(),
        text=text.get(),
        opacity=opacity_value,
        fontName=selected_font(),
        size=listbox.get(listbox.curselection()),
        position=selected_position(),
    )
    messagebox.showinfo(title="Success", message="Watermarking was successful.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Peter's Watermark App")
window.config(padx=50, pady=50)

# Buttons:
open_button = Button(text="Open File", command=select_file)
select_output = Button(text="Select location", command=output_path)
create_watermark_button = Button(text="Create Watermark", command=create_watermark)

open_button.grid(column=1, row=0)
select_output.grid(column=1, row=3)
create_watermark_button.grid(column=0, row=22, columnspan=2)

# Labels:
image_select = Label(text="Select image: ")
file_path_in_label = Label(text="File path of the image: ")
watermark_text = Label(text="Text of the watermark: ")
output = Label(text="Select output file location: ")
output_path_label = Label(text="Output path: ")
set_opacity = Label(text="Set opacity: ")
choose_font = Label(text="Choose a font: ")
choose_size = Label(text="Choose the size: ")
position = Label(text="Watermark position: ")

image_select.grid(column=0, row=0, sticky="W")
file_path_in_label.grid(column=0, row=1, sticky="W")
watermark_text.grid(column=0, row=2, sticky="W")
output.grid(column=0, row=3, sticky="W")
output_path_label.grid(column=0, row=4, sticky="W")
set_opacity.grid(column=0, row=5, sticky="W")
choose_font.grid(column=0, row=7, sticky="W")
choose_size.grid(column=0, row=12, sticky="W")
position.grid(column=0, row=16, sticky="W")

# Entries:
file_path_in = Entry(width=28)
text = Entry(width=28)
output_loc = Entry(width=28)

file_path_in.grid(column=1, row=1)
text.grid(column=1, row=2)
output_loc.grid(column=1, row=4)

text.insert(0, "Watermark")

# Scale:
scale = Scale(from_=0, to=100, orient=HORIZONTAL, length=255)
scale.grid(column=1, row=5)
scale.set(100)


# Radio Buttons:
def selected_font():
    """From the radio button selection returns the font name"""
    radio_value = radio_state.get()
    font = fonts[radio_value]
    return font


radio_state = IntVar()
fonts = getAvailableFonts()
fonts.sort()
radiobutton1 = Radiobutton(text=fonts[0], value=0, variable=radio_state)
radiobutton2 = Radiobutton(text=fonts[1], value=1, variable=radio_state)
radiobutton3 = Radiobutton(text=fonts[2], value=2, variable=radio_state)
radiobutton4 = Radiobutton(text=fonts[3], value=3, variable=radio_state)
radiobutton5 = Radiobutton(text=fonts[4], value=4, variable=radio_state)

radiobutton1.grid(column=1, row=7, sticky="W")
radiobutton2.grid(column=1, row=8, sticky="W")
radiobutton3.grid(column=1, row=9, sticky="W")
radiobutton4.grid(column=1, row=10, sticky="W")
radiobutton5.grid(column=1, row=11, sticky="W")


def selected_position():
    """From the radio button selection returns the chosen position"""
    pos_value = pos_state.get()
    return pos_value


pos_state = StringVar()
pos_radio_1 = Radiobutton(text="Top Left", value="TL", variable=pos_state)
pos_radio_2 = Radiobutton(text="Top Right", value="TR", variable=pos_state)
pos_radio_3 = Radiobutton(text="Bottom left", value="BL", variable=pos_state)
pos_radio_4 = Radiobutton(text="Bottom Right", value="BR", variable=pos_state)

pos_radio_1.grid(column=0, row=17, sticky="W")
pos_radio_2.grid(column=1, row=17, sticky="W")
pos_radio_3.grid(column=0, row=18, sticky="W")
pos_radio_4.grid(column=1, row=18, sticky="W")

# Setting the default value:
pos_state.set("BR")


# List box:
def listbox_used():
    """Takes current selection from listbox"""
    return listbox.get(listbox.curselection())


listbox = Listbox(height=6, width=28)
sizes = ["XS", "S", "M", "L", "XL", "XXL"]
for item in sizes:
    listbox.insert(sizes.index(item), item)

# listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=1, row=12, sticky="W")
listbox.select_set(2)  # Setting the default value

window.mainloop()
