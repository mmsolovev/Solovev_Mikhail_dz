def thesaurus(*args):
    people = {}
    for name in args:
        people.setdefault(name[0], [])
        people[name[0]].append(name)
    return people


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Михаил", "Алексей", "Павел"))
