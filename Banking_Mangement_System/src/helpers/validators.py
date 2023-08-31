import re


def validate_name(name):
    pattern = '[A-Za-z ]+'
    matcher = re.fullmatch(pattern, name)
    return matcher


def validate_username(username):
    pattern = '[A-Za-z1-9_]+'
    matcher = re.fullmatch(pattern, username)
    return matcher


def validate_phone(phone):
    pattern = '[0-9]{10}'
    matcher = re.fullmatch(pattern, phone)
    return matcher


def validate_email(email):
    pattern = '^[a-zA-Z][a-zA-Z0-9]+\@[a-zA-Z]+\.(in|net|com)'
    matcher = re.fullmatch(pattern, email)
    return matcher


def validate_number(number):
    pattern = '[0-9]+'
    matcher = re.fullmatch(pattern, number)
    if matcher is not None:
        num = int(number)
        if num < 0:
            matcher = None
    return matcher


def validate_password(password):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    matcher = re.fullmatch(pattern, password)
    return matcher
