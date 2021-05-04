import re

EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')
my_dict = {'username': 'someone', 'domain': 'some_address'}


def email_parse(email_address):
    found_info = EMAIL.findall(email_address)[0]
    if found_info:
        name, domain = found_info
        my_dict['username'] = name
        my_dict['domain'] = domain
    else:
        raise ValueError(f'wrong email: {email_address}')
    return my_dict


print(email_parse('someone@geekbrains.ru'))
print(email_parse('solomix92@gmail.com'))
print(email_parse('solomix92@gmailcom'))
