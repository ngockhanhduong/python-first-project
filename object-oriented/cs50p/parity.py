def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


# basic syntax for writing if-else clause
def is_even_basic(n):
    if n % 2 == 0:
        return True
    else:
        return False


# better way to write if-else clause using Pythonic expressions
def is_even_better(n):
    return True if n % 2 == 0 else False


# best way to write if-else clause using the type of output of return
def is_even(n):
    return n % 2 == 0


main()