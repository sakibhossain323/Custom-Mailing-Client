from modules import ui
import csv
import re


def read_records():
    filepath = ui.open_csv()

    with open(filepath) as file:
        csv_obj = csv.DictReader(file)
        records = []
        for record in csv_obj:
            records.append(record)

    return records


def detect_email(record):
    fields = record.keys()
    email_fields = []

    for field in fields:
        entry = record[field]
        match_obj = re.search(r"(^[\w.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", entry)
        if match_obj is not None:
            email_fields.append(field)

    return email_fields


def read_contents():
    filepath = ui.open_txt()
    with open(filepath, 'r') as file:
        contents = file.read()
    return contents
