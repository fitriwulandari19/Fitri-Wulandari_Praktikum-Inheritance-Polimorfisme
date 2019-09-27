class tekoma(object):
    def __init__(self, a):
        self.a = a
    def cetakA(self):
        print("TeKom A = ", self.a)

class tekomb(object):
    def __init__(self, b):
        self.b = b
    def cetakB(self):
        print("TeKom B = ", self.b)

class tekomc(tekoma, tekomb):
    def __init__(self, a, b, c):
        #memanggil induk1.__init__)
        tekoma.__init__(self, a)
        #memanggil induk2.__init__)
        tekomb.__init__(self, b)
        self.c = c
    def cetakC(self):
        print("TeKom C = ", self.c)

def main():
    obj = tekomc("28 orang" , "29 orang", "31 orang")

    obj.cetakA()

    obj.cetakB()

    obj.cetakC()

if __name__ == "__main__":
    main()
