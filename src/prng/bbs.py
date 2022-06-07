PRIME1 = 1000000000547
PRIME2 = 1000000016531

""" BBS class"""
class BBS:
    """ :returns a BBS object
    :param seed - seed number
    :param prime1 and prime2 - prime numbers that will generate m
    :param s - number of bits

    'number' is the generated pseudo-random number
    """
    def __init__(self, seed, s, p1=PRIME1, p2=PRIME2):
        self.time = 0
        self.m = p1 * p2
        self.seed = seed
        self.s = s
        self.result = ''
        self.number = seed

    """ :returns result from the formula
    x(n+1) = x(n)² mod M
    """
    def algorithm(self):
        self.number = pow(self.number, 2) % self.m
        return self.number

    """
    runs the code (s - 1) times, each time it runs using 
    the last seed (saved in number), receives the result and appends
    the least significant digit to the result, creating
    a binary result of the desired s.
    It starts with 1 in the beginning
    """
    def calculate(self):
        result = "1"
        for _ in range(self.s - 1):
            rnd = self.algorithm()
            b = rnd % 2
            result += str(b)
        self.number = int(result, 2)
        self.result = result
        return result
