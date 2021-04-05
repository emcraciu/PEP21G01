import random
from communicator.utils.utils import primes


class AlreadySetError(Exception):
    pass


class Connector:
    __shared_secret = None
    __local_secret = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def generate_prime(self):
        primes_list = list(filter(lambda no: True if no > 129 else False, primes(256)))
        # self.prime = primes_list[random.randint(0, len(primes_list) - 1)]
        self.prime = random.choice(primes_list)

    def get_prime(self, prime):
        if not getattr(self, "prime", False):
            self.prime = prime
        else:
            raise AlreadySetError('Value for prime already set to:', self.prime)

    def generate_base(self):
        if getattr(self, "prime", False):
            self.base = random.randint(2, self.prime - 1)
        else:
            raise AttributeError('Value for prime needs to be set first')

    def get_base(self, base):
        if not getattr(self, "base", False):
            self.base = base
        else:
            raise AlreadySetError('Value for base already set to:', self, base)

    def generate_local_secret(self):
        self.__local_secret = random.randint(2, self.prime)
        return pow(self.base, self.__local_secret) % self.prime

    def get_secret(self, secret):
        self.__shared_secret = pow(secret, self.__local_secret) % self.prime + 129


class Client(Connector):
    pass


class Server(Connector):
    pass
