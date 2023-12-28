total = 0
myNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open('input.txt', 'r') as file:
    'for line in file:'
    file.readline()
    line = file.readline()
    lineLength = len(line) - 1
    print(lineLength)
    print(line)


    def find_word_number(myString):
        a, b = 0, 5
        while b != len(myString) + 1:
            print(myString[a:b])
            for i in myNumbers:
                if i in myString[a:b]:
                    if len(i) == 3:
                        print("Length is 3")
                        return i, a + 2
                    if len(i) == 4:
                        print("Length is 4")
                        return i, a + 1
                    else:
                        print("Length is 5")
                        return i, a
            a, b = a + 1, b + 1
        return "None", "None"

    def find_word_number_backwards(myString):
        myString2 = "HellosixWorld"
        myString1 = myString2[::-1]
        a, b = 0, 5
        while b != len(myString1) + 1:
            print(myString1[a:b])
            for i in myNumbers:
                if i[::-1] in myString1[a:b]:
                    if len(i) == 3:
                        print("Length is 3")
                        return i, 0 + len(myString1) - b

                    if len(i) == 4:
                        print("Length is 4")
                        return i, 0 + len(myString1) - b

                    else:
                        print("Length is 5")
                        return i, 0 + len(myString1) - b
            a, b = a + 1, b + 1
        return "None", "None"

'''
    wordNum, index = find_word_number(line)
    print("The word number is:", wordNum, "\nPosition:", index)
'''

wordNum, index = find_word_number_backwards(line[::-1])
print("The word number is:", wordNum, "\nPosition:", index)

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
