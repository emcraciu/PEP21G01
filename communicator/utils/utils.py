def primes(max_prime):
    _primes = []
    for number in range(1, max_prime + 1):
        if number < 3:
            _primes.append(number)
            continue
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            _primes.append(number)
    return _primes
