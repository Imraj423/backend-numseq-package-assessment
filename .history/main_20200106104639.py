from numseq import fib, geo, prime


def main():
    print("Prime Numbers")
    plist = prime.prime(100)
    for p in plist[-100:]:
        print(p)
    print("===== T or F =====")
    print("Is {} prime? {}".format(32, prime.is_prime(32)))
    print("Is {} prime? {}".format(181, prime.is_prime(181)))
    
    print("Fibonacci")
    for i in range(10):
        print("{}: {}".format(i, fib(i)))

    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))


if __name__ == "__main__":
    main()
