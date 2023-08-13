def extract_name(email):

    parts = email.split('@')
    name_parts = parts[0].split('.')
    name = ' '.join(name_parts).title()
    return name


emails = {}

while True:
    email = input("Email: ")
    if email == "":
        break

    name = extract_name(email)

    answer = input("Is your name {}? (Y/n) ".format(name))

    if answer.lower() != "y" and answer != "":
        name = input("Name: ")

    emails[email] = name

for email, name in emails.items():
    print("{} ({})".format(name, email))