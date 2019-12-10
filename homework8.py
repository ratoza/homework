print("This program asks for a number and tests if it is prime")
while True:
    try:
        read_line = input("Please give me an integer number")
        num = int(read_line)
    except ValueError:
        print("That was not a valid integer number")
        continue
    break

count = 0
while count < 100:
    for i in range(2, num // 2):
        if num % i == 0:
            print("The number", num, "is not prime")
            num = num + 1
            count = count + 1
    print("The number", num, "is prime")
    num = num+1
    count = count+1
