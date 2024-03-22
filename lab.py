class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    @property
    def Weight(self):
        return self._weight

    @Weight.setter
    def Weight(self, value):
        self._weight = value

    @property
    def Height(self):
        return self._height

    @Height.setter
    def Height(self, value):
        self._height = value

    def BMI_Value(self):
        return self.weight / (self.height / 100) ** 2 
    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height

def main():
    weight = float(input("Masukkan berat dalam kilogram: "))
    height = float(input("Masukkan tinggi dalam sentimeter: "))
    person = BMI(weight, height)

    print("BMI orang tersebut adalah: {:.2f}".format(person.BMI_Value()))

if __name__ == "__main__":
    main()
