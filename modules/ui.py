import tkinter as tk
from tkinter import filedialog


def open_csv():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(title='Select Records',
                                          filetypes=(('CSV (*.csv)', '*.csv'), ))
    root.destroy()

    print(filepath + '\n')
    return filepath


def open_txt():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(title='Select Contents',
                                          filetypes=(('Text Documents (*.txt)', '*.txt'), ))
    root.destroy()

    print(filepath + '\n')
    return filepath
