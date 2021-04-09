my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for word in my_list:
    for letter in word:
        if letter.isdigit():
            if len(word) > 1:
                new_list.extend(['"', word, '"'])
                break
            else:
                new_list.extend(['"', f'0{letter}', '"'])
        else:
            if letter == '+':
                new_list.extend(['"', f'+0{word[word.index(letter)+1]}', '"'])
                break
            elif letter == '-':
                new_list.extend(['"', f'-0{word[0:]}', '"'])
                break
            else:
                new_list.append(word)
                break
print(' '.join(new_list))
