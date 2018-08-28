##############################################################
#
# primes.py source for unit test example
#
##############################################################

def is_prime(number):
    """return True if *number* is prime"""
    for element in range(2, number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """print the closest prime number larger than *number*"""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)

