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
    fields_email = []

    for field in fields:
        entry = record[field]
        match_obj = re.search(r"(^[\w.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", entry)
        if match_obj is not None:
            fields_email.append(field)

    return fields_email


def read_contents():
    filepath = ui.open_txt()
    with open(filepath, 'r') as file:
        contents = file.read()
    return contents


def get_variables(fields, body_template):
    variables = []
    obj = re.finditer(r"%{(.+?)}%", body_template)

    for i in obj:
        v = i.group(1)

        if v in variables:
            continue
        elif v in fields:
            variables.append(v)
        else:
            ui.invalid_variable(v)

    return variables


def generate_body(template, record, variables):
    body = template
    for v in variables:
        body = body.replace(f"%{{{v}}}%", record[v])

    return body
