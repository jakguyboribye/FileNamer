import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def rename_selected_files():
    file_paths = filedialog.askopenfilenames(title="Select files to rename")

    if not file_paths:
        return
    
    prefix = simpledialog.askstring("Input", "Enter filename prefix") or "file"

    for index, file_path in enumerate(file_paths, start=1):
        folder, old_filename = os.path.split(file_path)
        _, extension = os.path.splitext(old_filename)

        new_filename = f"{prefix}-{index}{extension}"
        new_path = os.path.join(folder, new_filename)

        os.rename(file_path, new_path)

    messagebox.showinfo("Done", "Files have been renamed successfully!")

root = tk.Tk()
root.withdraw()

rename_selected_files()
