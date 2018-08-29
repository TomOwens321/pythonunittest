##############################################################
#
# primes.py source for unit test example
#
##############################################################

def is_prime(number):
    if number <= 1:
        return False

    """return True if *number* is prime"""
    for element in range(2, number):
        if number % element == 0:
            return False

    return True

def next_prime(number):
    index = number
    while not is_prime(index):
        index += 1
    print(index)
