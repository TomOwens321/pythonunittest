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
