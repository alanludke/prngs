"""
taken from
https://en.wikipedia.org/wiki/Primitive_root_modulo_n#Table_of_primitive_roots
n = 47
primitive roots modulo n = 5, 10, 11, 13, 15, 19, 20, 22, 23, 26, 29, 30, 31, 33, 35, 38, 39, 40, **41**, 43, 44, 45
order = 46
"""

# Parameters commonly use
_PRIMITIVE_ROOT = 48271
_MOD = 2147483647

""" Lehmer class (aka as Park-Miller)"""
class Lehmer:
    """ :returns Lehmer object
    :param a - element of high multiplicative order module m
    :param s - number of bits
    :param m - a big prime number or power of prime number
    :param seed - seed number

    num is the generated number
    """
    def __init__(self, seed, s, a=_PRIMITIVE_ROOT, m=_MOD):
        self.seed = seed
        self.s = s
        self.m = m
        self.a = a
        self.num = seed
        self.time = 0
        self.result = ''

    """ :returns result from the formula
    X(k+1) = a * X(k) mod m
    """
    def algorithm(self):
        self.num = (self.a * self.num) % self.m
        return self.num

    """
    runs the code (s - 1) times, each time it runs using 
    the last seed (saved in num), receives the result and appends
    the least significant digit to the result, creating
    a binary result of the desired s.
    It starts with 1 in the start (this will make sure
    that the number has 's' bits)
    """
    def calculate(self):
        result = "1"
        for _ in range(self.s - 1):
            rnd = self.algorithm()
            b = rnd % 2
            result += str(b)
        self.num = int(result, 2)
        self.result = result
        return result
