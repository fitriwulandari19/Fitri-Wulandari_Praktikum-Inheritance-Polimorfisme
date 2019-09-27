class SuperJunior(object):
    def __init__(self, f, a, l):
        self.fandom = f
        self.anggota = a
        self.leader = l

    def cetakdata(self):
        print("fandom\t: ", self.fandom)
        print("anggota\t: ", self.anggota)
        print("leader\t: ", self.leader)


class SuJu(SuperJunior):
    def __init__(self, f, a, l, m):
        self.fandom = f
        self.anggota = a
        self.leader = l
        self.maknae = m

    def cetakdata(self):
        print("fandom\t: ", self.fandom)
        print("anggota\t: ", self.anggota)
        print("leader\t: ", self.leader)
        print("maknae(termuda)\t: ", self.maknae)

def main():
    SuJu1 = SuJu("ELF", "13 orang", "Leeteuk", "Kyuhyun")
    
    SuJu1.cetakdata()

if __name__ == "__main__":
    main()
