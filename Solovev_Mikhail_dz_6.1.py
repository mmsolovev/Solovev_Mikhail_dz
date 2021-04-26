with open('nginx_logs.txt') as file:
    my_list = []
    for line in file:
        text = line.split()
        my_list.append((text[0], text[5].replace('"', ''), text[6]))
print(my_list)
