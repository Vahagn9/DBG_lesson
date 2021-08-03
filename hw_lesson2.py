ex_num = int(input("please input exercise number to run: "))

if ex_num <= 0 or ex_num > 6:
    print("Wrong exercise number entered")
# ===== exercise 1 =====
# Works for any positive int
elif ex_num == 1:
    print("running exercise:", ex_num)
    input_number = int(input("please input a positive int number: "))
    #   first method
    print("running first method...")
    for i in str(input_number):
        print(int(i))
    #   second method
    print("running second method...")
    if input_number < 0:
        print("not a positive number entered")
    else:
        # getting the number of digits from input_number
        temp = input_number
        digits_count = 0
        while temp > 0:
            temp //= 10
            digits_count += 1
        # getting and printing digits started from 1st
        for i in range(digits_count - 1, -1, -1):
            print(input_number // 10 ** i)
            input_number %= 10 ** i
# ===== exercise 2 =====
elif ex_num == 2:
    print("running exercise:", ex_num)
    my_str = input("enter a string: ")
    # my_str = "test string"
    char_count = 0
    for i in my_str:
        char_count += 1
    print("The number of characters :", char_count)
# ===== exercise 3 =====
elif ex_num == 3:
    print("running exercise:", ex_num)
    P = int(input("please input int number:"))
    is_prime = True
    if P < 2:
        is_prime = False
    else:
        for i in range(2, P):
            if P % i == 0:
                is_prime = False
                break
    if is_prime:
        print("The number is Prime")
    else:
        print("The number is not Prime")
# ===== exercise 4 =====
elif ex_num == 4:
    print("running exercise:", ex_num)
    for i in range(1, 6):
        print(i, 0, sep=". ")

# ===== exercise 5 =====
elif ex_num == 5:
    print("running exercise:", ex_num)
    a = int(input("please input the first number:"))
    b = int(input("please input the second number:"))
    c = int(input("please input the third number:"))
    if a + b == c or a + c == b or c + b == a:
        print("yes")
# ===== exercise 6 =====
elif ex_num == 6:
    print("running exercise:", ex_num)
    given_num = int(input("please input a number:"))
    series_sum = 0
    for i in range(given_num + 1):
        series_sum += i
    print("The sum of a number series from 0 to", given_num, "inclusive is :", series_sum)
