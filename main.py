from modules import data, mail, ui


# Show project title & connect to smtp server
ui.project_title('Custom Mailing Client')
mail.connect_server()


# Read records from csv file
records = data.read_records()
fields = records[0].keys()
ui.csv_info(len(records), len(fields))


# Detect fields containing emails & select one field
fields_email = data.detect_email(records[0])
email_field = ui.select_email(fields_email)


# Reading contents from text file
contents = data.read_contents()
subject, body_template = contents.split('\n', 1)
ui.show_content(subject, body_template)


# Extract variables from body template
variables = data.get_variables(fields, body_template)


# login to sender's gmail account
mail.sender_login()

input()
