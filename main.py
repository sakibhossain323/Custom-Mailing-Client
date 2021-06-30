from modules import ui, data


ui.project_title('Custom Mailing Client')


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

input()
