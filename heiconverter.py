import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def convert_heic_to_image_format(heic_file_path, output_dir, image_format):
    # Open the HEIC image using Pillow
    image = Image.open(heic_file_path)

    # Generate the output file path
    output_file_path = os.path.join(
        output_dir, os.path.splitext(os.path.basename(heic_file_path))[0] + "." + image_format
    )

    # Save the image in the specified format
    image.save(output_file_path, image_format)

    return output_file_path


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("HEIC files", "*.heic")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)


def browse_output_dir():
    output_dir = filedialog.askdirectory()
    if output_dir:
        entry_output_dir.delete(0, tk.END)
        entry_output_dir.insert(0, output_dir)

def convert():
    heic_file_path = entry_file_path.get()
    output_dir = entry_output_dir.get()
    image_format = format_selection.get()

    if heic_file_path and output_dir:
        if image_format:
            image_format = image_format.lower()
            if image_format in ["png", "jpg", "gif"]:
                if image_format == "jpg":
                    image_format = "jpeg"
                converted_file_path = convert_heic_to_image_format(
                    heic_file_path, output_dir, image_format
                )
                lbl_status.config(
                    text="HEIC file converted to {}:/n{}".format(image_format.upper(), converted_file_path)
                )
            else:
                lbl_status.config(text="Invalid image format. Please select PNG, JPG, or GIF.")
        else:
            lbl_status.config(text="Please select an image format.")
    else:
        lbl_status.config(text="Please select a HEIC file and output directory.")


# Create the main window
window = tk.Tk()
window.title("HEIC Converter")

# Create the file selection label and entry
lbl_file_path = tk.Label(window, text="HEIC File:")
lbl_file_path.pack()

entry_file_path = tk.Entry(window, width=50)
entry_file_path.pack()

btn_browse_file = tk.Button(window, text="Browse", command=browse_file)
btn_browse_file.pack()

# Create the output directory selection label and entry
lbl_output_dir = tk.Label(window, text="Output Directory:")
lbl_output_dir.pack()

entry_output_dir = tk.Entry(window, width=50)
entry_output_dir.pack()

btn_browse_output_dir = tk.Button(window, text="Browse", command=browse_output_dir)
btn_browse_output_dir.pack()

# Create the format selection label and option menu
lbl_format = tk.Label(window, text="Output Format:")
lbl_format.pack()

format_selection = tk.StringVar(window)
format_selection.set("PNG")  # Default selection

option_menu = tk.OptionMenu(window, format_selection, "PNG", "JPG", "GIF")
option_menu.pack()

# Create the convert button
btn_convert = tk.Button(window, text="Convert", command=convert)
btn_convert.pack()

# Create the status label
lbl_status = tk.Label(window, text="")
lbl_status.pack()

# Start the GUI event loop
window.mainloop()
