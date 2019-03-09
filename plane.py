"""
Створити клас “Літак” , котрий містить поля:
- об'єм паливних баків в літрах
- назва
- кількість пасажирів

Створити консольну програму мовою Python і написати клас <Назва_із_завдання> який міститиме:
• Три додаткових поля, які найкраще описують даний клас
• Конструктор (із вказаними дефолтними значеннями)
• Деструктор
• Метод, що повертає стрічкове представлення класу
• Статичне поле
• Статичний метод, що повертає значення статичного поля
• В main() методі визначіть 3 об’єкти типу із завдання (з-за допомогою передачі
   різної кількості параметрів) та виведіть інформацію про них з-за допомогою
   методу з пункту 4 в консоль
"""


def xuy(self=0):
  pass


class Plane:

  _numOfPlanesWasRepaired = 0

  def __init__(self,
         nameOfPlane="NoName", volumeOfFuelTanksInLiters=0, numberOfPassangers=0,
         powerOfEngine=0, maxAltitudeInKilometers=0, massOfPlaneInTons=0
         ):
    self._name = nameOfPlane
    self._volumeOfFuel = volumeOfFuelTanksInLiters
    self._numberOfPassangers = numberOfPassangers
    self._powerOfEngine = powerOfEngine
    self._maxAltitude = maxAltitudeInKilometers
    self._massOfPlane = massOfPlaneInTons

  def __del__(self):
    print("I have deleted", self._name)
    print("I have deleted %s" % self._name)
    print(f"{self._name} was deleted")

  def __str__(self):
    return ', '.join((f"{name[1:]} = {value}" for name, value in self.__dict__.items()))

  __repr__ = __str__

  @staticmethod
  def repairPlanes(numberOfRepairedPlanes):
    Plane._numOfPlanesWasRepaired += numberOfRepairedPlanes


def main():
  mriya = Plane("Ан-225 «Мрія»", 411000, 70, 229.5, 11, 250)
  aerobus = Plane("Аеробус А380-800", numberOfPassangers=366)
  boeing = Plane("Боїнг 747-8F")
  print(mriya)
  print(aerobus)
  print(boeing)
  print(Plane._numOfPlanesWasRepaired)
  Plane.repairPlanes(3)
  print(Plane._numOfPlanesWasRepaired)


if __name__ == '__main__':
  main()
