from numseq import fib, geo, prime


def main():
    print("Fib Seq")
    for i in range(5):
        print("{}: {}".format(i, fib.fib(i)))

    print("Geo Numbers")
    for i in range(5):
        print("{}: {} {} {}".format(i, geo.square(i), geo.triangle(i),
                                    geo.cube(i)))
    
    print("Prime Numbers")
    plist = prime.prime(100)
    
    for p in plist[-10:]:
        print(p)
    print("Is {} prime? {}".format(32, prime.is_prime(32)))
    print("Is {} prime? {}".format(181, prime.is_prime(181)))


if __name__ == "__main__":
    main()
