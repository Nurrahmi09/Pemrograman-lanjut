class FakultasTeknik:
  def __init__(self, Universitas, Fakultas, TahunAjar):
    self.univ = Universitas
    self.fak = Fakultas
    self.TA = TahunAjar
  def CetakData(self):
    print("Universitas  : ",self.univ)
    print("Fakultas     : ",self.fak)
    print("Tahun Ajaran : ",self.TA)
    
class TEKOM(FakultasTeknik):
  def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan):
    self.JA = JumlahAngkatan
    FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)
  def CetakData(self):
    print(200 * " ")
    print("Teknik Komputer")
    print("Universitas  : ",self.univ)
    print("Fakultas     : ",self.fak)
    print("Tahun Ajaran : ",self.TA)
    print("Jumlah Angkatan Prodi Teknik Komputer adalah" , self.JA)
    print(200 * " ")

class PTIK(FakultasTeknik):
  def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan, Jurusan):
    self.JA = JumlahAngkatan
    self.J = Jurusan
    FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)
  def CetakData(self):
    print(200 * " ")
    print("Pend. Teknik Informatika & Komputer")
    print("Universitas  : ",self.univ)
    print("Fakultas     : ",self.fak)
    print("Tahun Ajaran : ",self.TA)
    print("Jumlah Angkatan Prodi Pend. Teknik Informatika & Komputer adalah" , self.JA)
    print(200 * " ")
    
class Mekatronika(FakultasTeknik):
  def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan):
    self.JA = JumlahAngkatan
    FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)
  def CetakData(self):
    print(200 * " ")
    print("Pend. Vokasi Mekatronika")
    print("Universitas  : ",self.univ)
    print("Fakultas     : ",self.fak)
    print("Tahun Ajaran : ",self.TA)
    print("Jumlah Angkatan Prodi Pend. Vokasi Mekatronika" , self.JA)
    print(200 * " ")
    
def main():
 
  a = FakultasTeknik ("UNM", "Teknik", 2018)
  a.CetakData()
  
  del a
  
  a = TEKOM("UNM", "Teknik", 2018 , 2)
  a.CetakData()
  
  b = PTIK("UNM", "Teknik", 2018, 9, "Pend. Teknik Elektro")
  b.CetakData()
  
  del b
  b = Mekatronika("UNM", "Teknik", 2018, 2)
  b.CetakData()
  
if __name__ == "__main__":
  main()
