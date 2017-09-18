# ------------------------------------------------------------------------------------------------------------------------
def CapIgnoringScriptSearch(bible):
    plus_key = []
    minus_key = []

    user_input = input('(+)keyword: ')
    user_input = user_input.lower()
    plus_key.append(user_input)

    number_of_line = 0

    while True:
        stop_or_go = input('Type 1 to add (+)keyword, 2 for (-)keyword, 0 to search now: ')
        if stop_or_go == '0':
            break
        elif stop_or_go == '1':
            user_input = input('(+)keyword: ')
            user_input = user_input.lower()
            plus_key.append(user_input)
        elif stop_or_go == '2':
            user_input = input('(-)keyword: ')
            user_input = user_input.lower()
            minus_key.append(user_input)
        else:
            print('Invalid value. Try again.')

    line = 'Bible_search_line_default'

    while line != '':
        line = b.readline()
        lower_line = line.lower()
        for i, key in enumerate(plus_key):
            if key not in lower_line:
                break
            elif i == (len(plus_key)-1):
                if minus_key == []:
                    number_of_line += 1
                    print(line)
                else:
                    for k, key in enumerate(minus_key):
                        if key in lower_line:
                            break
                        elif k == (len(minus_key)-1):
                            number_of_line += 1
                            print(line)
    print('------------------------------------------------')
    print('{} verses'.format(number_of_line))
# ------------------------------------------------------------------------------------------------------------------------
def ScripSearch(bible):
    plus_key = []
    minus_key = []

    user_input = input('(+)keyword: ')
    plus_key.append(user_input)

    number_of_line = 0

    while True:
        stop_or_go = input('Type 1 to add (+)keyword, 2 for (-)keyword, 0 to search now: ')
        if stop_or_go == '0':
            break
        elif stop_or_go == '1':
            user_input = input('(+)keyword: ')
            plus_key.append(user_input)
        elif stop_or_go == '2':
            user_input = input('(-)keyword: ')
            minus_key.append(user_input)
        else:
            print('Invalid value. Try again.')

    line = 'Bible_search_line_default'

    while line != '':
        line = b.readline()
        for i, key in enumerate(plus_key):
            if key not in line:
                break
            elif i == (len(plus_key)-1):
                if minus_key == []:
                    number_of_line += 1
                    print(line)
                else:
                    for k, key in enumerate(minus_key):
                        if key in line:
                            break
                        elif k == (len(minus_key)-1):
                            number_of_line += 1
                            print(line)
    print('------------------------------------------------')
    print('{} verses'.format(number_of_line))
# ------------------------------------------------------------------------------------------------------------------------


kb = open("./KoreanBible.txt", 'r')
eb = open("./EnglishBible.txt", 'r')

while True:
    search_type = input('Type 1 for KoreanBible, 2 for EnglishBible: ')
    if search_type == '1':
        b = kb
        ScripSearch(b)
        break
    elif search_type == '2':
        b = eb
        while True:
            capital_type = input('Type 1 for ignore CAPITAL LETTER, 2 for normal search: ')
            if capital_type == '1':
                print('================================================')
                CapIgnoringScriptSearch(b)
                print('================================================')
                break
            elif capital_type == '2':
                print('================================================')
                ScripSearch(b)
                print('================================================')
                break
            else:
                print('Invalid value. Try again.')
        break
    else:
        print('Invalid value. Try again.')

# while True:
#     capital_type = input('Type 1 for ignore CAPITAL LETTER, 2 for normal search: ')
#     if capital_type == '1':
#         print('================================================')
#         CapIgnoringScriptSearch(b)
#         print('================================================')
#         break
#     elif capital_type == '2':
#         print('================================================')
#         ScripSearch(b)
#         print('================================================')
#         break
#     else:
#         print('Invalid value. Try again.')



kb.close()
eb.close()
