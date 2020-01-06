from numseq import fib, geo, prime


def main():
    print("Fib Seq")
    for i in range(20):
        print("{}: {}".format(i, fib(i)))


if __name__== "__main__":
    main()
