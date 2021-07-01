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


def send_email(email_field, subject, body_template, records, variables):
    sent, total = 0, len(records)
    file = open('Logs/emails_sent.txt', 'w')
    file.close()

    for record in records:
        body = data.generate_body(body_template, record, variables)

        mail = EmailMessage()
        mail['From'] = sender_email
        mail['To'] = record[email_field]
        mail['Subject'] = subject
        mail.set_content(body)

        this = True
        while this:
            try:
                # noinspection PyUnresolvedReferences
                server.send_message(mail)
                sent += 1
                with open('Logs/emails_sent.txt', 'a') as file:
                    file.write(f"{sent}) {record[email_field]}\n")
                this = False

            except smtplib.SMTPServerDisconnected:
                ui.already_sent(sent, total)
                ui.connection_lost()
                sender_login()
            except Exception as err:
                ui.already_sent(sent, total)
                ui.unknown_error(err)
