from faker import Faker
import random
import string

f = Faker("en_US")


def random_str(str_len):
    return "".join(random.choice(string.ascii_letters+string.digits) for _ in range(str_len))


def random_num(digits_len):
    return "".join(random.choice(string.digits) for _ in range(digits_len))


def name():
    return f.name()











if __name__ == '__main__':
    print(name())
    print(random_str(9))
    print(random_num(12))