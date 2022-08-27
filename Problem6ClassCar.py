'''
THIS IS NOT THE QUESTION IN THE LAB ASSIGNMENT 7
'''



#Syed Hussain
#08/20/2022
#Problem number 6 - Modifying the following code with the Python Class ‘car'
#Adding two more attributes type and manufacturer and printing it in the end with the full specs.

class car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_color(self):
        return self.color
    def get_type(self):
        return self.type
    def get_manufacturer(self):
        return self.manufacturer
    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + self.type + self.manufacturer

car1 = car("Sports", 2012, "Blue"," coupe"," BMW")
car2 = car("Sedan", 2020, "Black", " 4dr", " Toyota")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
