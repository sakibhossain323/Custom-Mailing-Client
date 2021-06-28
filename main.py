from modules import data


# Reading records from csv file
records = data.read_records()

# Detecting fields containing email
email_fields = data.detect_email(records[0])

# Reading contents from text file
contents = data.read_contents()
subject, body_template = contents.split('\n', 1)

input()
