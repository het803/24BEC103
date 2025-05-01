def checker():
    x = int(input("Enter a number.: "))

    if str(x) == str(x)[::-1]:
        print("It is a palindrone number.")
    else:
        print("It is not a Palindrone number.")

    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                print("It is not a prime number..")
                break
        else:
            print("It is a prime number..")
    else:
        print("It is not a prime number.")

    if x > 0:
        armstrong_sum = 0
        temp = x
        while temp > 0:
            digit = temp % 10
            armstrong_sum += digit ** 3
            temp //= 10
        if x == armstrong_sum:
            print("It is an armstrong number.")
        else:
            print("It is not an Armstrong number.")
    else:
        print("It is not an Armstrong number.")

checker()