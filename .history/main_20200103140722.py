from numseq import fib, geo, prime


def main():
    print("Fib Seq")
    for i in range(5):
        print("{}: {}".format(i, fib.fib(i)))

    print("Geo Numbers")
    for i in range(5):
        print("{}: {} {} {}".format(i, geo.square(i), geo.triangle(i),
                                    geo.cube(i)))
    n = 32
    print("Prime Numbers")
    plist = prime.prime(n)
    
    for p in plist[-1:]:
        print(p)
    print("Is {} prime? {}".format(int(prime.is_prime(n)), prime.is_prime(n)))
    print("Is {} prime? {}".format(prime.is_prime(n), prime.is_prime(n)))


if __name__ == "__main__":
    main()
