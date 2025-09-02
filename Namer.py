import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# List of keywords that trigger grouping
KEYWORDS = ["final", "render", "temp", "copy"]

def rename_selected_files():
    file_paths = filedialog.askopenfilenames(title="Select files to rename")
    if not file_paths:
        return
    
    prefix = simpledialog.askstring("Input", "Enter filename prefix") or "file"

    # sort files by creation time
    file_paths = sorted(file_paths, key=lambda x: os.path.getctime(x))

    # counters
    general_index = 1
    keyword_counters = {kw.lower(): 1 for kw in KEYWORDS}

    for file_path in file_paths:
        folder, old_filename = os.path.split(file_path)
        name, extension = os.path.splitext(old_filename)

        # find if it has any of the keywords
        matched_keyword = None
        for kw in KEYWORDS:
            if kw.lower() in name.lower():
                matched_keyword = kw.lower()
                break
        
        # if theres a match, set count, rename and increment the keyword counter
        if matched_keyword:
            count = keyword_counters[matched_keyword]
            new_filename = f"{prefix}-{matched_keyword}-{count}{extension}"
            keyword_counters[matched_keyword] += 1
        # if no match, keep numbering normally
        else:
            new_filename = f"{prefix}-{general_index}{extension}"
            general_index += 1

        new_path = os.path.join(folder, new_filename)
        os.rename(file_path, new_path)

    messagebox.showinfo("Done", "Files have been renamed successfully!")

root = tk.Tk()
root.withdraw()
rename_selected_files()