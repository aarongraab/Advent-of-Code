total = 0
myNumbersMapped = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                   "eight": "8", "nine": "9"}

with open('input.txt', 'r') as file:
    for line in file:
        for word, value in myNumbersMapped.items():
            line = line.replace(word, value)
        count = ""
        for i in line:
            if i.isdigit():
                count += i
                break
        for i in line[::-1]:
            if i.isdigit():
                count += i
                break
        total += int(count)

print("Final total is:", total)
