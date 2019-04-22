class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return 'a:{}\nb:{}'.format(self.a*self.a, self.b*self.b)


if __name__ == '__main__':
    from sys import argv

    cal = Calculator(int(argv[1]), int(argv[2]))
    print(cal.square())

