from numseq import fib, geo, prime


def main():
    print("Fib Seq")
    for i in range(20):
        print("{}: {}".format(i, fib(i)))

    print("Geo Numbers")
    for i in range(10):
        print("{}: {} {} {}".format(i, geo.square(i), geo.triangle(i),
                                    geo.cube(i)))



if __name__== "__main__":
    main()
