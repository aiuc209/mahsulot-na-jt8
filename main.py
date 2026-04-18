class Mahsulot:
    def __init__(self, nomi, narxi, chegirma):
        self.nomi = nomi
        self.narxi = narxi
        self.chegirma = chegirma

    def yakuniy_narx(self):
        return self.narxi - (self.narxi * self.chegirma / 100)

class Doxon:
    def __init__(self):
        self.mahsulotlar = []

    def mahsulot_qoshish(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def yakuniy_narxlar(self):
        for mahsulot in self.mahsulotlar:
            print(f"{mahsulot.nomi}: {mahsulot.yakuniy_narx()}")

doxon = Doxon()
doxon.mahsulot_qoshish(Mahsulot("Apple", 100, 10))
doxon.mahsulot_qoshish(Mahsulot("Banana", 50, 5))
doxon.mahsulot_qoshish(Mahsulot("Orange", 200, 20))
doxon.yakuniy_narxlar()
