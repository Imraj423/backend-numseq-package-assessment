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
    print("Is 999981 prime? {}".format(prime.is_prime(999981)))
    print("Is 999983 prime? {}".format(prime.is_prime(999983)))


if __name__ == "__main__":
    main()
