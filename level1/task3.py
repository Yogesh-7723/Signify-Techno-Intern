import re

def email_valid(text):
    matches = re.findall('[a-zA-Z0-9]+@(gmail)+(.com)', text)
    if matches:
        print(f"{text} is valid...")
    else:
        print(f"{text} invalid email format..")



email_valid(input("enter any email id :"))


# Find all words that end with 'ain'


