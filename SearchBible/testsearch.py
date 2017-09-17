f = open('./testsearch.txt','r')
for i in range(5):
    line = f.readline()
    if line == '':
        print('blank line')
    print(line)
