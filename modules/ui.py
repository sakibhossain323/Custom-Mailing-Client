import tkinter as tk
from tkinter import filedialog


def project_title(title):
    print(80*'=')
    print(title.center(80, '-'))
    print(80*'_' + '\n')


def open_csv():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(title='Select Records',
                                          filetypes=(('CSV (*.csv)', '*.csv'), ))
    root.destroy()

    print(filepath + '\n')
    return filepath


def csv_info(len_records, len_fields):
    print(f"Records: {len_records}\t\tFields: {len_fields}", end='')


def select_email(fields_email):
    length = len(fields_email)
    email_field = None

    if length == 1:
        email_field = fields_email[0]
        print(f"\t\tField of emails: {email_field}\n")
    else:
        print("\n\nEmail addresses detected in:")
        for i in range(length):
            print(f"{i+1}) {fields_email[i]}")

        selected = False
        while not selected:
            try:
                index = int(input(f"Select primary email field(1-{length}): "))
                email_field, selected = fields_email[index - 1], True
                print(f"\n'{email_field}' is selected as primary email field\n")
            except ValueError:
                print(f"\nInvalid selection! Please insert an integer from 1 to {length}\n")
            except IndexError:
                print(f"\nInvalid selection! Please insert an integer from 1 to {length}\n")

    return email_field


def open_txt():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(title='Select Contents',
                                          filetypes=(('Text Documents (*.txt)', '*.txt'), ))
    root.destroy()

    print(filepath + '\n')
    return filepath


def show_content(subject, body_template):
    print(f"Subject: {subject}")
    print(body_template)
    print(80*'-')


def invalid_variable(variable):
    print(f"Invalid Variable! %{{{variable}}}% doesn't match with any fields\n")
    input('Press Enter to close program...')
    exit(1)


def variables_matched(len_vars):
    print(f"All variables({len_vars}) matched and replaceable with records\n")
