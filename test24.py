class Car:
 FUEL_TYPES = ['бензин', 'дизель', 'электричество', 'гибрид']
 COLORS = []
 NUMBER_OF_CARS = 0

 def __init__(self, model, year, fuel_type, color):
  self.model = model
  self.year = year
  self.color = color
  self.fuel_type = self.is_valid_fuel_type(fuel_type, Car.FUEL_TYPES)
  if color not in Car.COLORS:
   Car.COLORS.append(color)
  Car.NUMBER_OF_CARS += 1
  self.number = Car.NUMBER_OF_CARS

 def __str__(self):
  return f"{self.model} {self.year} {self.fuel_type} {self.color}"

 @property
 def numbers(self):
  return f'{self.number} from {Car.NUMBER_OF_CARS}'

 @staticmethod
 def is_valid_fuel_type(fuel_type, fuel_types):
  res = None
  if fuel_type and fuel_types and isinstance(fuel_types, list):
   res = fuel_type if fuel_type in fuel_types else fuel_types[0]
  return res

 @classmethod
 def get_used_colors(cls):
  return len(cls.COLORS)

 @classmethod
 def get_number_of_cars(cls):
  return cls.NUMBER_OF_CARS


car_1 = Car('Zaz', 1979, 'дизель', 'black')
car_2 = Car('BMW', 2000, 'бензин', 'red')
car_3 = Car('VOLVO', 2012, 'электричествоcccc', 'black')
car_4 = Car('Mersedes', 2012, 'гибрид', 'black')

print('COLORS: ', Car.get_used_colors())  # -> 'COLORS: 2'
print('NUMBER_OF_CARS: ', Car.get_number_of_cars())  # -> 'NUMBER_OF_CARS: 4'
for item in (car_1, car_2, car_3, car_4):
 print('item:', item)
 print('numbers:', item.numbers)
