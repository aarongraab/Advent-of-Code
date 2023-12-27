total = 0
myNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open('input.txt', 'r') as file:
    'for line in file:'
    'file.readline()'
    line = file.readline()
    lineLength = len(line) - 1
    print(lineLength)
    print(line)

    count = ""
    a, b = 0, 5
    myString = "HelloWorld"
    print(myString[a:b])

    a, b = a+1, b+1
    print(myString[a:b])

    a, b = a+1, b+1
    print(myString[a:b])



'''
    for i in line:
        if i.isdigit():
            count += i
            break
    for i in line[::-1]:
        if i.isdigit():
            count += i
            break
        total += int(count)
print(total)
'''