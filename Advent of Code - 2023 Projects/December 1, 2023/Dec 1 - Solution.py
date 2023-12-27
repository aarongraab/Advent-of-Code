total = 0
with open('input.txt', 'r') as file:
    for line in file:
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
print(total)
