MAX = 1000000


def print3numbers(n):
    if n > MAX:
        return
    else:
        print3numbers(n+3)
        print(n)


def print_two_powers(n):
    if n> MAX:
        return
    else:
        print_two_powers(n<<1)
        print(n)


print_two_powers(1)
