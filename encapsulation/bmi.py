class Bmi():
    def setdata(self, kg, m):
        self.kg = kg
        self.m = m

    def add(self):
        return self.kg / self.m * self.m

if __name__ == '__main__':
    b = Bmi()
    b.setdata(60, 161)
    print(b.add())