
# 1.
# 매개변수로 문자열을 받고, 해당 문자열이 red면 apple을, yellow면 banana를, green이면 melon을,
# 어떤 경우도 아닐 경우 I don't know를 리턴하는 함수를 정의하고, 사용하여 result변수에 결과를 할당하고 print해본다.
def outer():
    i = 0
    def base(string):
        '''
        This fuction matches colors to fruits.
            arguments(string) : colors(red, yellow, green)
            results(string) : fruits(apple, banana, melon)
        if there's no color-fruit data, it returns 'I don't know' or something like that.
        '''
        else_return_phrase = [
            "I Don't know.",
            'I have only 3 data for red, yellow, and green.',
            'You may know you shoud not enter this argument.',
            "Come on, I'm getting upset.",
            'What the Fuck are you doing?',
            'Seriously, stop it. I might gonna kill you.',
            'What? Seriously?',
            'Oh fuck! I will kill you! No matter what the cost is.',
            'Hey! Jimmy! Where are my guns?',
            'No, no, no, Jimmy, I need something bigger.',
            'Kreeeen TUHK! (door closing)',
            '(Hey, he is really coming to you. Be wise.)'
        ]
        nonlocal i

        if string.lower() == 'red':
            return 'apple'
        elif string.lower() == 'yellow':
            return 'banana'
        elif string.lower() == 'green':
            return 'melon'
        else:
            if i < 12:
                i += 1
            return else_return_phrase[i-1]

    return base

color_to_fruit = outer()

color_list = ['red','yellow','green','banana']

print('\n')
print('=========================================================================')
print('              Q#1. What fruits do you have with this color?              ')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('\n   [color]   :   [fruit] \n')
for item in color_list:
    print(' -','{:9}'.format(item),':',color_to_fruit(item))
print('\n')
while 1:
    usercolor = input('type any color you know. (or type "0" to exit):')
    if usercolor == '0':
        break
    else:
        print(' -','{:9}'.format(usercolor),':',color_to_fruit(usercolor),'\n')



# 2.
# 1번에서 작성한 함수에 docstring을 작성하여 함수에 대한 설명을 달아보고, help(함수명)으로 해당 설명을 출력해본다.
print('=========================================================================')
print('                  Q#2. What the hell is this function?                   ')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

answer = input('If you are curious of the function used in Q#1, \ntype any key, or not, type "0": ')
print(answer)
if answer != '0':
    help(color_to_fruit)

print('\n')

# 3
# 한 개 또는 두 개의 숫자 인자를 전달받아, 하나가 오면 제곱, 두개를 받으면 두 수의 곱을 반환해주는 함수를 정의하고 사용해본다.
print('=========================================================================')
print('            Q#3. Can you be more boring than this function?              ')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

def dex(*args):
     if len(args)==2:
         return args[0]*args[1]
     elif len(args)==1:
         return args[0]**2
     else:
         print("No, no, no. That's not a good try.")
         print('Only two or less arguments.')

print('dex(4): 4*4 = ',dex(4))
print('dex(2,7): 2*7 = ',dex(2,7))
print('dex(3,5,9):')
dex(3,5,9)

print('\n')

# 4
# 두 개의 숫자를 인자로 받아 합과 차를 튜플을 이용해 동시에 반환하는 함수를 정의하고 사용해본다.
print('=========================================================================')
print('            Q#4. Can you be more boring than this function?              ')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def sum_mul(int_a,int_b=0):
    s = 0
    m = 0
    if (type(int_a)==int or type(int_a)==float) and (type(int_b)==int or type(int_b)==float):
        s = int_a + int_b
        m = int_a * int_b
    return(s,m)

print('(2,3)')
print('2 + 3 = {}\n2 * 3 = {}'.format(sum_mul(2,3)[0],sum_mul(2,3)[1]))
print('(2.5,3.7)')
print('2.5 + 3.7 = {}\n2.5 * 3.7 = {}'.format(sum_mul(2.5,3.7)[0],sum_mul(2.5,3.7)[1]))
print('\n')

input_value = input('type any two numbers with ",". (ex. 2,3): ')
if ',' in input_value:
    keylist = input_value.split(',')
    a = int(keylist[0])
    b = int(keylist[1])
else:
    for item in input_value:
        if not item in '1234567890':
            print('Invalid Syntax: you can only type number or ','.')
            input_value = input('type any two numbers with ",". (ex. 2,3): ')
        else:
            a = a = int(input_value)
            b = 0

print('{0} + {1} = {2}\n{0} * {1} = {3}'.format(a,b,sum_mul(a,b)[0],sum_mul(a,b)[1]))
print('\n')


# 5
# 위치인자 묶음을 매개변수로 가지며, 위치인자가 몇 개 전달되었는지를 print하고 개수를 리턴해주는 함수를 정의하고 사용해본다.
def num_of_arg(*args):
    print(len(args))
    return len(args)

num_of_arg('sdaf','sdf','s','d','f','sa','sf','a')


# 6
# 람다함수와 리스트 컴프리헨션을 사용해 한 줄로 구구단의 결과를 갖는 리스트를 생성해본다.
l = ['{} * {} = {}'.format(x,y,x*y) for x in range(2,10) for y in range(1,10)]

l = [(lambda x,y : '{} * {} = {}'.format(x,y,x*y))(x,y) for x in range(2,10) for y in range(1,10)]

l = [''.join([str(x),' * ',str(y),' = ',str(x*y)]) for x in range(2,10) for y in range(1,10)]
