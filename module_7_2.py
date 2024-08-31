def custom_write(file_name, strings):
    strings_list = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            position = file.tell()
            file.write(string + '\n')
            strings_list[(len(strings_list) + 1, position)] = string
    file.close()
    return strings_list


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
