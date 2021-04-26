from itertools import zip_longest
import json

my_dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        len_users = sum(1 for line in users)
        len_hobby = sum(1 for lines in hobby)
        if len_users < len_hobby:
            exit(1)
        else:
            users.seek(0)
            hobby.seek(0)
            for line_users, line_hobby in zip_longest(users, hobby):
                if line_hobby is not None:
                    my_dict[line_users.strip()] = line_hobby.strip()
                else:
                    my_dict[line_users.strip()] = line_hobby

with open('dz_6.3.json', 'w', encoding='utf-8') as file:
    json.dump(my_dict, file, ensure_ascii=False)
print(my_dict)
