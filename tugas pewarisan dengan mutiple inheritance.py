class SuJu_KRY(object):
    def __init__(self, a):
        self.a = a
    def cetakA(self):
        print("Super Junior KRY = ", self.a)

class SuJu_M(object):
    def __init__(self, b):
        self.b = b
    def cetakB(self):
        print("Super Junior M   = ", self.b)

class SuJu_DE(SuJu_KRY, SuJu_M):
    def __init__(self, a, b, c):
        #memanggil SuJu_KRY.__init__)
        SuJu_KRY.__init__(self, a)
        #memanggil SuJu_M.__init__)
        SuJu_M.__init__(self, b)
        self.c = c
    def cetakC(self):
        print("Super Junior D&E = ", self.c)

def main():
    obj = SuJu_DE("3 orang" , "7 orang", "2 orang")

    obj.cetakA()

    obj.cetakB()

    obj.cetakC()

if __name__ == "__main__":
    main()
