import tkinter as tk
from tkinter import filedialog
from modules import mail


def unknown_error(error):
    print(f"\n{error}\nCouldn't resolve the error! Please contact sys.execute@gmail.com\n")
    input("Press Enter to close program...")
    exit(1)


def connection_error(error):
    print(f"{error}! Couldn't connect to SMTP server!\n")
    input('Press Enter to close program...')
    exit(1)


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
            except ValueError or IndexError:
                print(f"\nInvalid selection! Please insert an integer from 1 to {length}\n")
            except Exception as err:
                unknown_error(err)

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
    print(80*'_')


def invalid_variable(variable):
    print(f"Invalid Variable! %{{{variable}}}% doesn't match with any fields\n")
    input('Press Enter to close program...')
    exit(1)


def variables_matched(len_vars):
    print(f"All variables({len_vars}) matched and replaceable with records\n")


def get_login_info(tried):
    if tried == 0:
        print("Login to your gmail account")

    login_info = dict()
    login_info['email'] = input('Email: ')
    login_info['password'] = input('Password: ')
    return login_info


def authentication_error():
    print("\nLogin failed! SMTP authentication error. Possible reasons:")
    print("1) Email/password was incorrect.\n2) Your account doesn't allow access via app.")
    print("Please try again!\n")


def connection_lost():
    print("\nConnection lost to server! Trying to reconnect...")
    mail.connect_server()
    print("Connection reestablished. Please try again!\n")
