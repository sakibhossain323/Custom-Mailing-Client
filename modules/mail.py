from modules import data, ui
from email.message import EmailMessage
import smtplib


server, sender_email = None, None


def connect_server():
    try:
        global server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
    except Exception as err:
        ui.connection_error(err)


def sender_login():
    logged_in, tried = False, 0
    while not logged_in:
        try:
            info = ui.get_login_info(tried)
            # noinspection PyUnresolvedReferences
            server.login(info['email'], info['password'])

            logged_in = True
            global sender_email
            sender_email = info['email']

        except smtplib.SMTPAuthenticationError:
            ui.authentication_error()
            tried += 1
        except smtplib.SMTPServerDisconnected:
            ui.connection_lost()
            tried += 1
        except Exception as err:
            ui.unknown_error(err)
