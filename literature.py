import tkinter as tk
from tkinter import messagebox
import sqlite3

# Output:  T. Schrader. „Wissenschaftliche Texte finden, verstehen und schreiben“. Scribbr.com. https://www.scribbr.de/wissenschaftliches-schreiben/wissenschaftliche-texte/ (abgerufen 31.10.2022).

# Output whitout Author: „Wissenschaftliche Texte finden, verstehen und schreiben“. Scribbr.com. https://www.scribbr.de/wissenschaftliches-schreiben/wissenschaftliche-texte/ (abgerufen 31.10.2022).

# const allCitation = [
#    [false, "Template Matching", "OpenCV", "https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html", "06.07.2023"],
#    ["J. Malik, R. Dahiya, G. Sainarayanan", "citeseerx", "Harris Operator Corner Detection using Sliding Window Method", "https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=06b419ccfb4b63efa6c64cdb971bf2e7f5d7ca47", "06.07.2023"],
#    ["David G. Lowe", "University of British Columbia", "Distinctive Image Features from Scale-Invariant Keypoints", "https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf", "07.07.2023"],
#    ["E. Rublee, V. Rabaud, K. Konolige, G. Bradski", "willowgarage", "ORB: an efficient alternative to SIFT or SURF", "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6126544", "07.07.2023"],
#    ["D. Tyagi", "medium.com", "Introduction to FAST (Features from Accelerated Segment Test)", "https://medium.com/data-breach/introduction-to-fast-features-from-accelerated-segment-test-4ed33dde6d65", "07.07.2023"],
#    ["D. Tyagi", "medium.com", "Introduction to BRIEF(Binary Robust Independent Elementary Features)", "https://medium.com/@deepanshut041/introduction-to-brief-binary-robust-independent-elementary-features-436f4a31a0e6", "07.07.2023"],
# ];

# Datenbank erstellen und verbinden
conn = sqlite3.connect('literature.sqlite3')
c = conn.cursor()

# Tabelle erstellen
c.execute('''CREATE TABLE IF NOT EXISTS literature
             (id INTEGER PRIMARY KEY, author text, title text, website text, url text, accessed text)''')


def save():
    c.execute("INSERT INTO literature VALUES (NULL, ?, ?, ?, ?, ?)",
              (author_entry.get(), title_entry.get(), website_entry.get(), url_entry.get(), accessed_entry.get()))
    conn.commit()
    author_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    website_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    accessed_entry.delete(0, tk.END)
    messagebox.showinfo("save", "Add literature")
    update_liste()


def update_liste():
    text_widget.delete(1.0, tk.END)
    for row in c.execute('SELECT * FROM literature ORDER BY author'):
        if (row[1] != ""):
            text_widget.insert(
                tk.END, f"[P{row[0]}] {row[1]}. „{row[2]}“. {row[3]}. {row[4]} (abgerufen {row[5]})")
        else:
            text_widget.insert(
                tk.END, f"[P{row[0]}] „{row[2]}“. {row[3]}. {row[4]} (abgerufen {row[5]})")


root = tk.Tk()

bg_label = '#777777'
bg_entry = '#555555'
fg = 'white'

root.configure(bg='#777777')
author_label = tk.Label(root, text="Author:", bg=bg_label,
                        fg=fg).grid(row=0, column=0)
tk.Label(root, text="Title:", bg=bg_label, fg=fg).grid(row=1, column=0)
tk.Label(root, text="Title of Website:", bg=bg_label,
         fg=fg).grid(row=2, column=0)
tk.Label(root, text="Url:", bg=bg_label, fg=fg).grid(row=3, column=0)
tk.Label(root, text="Accessed:", bg=bg_label,
         fg=fg).grid(row=4, column=0)

author_entry = tk.Entry(root, bg=bg_entry, fg=fg)
author_entry.grid(row=0, column=1, sticky='ew')

title_entry = tk.Entry(root, bg=bg_entry, fg=fg)
title_entry.grid(row=1, column=1, sticky='ew')

website_entry = tk.Entry(root, bg=bg_entry, fg=fg)
website_entry.grid(row=2, column=1, sticky='ew')

url_entry = tk.Entry(root, bg=bg_entry, fg=fg)
url_entry.grid(row=3, column=1, sticky='ew')

accessed_entry = tk.Entry(root, bg=bg_entry, fg=fg)
accessed_entry.grid(row=4, column=1, sticky='ew')

tk.Button(root, text='Save', command=save, bg="#047c34", fg=fg).grid(
    row=5, column=0, columnspan=2, sticky='ew')

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=6, column=2, sticky='ns')

def copy_to_clipboard():
    root.clipboard_clear()
    text = text_widget.get("1.0", 'end-1c')
    root.clipboard_append(text)

copy_button = tk.Button(root, text="Copy to clipboard", command=copy_to_clipboard)
copy_button.grid(row=7, column=0, columnspan=2, sticky='ew')

text_widget = tk.Text(root, height=20, width=150,
                      wrap=tk.WORD, yscrollcommand=scrollbar.set, bg=bg_entry, fg=fg)
text_widget.grid(row=6, column=0, columnspan=2, sticky='nsew')

scrollbar.config(command=text_widget.yview)

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(1, weight=1)
update_liste()
# text_widget.config(state=tk.DISABLED)

root.mainloop()

conn.close()
