from number_generator import NumberGenerator

def main():
    number_generator = NumberGenerator(144)
    print("\x1B[31;1mAll Fibonacci numbers that are also prime:\x1B[0m")
    print(number_generator.generate_prime_Fibonacci())
    print("\x1B[31;1mAll Fibonacci numbers that are sum of two other primes:\x1B[0m")
    number_generator.print_primeSplit()

if __name__ == '__main__':
    main()
